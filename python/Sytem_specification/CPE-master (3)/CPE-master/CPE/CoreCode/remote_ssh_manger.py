import os
import subprocess

import CoreCode.logger as Logger
import Definitions.system_definitions as SystemDefinitions
import Definitions.message_definitions as MessageDefinitions
import Definitions.message_code_definitions as MessageCodeDefinitions

from CoreCode.service_manager import ServiceManager
import CoreCode.service_manager_helper_functions as HelperFunctions
import CoreCode.service_manager_linux_helper_functions as LinuxHelperFunctions

ECHO_COMMAND = 'echo'
PIPE_SYMBOL = "|"
SSH_KEYGEN_COMAMND = 'ssh-keygen -t rsa'
SPACE_CHARACTER = ' '
EXISTING_PASSPHRASE_OPTION = '-P'
NEW_PASSPHRASE_OPTION = '-N'
SSH_KEY_FILE_OPTION = '-f'
SSH_PRIVATE_KEY_FILE_PATH = '"/home/chiefnet/.ssh/id_rsa"'
SSH_PUBLIC_KEY_FILE_PATH = "/home/chiefnet/.ssh/id_rsa.pub"

OVERWRITE_FILE_YES_OPTION = 'y'

SSH_COMMAND_NAME = "ssh"

KILL_COMMAND = "kill"
SIGKILL_OPTION = "-9"

# By default Existing passphrase is empty string
EXISTING_PASSPHRASE = '""'
NEW_PASSPHRASE = '""'

RECEIVED_REMOTE_SSH_CONFIGURATION_UPDATE_NOTIFICATION = "Successfully received Update Remote SSH configuration notification"
DOWNLOADED_REMOTE_SSH_CONFIGURATION = "Successfully downloaded Remote SSH configuration"
SUCCESSFULLY_APPLIED_REMOTE_SSH_CONFIGURATION =  "Successfully applied Remote SSH configuration"
FAILED_TO_APPLY_REMOTE_SSH_CONFIGURATION = "Failed to access Remote SSH configuration"
EMPTY_REMOTE_SSH_CONFIGURATION_DATA = "Received empty Remote SSH configuration data"

RECEIVED_NOTIFICATION_TO_SHARE_SSH_PUBLIC_KEY =  "Successfully received Share SSH Public key notification"
SUCCESSFULY_SHARED_SSH_PUBLIC_KEY = "Successfully shared SSH Public Key"
FAILED_TO_SHARE_SSH_PUBLIC_KEY = "Failed to share SSH Public Key"


class RemoteSSHManager(ServiceManager):
    """
    RemoteSSHManager is derived from ServiceManager and is used to execute operations with respect to the remote SSH configuration for debugging purpose
    Arguments:
    data_manager:
        An instance of DataManager must be passed.s instance is used to fetch the configuration file from the endpoint 
        and also to send the routing information to the Backend
    response_manager:
        An instance of ResponseManager must be passed
    """
    def __init__(self, data_manager, response_manager):
        self.__logger = Logger.get_logger(__name__)
        self.__logger.info("RemoteSSHManager initializer starts")

        self.__remote_ssh_configuration_file_path = SystemDefinitions.USER_CONFIG_FILE_PATH + os.path.sep  + SystemDefinitions.REMOTE_SSH_CONFGURATION_FILE_NAME

        # Apply Remote SSH configuration, when the RemoteSSHManager instace is created, to restore the previous configuration when the CPE application starts.
        self.__apply_remote_ssh_configuration()
        
        event_dictionary = {}
        event_dictionary[MessageCodeDefinitions.UPDATE_REMOTE_SSH_CONFIGURATION] = self.__update_remote_ssh_configuration_event_routine
        event_dictionary[MessageCodeDefinitions.CREATE_AND_SHARE_NEW_SSH_KEY] = self.__create_share_new_ssh_key_routine

        ServiceManager.__init__(self, data_manager=data_manager, response_manager=response_manager, event_dictionary=event_dictionary)
        self.__logger.info("RemoteSSHManager initializer ends")
    

    def __update_remote_ssh_configuration_event_routine(self):
        self.__logger.info("Remote SSH configuration update event routine start")
        self._response_manager.send_response(message=self._message_dictionary, 
                                                status_code=MessageCodeDefinitions.RECEIVED_CONFIGURATION_UPDATE_NOTIFICATION,
                                                status_message=RECEIVED_REMOTE_SSH_CONFIGURATION_UPDATE_NOTIFICATION)
        
        fetch_remote_ssh_configuration_status, self.__remote_ssh_configuration  = self._fetch_configuration_from_endpoint()

        if fetch_remote_ssh_configuration_status == True:
            self._response_manager.send_response(message=self._message_dictionary, 
                                                    status_code=MessageCodeDefinitions.DOWNLOADED_CONFIGURATION_FILE,
                                                    status_message=DOWNLOADED_REMOTE_SSH_CONFIGURATION)

            if self.__remote_ssh_configuration != b"": 
                if HelperFunctions.rotate_files(file_to_be_rotated_filepath=self.__remote_ssh_configuration_file_path,
                                                data_to_be_written_in_newfile=self.__remote_ssh_configuration,
                                                logger_object=self.__logger) == True:

                    if HelperFunctions.set_executable_permission_to_file(path_to_file=self.__remote_ssh_configuration_file_path, 
                                                                            logger_object=self.__logger) == True:

                        if self.__stop_ssh_process() == True:
                            self.__logger.info("Existing Remotes SSH configuration process killed successfully")

                            if self.__apply_remote_ssh_configuration() == True:
                                self._response_manager.send_response(message=self._message_dictionary, 
                                                                        status_code=MessageCodeDefinitions.SUCCESSFULLY_APPLIED_CONFIGURATION_DATA,
                                                                        status_message=SUCCESSFULLY_APPLIED_REMOTE_SSH_CONFIGURATION)

                                self.__logger.info("Successfully applied Remote SSH configuraton")
                                return True
                            else:
                                self.__logger.error("Failed to apply Remote SSH configuration settings")
                                self._response_manager.send_response(message=self._message_dictionary, 
                                                                        status_code=MessageCodeDefinitions.FAILED_TO_APPLY_CONFIGURATION_DATA,
                                                                        status_message=FAILED_TO_APPLY_REMOTE_SSH_CONFIGURATION)
                                return False
                        else:
                            self.__logger.error("Failed to kill existing SSH configuration") 
                            return False
                    else:
                        self.__logger.error("Unable to set executable permission to remote_ssh_configuration.sh")
                else:
                    self.__logger.error("Failed to apply Remote SSH configuration")                
                    return False
            else:
                self.__logger.error("Empty Remote SSH configuration data received")
                self._response_manager.send_response(message=self._message_dictionary, 
                                                        status_code=MessageCodeDefinitions.EMPTY_CONFIGURATION_DATA,
                                                        status_message=EMPTY_REMOTE_SSH_CONFIGURATION_DATA)
                return False
        else:
            return False  
 

    def __create_share_new_ssh_key_routine(self):
        self.__logger.info("Create and share the new SSH key event routine start")
        self._response_manager.send_response(message=self._message_dictionary,
                                            status_code=MessageCodeDefinitions.RECEIVED_NOTIFICATION_TO_SHARE_SSH_PUBLIC_KEY,
                                            status_message=RECEIVED_NOTIFICATION_TO_SHARE_SSH_PUBLIC_KEY)
        
        if self.__create_new_ssh_key() == True:
            fetch_ssh_public_key_status, ssh_public_key_information = self.__fetch_ssh_public_key_information() 
            
            if fetch_ssh_public_key_status == True:
                                
                try:
                    destination_endpoint = self._message_dictionary[MessageDefinitions.CONTENT_KEY][MessageDefinitions.ENDPOINT_KEY]
                except Exception as exception:
                    self.__logger.debug(exception)

                ssh_key_information_message = dict()
                ssh_key_information_message["ssh_key"] = ssh_public_key_information

                put_data_status = self._data_manager.put_data(ssh_key_information_message, destination_endpoint)
                    

                if put_data_status == True:
                    self._response_manager.send_response(message=self._message_dictionary,
                                                       status_code=MessageCodeDefinitions.SUCCESSFULLY_SHARED_SSH_PUBLIC_KEY,
                                                       status_message=SUCCESSFULY_SHARED_SSH_PUBLIC_KEY)
                    return True
                else:
                    self._response_manager.send_response(message=self._message_dictionary,
                                                        status_code=MessageCodeDefinitions.FAILED_TO_SHARE_SSH_PUBLIC_KEY,
                                                        status_message=FAILED_TO_SHARE_SSH_PUBLIC_KEY)
                    return False 
            else:
                self.__logger.info("Failed to fetch Remote SSH Public key")
                return False  
        else:
            self.__logger.info("Failed to create Remote SSH New key")
            return False   


    def __fetch_ssh_public_key_information(self):
        fetch_ssh_public_key_status = False
        ssh_public_key_information = ""

        if os.path.exists(SSH_PUBLIC_KEY_FILE_PATH) == True:
            if os.path.isfile(SSH_PUBLIC_KEY_FILE_PATH) == True:
                try:
                    with open(SSH_PUBLIC_KEY_FILE_PATH, SystemDefinitions.FILE_READ_MODE) as ssh_pub_key_file:
                        ssh_public_key_information = ssh_pub_key_file.read()
                except Exception as exception:
                    self.__logger.error(exception)
                    return ssh_public_key_information, fetch_ssh_public_key_status
                
                fetch_ssh_public_key_status = True

        self.__logger.info("Successfully fetched the ssh public key")
        return fetch_ssh_public_key_status, ssh_public_key_information


    def __create_new_ssh_key(self):
        create_new_ssh_key_command = ECHO_COMMAND + SPACE_CHARACTER + OVERWRITE_FILE_YES_OPTION \
                                     + SPACE_CHARACTER + PIPE_SYMBOL + SPACE_CHARACTER \
                                     + SSH_KEYGEN_COMAMND + SPACE_CHARACTER + EXISTING_PASSPHRASE_OPTION + SPACE_CHARACTER \
                                     + EXISTING_PASSPHRASE + SPACE_CHARACTER + NEW_PASSPHRASE_OPTION + SPACE_CHARACTER \
                                     + NEW_PASSPHRASE + SPACE_CHARACTER + SSH_KEY_FILE_OPTION + SPACE_CHARACTER + SSH_PRIVATE_KEY_FILE_PATH

        # command => echo y | ssh-keygen -t rsa -P "" -N "" -f "/home/chiefnet/.ssh/id_rsa"

        if LinuxHelperFunctions.execute_linux_command(command=create_new_ssh_key_command, logger_object=self.__logger) == False:
            self.__logger.info("Failed to create new ssh key")
            return False

        self.__logger.info("SSH key created successfully")
        return True


    def __apply_remote_ssh_configuration(self):
        if os.path.exists(self.__remote_ssh_configuration_file_path):

            try:
                # For the SSH process the standard out of the SSH is not needed. So the capture ouput of the subprocess.run function made False
                result = subprocess.run(self.__remote_ssh_configuration_file_path, capture_output=False)

            except Exception as exception:
                self.__logger.error(exception)
                return False

        self.__logger.info("Successfully applied remote SSH configuration")
        return True


    def __stop_ssh_process(self):
        ssh_pid_list = LinuxHelperFunctions.get_pid(process_name=SSH_COMMAND_NAME, logger_object=self.__logger)
        try:
            for ssh_pid in ssh_pid_list:
                kill_ssh_pid_command = KILL_COMMAND + SPACE_CHARACTER + SIGKILL_OPTION + SPACE_CHARACTER + str(ssh_pid)

                if LinuxHelperFunctions.execute_linux_command(command=kill_ssh_pid_command, logger_object=self.__logger) == False:
                    return False

        except Exception as exceptions:
            return False
        
        self.__logger.info("Successfully killed existing Remote SSH process")
        return True