import os
import subprocess

import CoreCode.logger as Logger
import Definitions.system_definitions as SystemDefinitions
import Definitions.message_definitions as MessageDefinitions
import Definitions.message_code_definitions as MessageCodeDefinitions

from CoreCode.service_manager import ServiceManager
import CoreCode.service_manager_helper_functions as HelperFunctions

PATH_SEPERATOR_CHARACTER = os.path.sep
SPACE_CHARACTER = " "

SYSTEMCTL_COMMAND_PREFIX = "systemctl"
SYSTEMCTL_RESTART_OPTION = "restart"

SPLIT_DNS_CONFIG_FILENAME = "split-dns.conf"
DNSMASQ_SERVICE_NAME = "dnsmasq.service"
DNSMASQ_CONFIG_FILENAME = "dnsmasq-configuration.zip"
ETC_DIRECTORY_NAME = "etc"
DNSMASQ_CONFIG_FOLDER_NAME = "dnsmasq.d"
DNSMASQ_CONFIG_FILE_LOCATION = PATH_SEPERATOR_CHARACTER + ETC_DIRECTORY_NAME + PATH_SEPERATOR_CHARACTER + DNSMASQ_CONFIG_FOLDER_NAME

IPSET_DOMAIN_CONFIG_FILE_NAME = "ipset-domain.conf"

SUCCESSFULLY_APPLIED_DHCP_SERVER_CONFIGURATION = "Successfully applied DHCP server configuration"
RECEIVED_DHCP_SERVER_CONFIGURATION_UPDATE_NOTIFICATION = "Received DHCP server configuration update notification"
DOWNLOADED_DHCP_SERVER_CONFIGURATION = "Successfully downloaded DHCP server configuration"

EMPTY_DNSMASQ_CONFIGURATION_DATA = "Empty dnsmasq configuration data received"
FAILED_TO_APPLY_DNSMASQ_CONFIGURATION = "Failed to apply dnsmasq configuration"


class DHCPManager(ServiceManager):
    """
    DHCPManager is derived from ServiceManager and is used to handle operations with respect to DHCP on the CPE side
    Arguments:
    data_manager:
        An instance of DataManager must be passed. This instance is used to fetch the dnsmasq configuration files from the endpoint 
    response_manager:
        An instance of ResponseManager must be passed to send responses to the WebApp
    """

    def __init__(self, data_manager, response_manager):
        self.__logger = Logger.get_logger(__name__)
        self.__logger.info("DHCPManager initializer starts")

        self.__dhcpserver_configuration_filepath = SystemDefinitions.USER_CONFIG_FILE_PATH + PATH_SEPERATOR_CHARACTER + DNSMASQ_CONFIG_FILENAME
        self.__temp_dhcpserver_configuration_filepath = SystemDefinitions.TEMP_USER_CONFIG_FILE_PATH + PATH_SEPERATOR_CHARACTER + DNSMASQ_CONFIG_FOLDER_NAME

        self.__dnsmasq_restart_command = SYSTEMCTL_COMMAND_PREFIX + SPACE_CHARACTER \
                                            + SYSTEMCTL_RESTART_OPTION + SPACE_CHARACTER + DNSMASQ_SERVICE_NAME

        # insert event codes and corresponding routines into this dictionary
        event_dictionary = {}
        event_dictionary[MessageCodeDefinitions.DHCP_SERVER_CONFIGURATION_UPDATE_EVENT] = self.__dhcpserver_configuration_update_event_routine

        ServiceManager.__init__(self, data_manager=data_manager, response_manager=response_manager, event_dictionary=event_dictionary)
        self.__logger.info("DHCPManager initializer ends")


    def __dhcpserver_configuration_update_event_routine(self):
        self.__logger.info("DHCP server configuration update event routine start")
        self._response_manager.send_response(message=self._message_dictionary, 
                                                status_code=MessageCodeDefinitions.RECEIVED_CONFIGURATION_UPDATE_NOTIFICATION,
                                                status_message=RECEIVED_DHCP_SERVER_CONFIGURATION_UPDATE_NOTIFICATION)
        
        fetch_dhcp_server_configuration_status, self.__dhcp_server_configuration = self._fetch_configuration_from_endpoint()
        
        if fetch_dhcp_server_configuration_status == True:
            self._response_manager.send_response(message=self._message_dictionary, 
                                                    status_code=MessageCodeDefinitions.DOWNLOADED_CONFIGURATION_FILE,
                                                    status_message=DOWNLOADED_DHCP_SERVER_CONFIGURATION)

            if self.__dhcp_server_configuration != b"": 
                if HelperFunctions.rotate_files(file_to_be_rotated_filepath=self.__dhcpserver_configuration_filepath,
                                                    data_to_be_written_in_newfile=self.__dhcp_server_configuration,
                                                    logger_object=self.__logger) == True:
                    if self.__apply_dhcpserver_configuration() == True:
                        self._response_manager.send_response(message=self._message_dictionary, 
                                                                status_code=MessageCodeDefinitions.SUCCESSFULLY_APPLIED_CONFIGURATION_DATA,
                                                                status_message=SUCCESSFULLY_APPLIED_DHCP_SERVER_CONFIGURATION)
                        return True
                    else:
                        self.__logger.error("Failed to apply dnsmasq configuration")
                        self._response_manager.send_response(message=self._message_dictionary, 
                                                                status_code=MessageCodeDefinitions.FAILED_TO_APPLY_CONFIGURATION_DATA,
                                                                status_message=FAILED_TO_APPLY_DNSMASQ_CONFIGURATION)
                        return False
                else:
                    self.__logger.error("Failed to rotate DHCP server configuration")                
                    return False
            else:
                self.__logger.error("Empty dnsmasq configuration data received")
                self._response_manager.send_response(message=self._message_dictionary, 
                                                        status_code=MessageCodeDefinitions.EMPTY_CONFIGURATION_DATA,
                                                        status_message=EMPTY_DNSMASQ_CONFIGURATION_DATA)
                return False
        else:
            return False   
    

    def __apply_dhcpserver_configuration(self):
        self.__logger.info("Apply dnsmasq configuration")

        if HelperFunctions.extract_files_to_directory(zip_compressed_filepath=self.__dhcpserver_configuration_filepath, 
                                                        extract_destination_directory_path=self.__temp_dhcpserver_configuration_filepath, 
                                                        logger_object=self.__logger) != True:
            return False
        
        # Clearing only all DHCP server related configuration files in /etc/dnsmasq.d 
        try:
            for filename in os.listdir(DNSMASQ_CONFIG_FILE_LOCATION):
                if str(filename) != str(SPLIT_DNS_CONFIG_FILENAME) and str(filename) != str(IPSET_DOMAIN_CONFIG_FILE_NAME):
                    filepath = DNSMASQ_CONFIG_FILE_LOCATION + PATH_SEPERATOR_CHARACTER + str(filename)
                    os.remove(filepath)
        except Exception as exception:
            self.__logger.error(exception)
            return False
        
        if HelperFunctions.move_files_in_directory(source_directory_path=self.__temp_dhcpserver_configuration_filepath, 
                                                    destination_directory_path=DNSMASQ_CONFIG_FILE_LOCATION, 
                                                    logger_object=self.__logger) != True:
            return False

        try:
            self.__logger.info("Restarting dnsmasq service to apply dnsmasq configuration changes")
            dnsmasq_restart_status = subprocess.run(self.__dnsmasq_restart_command, shell=True, capture_output=True, text=True)            
            self.__logger.info(dnsmasq_restart_status.stdout)
            self.__logger.debug(dnsmasq_restart_status.stderr)

            if dnsmasq_restart_status.returncode != 0:
                return False
                
        except Exception as exception:
            self.__logger.error(exception)
            return False
        
        return True
