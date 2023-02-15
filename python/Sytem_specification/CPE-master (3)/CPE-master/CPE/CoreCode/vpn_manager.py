import os

import CoreCode.logger as Logger
import Definitions.system_definitions as SystemDefinitions
import Definitions.message_code_definitions as MessageCodeDefinitions

from CoreCode.service_manager import ServiceManager
import CoreCode.service_manager_helper_functions as HelperFunctions
import CoreCode.service_manager_linux_helper_functions as LinuxHelperFunctions

PATH_SEPERATOR_CHARACTER = os.path.sep

OPENVPN_SERVICE_NAME = "openvpn.service"
FRR_SERVICE_NAME = "frr.service"
SHELL_FILE_EXTENSION = ".sh"

VPN_ROUTING_CONFIG_FOLDER_NAME = "vpn-configuration"
VPN_ROUTING_CONFIG_FILENAME = VPN_ROUTING_CONFIG_FOLDER_NAME + ".zip"

ETC_DIRECTORY_NAME = "etc"
OPENVPN_CONFIG_FOLDER_NAME = "openvpn"
OPENVPN_UP_SCRIPT_FILE_NAME = "vpn-up.sh"
OPENVPN_DOWN_SCRIPT_FILE_NAME = "vpn-down.sh"
OPENVPN_CLIENT_CONFIG_FILE_SUFFIX_STRING = "-ovpn.conf"
FRR_CONFIG_FOLDER_NAME = "frr"
OPENVPN_SERVER_BRIDGE_UP_SCRIPT_FILE_NAME = "eth_br_up.sh"
OPENVPN_SERVER_BRIDGE_DOWN_SCRIPT_FILE_NAME = "eth_br_down.sh"
OPENVPN_SERVER_UP_SCRIPT_FILE_SUFFIX_STRING = "-server-up.sh"
OPENVPN_SERVER_DOWN_SCRIPT_FILE_SUFFIX_STRING = "-server-down.sh"
OPENVPN_SERVER_CONFIG_FILE_SUFFIX_STRING = "-server.conf"
PKI_CERTIFICATE_DIRECTORY_SUFFIX_STRING = "-pki"

FRR_OWNERSHIP_NAME = "frr"

OPENVPN_CONFIG_FILE_LOCATION = PATH_SEPERATOR_CHARACTER + ETC_DIRECTORY_NAME + PATH_SEPERATOR_CHARACTER + OPENVPN_CONFIG_FOLDER_NAME
FRR_CONFIG_FILE_LOCATION = PATH_SEPERATOR_CHARACTER + ETC_DIRECTORY_NAME + PATH_SEPERATOR_CHARACTER + FRR_CONFIG_FOLDER_NAME

OPENVPN_UP_SCRIPT_FILE_PATH = OPENVPN_CONFIG_FILE_LOCATION + PATH_SEPERATOR_CHARACTER + OPENVPN_UP_SCRIPT_FILE_NAME
OPENVPN_DOWN_SCRIPT_FILE_PATH = OPENVPN_CONFIG_FILE_LOCATION + PATH_SEPERATOR_CHARACTER + OPENVPN_DOWN_SCRIPT_FILE_NAME

OPENVPN_SERVER_BRIDGE_UP_SCRIPT_FILE_PATH = OPENVPN_CONFIG_FILE_LOCATION + PATH_SEPERATOR_CHARACTER + OPENVPN_SERVER_BRIDGE_UP_SCRIPT_FILE_NAME
OPENVPN_SERVER_BRIDGE_DOWN_SCRIPT_FILE_PATH = OPENVPN_CONFIG_FILE_LOCATION + PATH_SEPERATOR_CHARACTER + OPENVPN_SERVER_BRIDGE_DOWN_SCRIPT_FILE_NAME
OPENVPN_SERVER_UP_SCRIPT_FILE_PATH = OPENVPN_CONFIG_FILE_LOCATION + PATH_SEPERATOR_CHARACTER + OPENVPN_SERVER_UP_SCRIPT_FILE_SUFFIX_STRING
OPENVPN_SERVER_DOWN_SCRIPT_FILE_PATH = OPENVPN_CONFIG_FILE_LOCATION + PATH_SEPERATOR_CHARACTER + OPENVPN_SERVER_DOWN_SCRIPT_FILE_SUFFIX_STRING

SUCCESSFULLY_UPDATED_OPENVPN_AND_FRR_CONFIGURATION = "Successfully updated OpenVPN and FRR configuration"
SUCCESSFULLY_EMPTIED_OPENVPN_AND_FRR_CONFIGURATION = "Successfully emptied OpenVPN and FRR configuration"

RECEIVED_UPDATE_OPENVPN_AND_FRR_CONFIGURATION_NOTIFICATION = "OpenVPN and FRR configuration update notification received"
RECEIVED_STOP_OPENVPN_AND_FRR_SERVICE_NOTIFICATION = "Stop OpenVPN and FRR service notification received"
DOWNLOADED_OPENVPN_AND_FRR_CONFIGURATION = "Successfully downloaded OpenVPN and FRR configuration"

EMPTY_OPENVPN_AND_FRR_CONFIGURATION_DATA = "Empty OpenVPN and FRR configuration data received"
FAILED_TO_APPLY_OPENVPN_AND_FRR_CONFIGURATION = "Failed to apply OpenVPN and FRR configuration"


class VPNManager(ServiceManager):
    """
    VPNManager is derived from ServiceManager and is used to handle operations with respect to VPN and its routing on the CPE side
    Arguments:
    data_manager:
        An instance of DataManager must be passed. This instance is used to fetch the dnsmasq configuration files from the endpoint 
    response_manager:
        An instance of ResponseManager must be passed to send responses to the WebApp
    """

    def __init__(self, data_manager, response_manager):
        self.__logger = Logger.get_logger(__name__)
        self.__logger.info("VPNManager initializer starts")

        self.__vpn_configuration_filepath = SystemDefinitions.USER_CONFIG_FILE_PATH + PATH_SEPERATOR_CHARACTER + VPN_ROUTING_CONFIG_FILENAME

        self.__temp_vpn_configuration_filepath = SystemDefinitions.TEMP_USER_CONFIG_FILE_PATH + PATH_SEPERATOR_CHARACTER + VPN_ROUTING_CONFIG_FOLDER_NAME
        self.__temp_openvpn_configuration_filepath = self.__temp_vpn_configuration_filepath + PATH_SEPERATOR_CHARACTER + OPENVPN_CONFIG_FOLDER_NAME
        self.__temp_frr_configuration_filepath = self.__temp_vpn_configuration_filepath + PATH_SEPERATOR_CHARACTER + FRR_CONFIG_FOLDER_NAME

        # insert event codes and corresponding routines into this dictionary
        event_dictionary = {}
        event_dictionary[MessageCodeDefinitions.UPDATE_OPENVPN_AND_FRR_CONFIGURATION_EVENT] = self._update_openvpn_and_frr_configuration_event_routine
        event_dictionary[MessageCodeDefinitions.STOP_OPENVPN_AND_FRR_SERVICE_EVENT] = self._stop_openvpn_and_frr_service_event_routine

        ServiceManager.__init__(self, data_manager=data_manager, response_manager=response_manager, event_dictionary=event_dictionary)
        self.__logger.info("VPNManager initializer ends")


    def _update_openvpn_and_frr_configuration_event_routine(self):
        self.__logger.info("Update OpenVPN and FRR configuration event routine start")
        self._response_manager.send_response(message=self._message_dictionary,
                                             status_code=MessageCodeDefinitions.RECEIVED_CONFIGURATION_UPDATE_NOTIFICATION,
                                             status_message=RECEIVED_UPDATE_OPENVPN_AND_FRR_CONFIGURATION_NOTIFICATION)

        fetch_vpn_configuration_status, self.__vpn_configuration = self._fetch_configuration_from_endpoint()

        if fetch_vpn_configuration_status == True:
            self._response_manager.send_response(message=self._message_dictionary,
                                                 status_code=MessageCodeDefinitions.DOWNLOADED_CONFIGURATION_FILE,
                                                 status_message=DOWNLOADED_OPENVPN_AND_FRR_CONFIGURATION)

            if self.__vpn_configuration != b"":
                if HelperFunctions.rotate_files(file_to_be_rotated_filepath=self.__vpn_configuration_filepath,
                                                data_to_be_written_in_newfile=self.__vpn_configuration,
                                                logger_object=self.__logger) == True:

                    if self.__apply_update_vpn_configuration() == True:
                        self.__logger.info(SUCCESSFULLY_UPDATED_OPENVPN_AND_FRR_CONFIGURATION)
                        self._response_manager.send_response(message=self._message_dictionary,
                                                             status_code=MessageCodeDefinitions.SUCCESSFULLY_APPLIED_CONFIGURATION_DATA,
                                                             status_message=SUCCESSFULLY_UPDATED_OPENVPN_AND_FRR_CONFIGURATION)
                        return True
                    else:
                        self.__logger.error("Failed to apply openvpn and frr configuration")
                        self._response_manager.send_response(message=self._message_dictionary,
                                                             status_code=MessageCodeDefinitions.FAILED_TO_APPLY_CONFIGURATION_DATA,
                                                             status_message=FAILED_TO_APPLY_OPENVPN_AND_FRR_CONFIGURATION)
                        return False
                else:
                    self.__logger.error("Failed to rotate OpenVPN and Frr configuration")
                    return False
            else:
                self.__logger.error("Empty OpenVPN and Frr configuration received")
                self._response_manager.send_response(message=self._message_dictionary,
                                                     status_code=MessageCodeDefinitions.EMPTY_CONFIGURATION_DATA,
                                                     status_message=EMPTY_OPENVPN_AND_FRR_CONFIGURATION_DATA)
                return False
        else:
            return False


    def __stop_openvpn_and_frr_system_service(self):
        # Stop and disable Open VPN and Frr System services
        if LinuxHelperFunctions.stop_system_service(service_name=OPENVPN_SERVICE_NAME, logger_object=self.__logger) != True:
            return False

        self.__logger.info("OpenVPN Service Stoped successfully to update changes")

        if LinuxHelperFunctions.stop_system_service(service_name=FRR_SERVICE_NAME, logger_object=self.__logger) != True:
            return False

        self.__logger.info("FRR Service Stoped successfully to update changes")

        if LinuxHelperFunctions.disable_system_service(service_name=OPENVPN_SERVICE_NAME, logger_object=self.__logger) != True:
            return False

        self.__logger.info("OpenVPN Service disabled successfully to update changes")

        if LinuxHelperFunctions.disable_system_service(service_name=FRR_SERVICE_NAME, logger_object=self.__logger) != True:
            return False

        self.__logger.info("FRR Service disabled successfully to update changes")

        return True


    def __start_openvpn_and_frr_system_service(self):
        # Enable and start OpenVPN and Frr System services
        if LinuxHelperFunctions.enable_system_service(service_name=OPENVPN_SERVICE_NAME, logger_object=self.__logger) != True:
            return False

        self.__logger.info("OpenVPN Service enabled successfully after updated the changes")

        if LinuxHelperFunctions.enable_system_service(service_name=FRR_SERVICE_NAME, logger_object=self.__logger) != True:
            return False

        self.__logger.info("FRR Service enabled successfully after updated the changes")

        if LinuxHelperFunctions.start_system_service(service_name=OPENVPN_SERVICE_NAME, logger_object=self.__logger) != True:
            return False

        self.__logger.info("OpenVPN Service Start successfully after updated the changes")

        if LinuxHelperFunctions.start_system_service(service_name=FRR_SERVICE_NAME, logger_object=self.__logger) != True:
            return False

        self.__logger.info("FRR Service Start successfully after updated the changes")

        return True


    def __remove_existing_openvpn_client_and_frr_system_config_files(self):

        # Delete vpn-up.sh, vpn-down.sh, all xxx-ovpn.conf configuration files in /etc/openvpn
        try:
            if os.path.exists(OPENVPN_UP_SCRIPT_FILE_PATH) == True:
                os.remove(OPENVPN_UP_SCRIPT_FILE_PATH)

            if os.path.exists(OPENVPN_DOWN_SCRIPT_FILE_PATH) == True:
                os.remove(OPENVPN_DOWN_SCRIPT_FILE_PATH)

            for openvpn_config_filename in os.listdir(OPENVPN_CONFIG_FILE_LOCATION):
                if OPENVPN_CLIENT_CONFIG_FILE_SUFFIX_STRING in openvpn_config_filename:
                    openvpn_config_filepath = OPENVPN_CONFIG_FILE_LOCATION + PATH_SEPERATOR_CHARACTER + str(openvpn_config_filename)
                    os.remove(openvpn_config_filepath)
        except Exception as exception:
            self.__logger.error(exception)
            return False

        # Delete all files in /etc/frr
        try:
            for frr_config_filename in os.listdir(FRR_CONFIG_FILE_LOCATION):
                frr_config_filepath = FRR_CONFIG_FILE_LOCATION + PATH_SEPERATOR_CHARACTER + str(frr_config_filename)
                if os.path.isfile(frr_config_filepath) == True:
                    os.remove(frr_config_filepath)
        except Exception as exception:
            self.__logger.error(exception)
            return False

        return True


    def __apply_update_vpn_configuration(self):
        self.__logger.info("Apply update vpn configuration starts")

        if HelperFunctions.extract_files_to_directory(zip_compressed_filepath=self.__vpn_configuration_filepath,
                                                      extract_destination_directory_path=self.__temp_vpn_configuration_filepath,
                                                      logger_object=self.__logger) != True:
            return False

        self.__logger.info("Successfuly extracted {} files to directory {}".format(self.__vpn_configuration_filepath, self.__temp_vpn_configuration_filepath))

        if os.path.exists(path=self.__temp_openvpn_configuration_filepath):
            openvpn_config_file_list = os.listdir(self.__temp_openvpn_configuration_filepath)

            if len(openvpn_config_file_list) == 0:
                self.__logger.error("Received empty OpenVPN directory")
                return False

        else:
            self.__logger.error("OpenVPN directory is not received")
            return False

        self.__logger.info("{} file exist".format(self.__temp_openvpn_configuration_filepath))

        if os.path.exists(path=self.__temp_frr_configuration_filepath):
            frr_config_file_list = os.listdir(self.__temp_frr_configuration_filepath)

            if len(frr_config_file_list) == 0:
                self.__logger.error("Received empty Frr directory")
                return False
            
        else:
            self.__logger.error("Frr directory is not received")
            return False
        
        self.__logger.info("{} file exist".format(self.__temp_frr_configuration_filepath))


        if os.path.exists(path=OPENVPN_SERVER_BRIDGE_DOWN_SCRIPT_FILE_PATH):
            if LinuxHelperFunctions.execute_script(filepath=OPENVPN_SERVER_BRIDGE_DOWN_SCRIPT_FILE_PATH, logger_object=self.__logger) != True:
                return False

        if self.__stop_openvpn_and_frr_system_service() != True:
            return False

        self.__logger.info("Successfuly stoped and disabled openvpn and Frr configuration")

        if self.__remove_existing_openvpn_client_and_frr_system_config_files() != True:
            return False

        if self.__remove_existing_openvpn_server_config_files() != True:
            return False

        self.__logger.info("Successfuly removed existing openvpn and Frr configuration")

        if HelperFunctions.move_files_in_directory(source_directory_path=self.__temp_openvpn_configuration_filepath,
                                                   destination_directory_path=OPENVPN_CONFIG_FILE_LOCATION,
                                                   logger_object=self.__logger) != True:
            return False

        self.__logger.info("Successfuly moved from {} to {}".format(self.__temp_openvpn_configuration_filepath, OPENVPN_CONFIG_FILE_LOCATION))

        for openvpn_config_filename in os.listdir(OPENVPN_CONFIG_FILE_LOCATION):

            if SHELL_FILE_EXTENSION in openvpn_config_filename:
                openvpn_shell_filepath = OPENVPN_CONFIG_FILE_LOCATION + PATH_SEPERATOR_CHARACTER + str(openvpn_config_filename)

                if HelperFunctions.set_executable_permission_to_file(path_to_file=openvpn_shell_filepath ,logger_object=self.__logger) != True:
                    return False

                self.__logger.info("Successfuly set file permisison for {}".format(openvpn_shell_filepath ))

        if LinuxHelperFunctions.execute_script(filepath=OPENVPN_SERVER_BRIDGE_UP_SCRIPT_FILE_PATH, logger_object=self.__logger) != True:
            return False

        self.__logger.info("{} file is Successfuly Executed".format(OPENVPN_SERVER_BRIDGE_UP_SCRIPT_FILE_PATH))

        if HelperFunctions.move_files_in_directory(source_directory_path=self.__temp_frr_configuration_filepath,
                                                   destination_directory_path=FRR_CONFIG_FILE_LOCATION,
                                                   logger_object=self.__logger) != True:
            return False

        self.__logger.info("Successfuly moved from {} to {}".format(self.__temp_frr_configuration_filepath, FRR_CONFIG_FILE_LOCATION))

        if LinuxHelperFunctions.change_directory_and_its_files_ownership(user_name=FRR_OWNERSHIP_NAME,
                                                                         group_name=FRR_OWNERSHIP_NAME,
                                                                         directory_path=FRR_CONFIG_FILE_LOCATION, logger_object=self.__logger) != True:
            return False

        self.__logger.info("Succesfully change the ownership of {}".format(FRR_CONFIG_FILE_LOCATION))

        if self.__start_openvpn_and_frr_system_service() != True:
            return False

        self.__logger.info("Successfuly started and enabled openvpn and Frr configuration")

        return True


    def _stop_openvpn_and_frr_service_event_routine(self):
        self.__logger.info(RECEIVED_STOP_OPENVPN_AND_FRR_SERVICE_NOTIFICATION)
        self._response_manager.send_response(message=self._message_dictionary,
                                             status_code=MessageCodeDefinitions.RECEIVED_CONFIGURATION_UPDATE_NOTIFICATION,
                                             status_message=RECEIVED_STOP_OPENVPN_AND_FRR_SERVICE_NOTIFICATION)        
        
        for openvpn_config_filename in os.listdir(OPENVPN_CONFIG_FILE_LOCATION):
            if OPENVPN_SERVER_BRIDGE_DOWN_SCRIPT_FILE_NAME in openvpn_config_filename:
                openvpn_down_script_filepath = OPENVPN_CONFIG_FILE_LOCATION + PATH_SEPERATOR_CHARACTER + str(openvpn_config_filename)
                if LinuxHelperFunctions.execute_script(filepath=openvpn_down_script_filepath, logger_object=self.__logger) != True:
                    return False

        if self.__stop_openvpn_and_frr_system_service() != True:
            self._response_manager.send_response(message=self._message_dictionary,
                                                 status_code=MessageCodeDefinitions.FAILED_TO_APPLY_CONFIGURATION_DATA,
                                                 status_message=MessageCodeDefinitions.FAILED_TO_APPLY_CONFIGURATION_DATA)
            return False

        self.__logger.info("Successfuly stoped and disabled openvpn and Frr configuration")

        if self.__remove_existing_openvpn_client_and_frr_system_config_files() != True:
            self._response_manager.send_response(message=self._message_dictionary,
                                                 status_code=MessageCodeDefinitions.FAILED_TO_APPLY_CONFIGURATION_DATA,
                                                 status_message=MessageCodeDefinitions.FAILED_TO_APPLY_CONFIGURATION_DATA)
            return False

        if self.__remove_existing_openvpn_server_config_files() != True:
            self._response_manager.send_response(message=self._message_dictionary,
                                                 status_code=MessageCodeDefinitions.FAILED_TO_APPLY_CONFIGURATION_DATA,
                                                 status_message=MessageCodeDefinitions.FAILED_TO_APPLY_CONFIGURATION_DATA)
            return False

        self.__logger.info("Successfuly removed existing openvpn and Frr configuration")
        self.__logger.info(SUCCESSFULLY_EMPTIED_OPENVPN_AND_FRR_CONFIGURATION)

        self._response_manager.send_response(message=self._message_dictionary,
                                             status_code=MessageCodeDefinitions.SUCCESSFULLY_APPLIED_CONFIGURATION_DATA,
                                             status_message=SUCCESSFULLY_EMPTIED_OPENVPN_AND_FRR_CONFIGURATION)

        return True


    def __remove_existing_openvpn_server_config_files(self):

        # Delete eth_br_start.sh, eth_br_stop.sh, all xxx-server-up.sh, xxx-server-down.sh, xxx-server.conf configuration files in /etc/openvpn
        try:
            if os.path.exists(OPENVPN_SERVER_BRIDGE_UP_SCRIPT_FILE_PATH) == True:
                os.remove(OPENVPN_SERVER_BRIDGE_UP_SCRIPT_FILE_PATH)

            if os.path.exists(OPENVPN_SERVER_BRIDGE_DOWN_SCRIPT_FILE_PATH) == True:
                os.remove(OPENVPN_SERVER_BRIDGE_DOWN_SCRIPT_FILE_PATH)

            for filename in os.listdir(OPENVPN_CONFIG_FILE_LOCATION):
                if OPENVPN_SERVER_UP_SCRIPT_FILE_SUFFIX_STRING in filename:
                    filepath = OPENVPN_CONFIG_FILE_LOCATION + PATH_SEPERATOR_CHARACTER + str(filename)
                    os.remove(filepath)

                if OPENVPN_SERVER_DOWN_SCRIPT_FILE_SUFFIX_STRING in filename:
                    filepath = OPENVPN_CONFIG_FILE_LOCATION + PATH_SEPERATOR_CHARACTER + str(filename)
                    os.remove(filepath)

                if OPENVPN_SERVER_CONFIG_FILE_SUFFIX_STRING in filename:
                    filepath = OPENVPN_CONFIG_FILE_LOCATION + PATH_SEPERATOR_CHARACTER + str(filename)
                    os.remove(filepath)

                if PKI_CERTIFICATE_DIRECTORY_SUFFIX_STRING in filename:
                    filepath = OPENVPN_CONFIG_FILE_LOCATION + PATH_SEPERATOR_CHARACTER + str(filename)
                    if HelperFunctions.remove_directory(directory_to_be_removed=filepath, logger_object=self.__logger) != True:
                        return False

        except Exception as exception:
            self.__logger.error(exception)
            return False

        return True
