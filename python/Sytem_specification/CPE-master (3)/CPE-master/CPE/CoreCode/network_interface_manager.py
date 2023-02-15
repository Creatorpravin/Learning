import os
import subprocess
import json
import time

import CoreCode.logger as Logger
import Definitions.system_definitions as SystemDefinitions
import Definitions.message_definitions as MessageDefinitions
import Definitions.message_code_definitions as MessageCodeDefinitions

from CoreCode.service_manager import ServiceManager
import CoreCode.service_manager_helper_functions as HelperFunctions

PATH_SEPERATOR_CHARACTER = os.path.sep
NETPLAN_CONFIG_FILE_NAME = "network-interface-configuration.zip"
ADMINISTRATIVE_STATUS_SCRIPT_FILENAME = "administrative-status.sh"
CUSTOM_ROUTING_SCRIPT_FILENAME = "chiefnet-custom-route-script.sh"
ETC_DIRECTORY_NAME = "etc"
NETPLAN_CONFIG_FOLDER_NAME = "netplan"
NETPLAN_CONFIG_FILE_LOCATION = PATH_SEPERATOR_CHARACTER + ETC_DIRECTORY_NAME + PATH_SEPERATOR_CHARACTER + NETPLAN_CONFIG_FOLDER_NAME

IP_COMMAND_PREFIX = "ip"
IP_COMMAND_STATS_OPTION = "-s"
IP_COMMAND_JSON_OPTION = "-json"
IP_COMMAND_ALL_OPTION = "-a"
IP_COMMAND_SHOW_ADDRESS_OPTION = "address show"
SPACE_CHARACTER = " "

NETPLAN_COMMAND_PREFIX = "netplan"
NETPLAN_DEBUG_OPTION = "--debug"
NETPLAN_GENERATE_SUFFIX = "generate"
NETPLAN_APPLY_SUFFIX = "apply"

SUCCESSFULY_SHARED_NETWORK_INTERFACE_INFO = "Successfully shared network interface information"
RECEIVED_NOTIFICATION_TO_SHARE_INTERFACE_INFO = "Received notification to share Network Interface information"
UNABLE_TO_GET_INTERFACE_INFO = "Unable to get network interface information from the system"
FAILED_TO_SHARE_INTERFACE_INFO = "Failed to share network interface information"

RECEIVED_NETWORK_INTERFACE_CONFIGURATION_UPDATE_NOTIFICATION = "Received network interface configuration update"
DOWNLOADED_NETWORK_INTERFACE_CONFIGURATION = "Successfully downloaded network interface configuration"
SUCCESSFULLY_APPLIED_NETWORK_INTERFACE_CONFIGURATION = "Successfully applied network interface configuration"
FAILED_TO_APPLY_NETWORK_INTERFACE_CONFIGURATION = "Failed to apply network interface configuration"
EMPTY_NETWORK_INTERFACE_CONFIGURATION_DATA = "Empty network interface configuration data"


class NetworkInterfaceManager(ServiceManager):
    """
    NetworkInterfaceManager is derived from ServiceManager and is used to execute operations with respect to the network interfaces
    Arguments:
    data_manager:
        An instance of DataManager must be passed. This instance is used to fetch the netplan configuration file from the endpoint
        and also to send the network interface information to the WebApp
    response_manager:
        An instance of ResponseManager must be passed
    """
    def __init__(self, data_manager, response_manager):
        self.__logger = Logger.get_logger(__name__)
        self.__logger.info("NetworkInterfaceManager initializer starts")

        self.__netplan_configuration_filepath = SystemDefinitions.USER_CONFIG_FILE_PATH + PATH_SEPERATOR_CHARACTER + NETPLAN_CONFIG_FILE_NAME
        self.__administrative_status_script_filepath = NETPLAN_CONFIG_FILE_LOCATION + PATH_SEPERATOR_CHARACTER + ADMINISTRATIVE_STATUS_SCRIPT_FILENAME
        self.__custom_routing_script_filepath = NETPLAN_CONFIG_FILE_LOCATION + PATH_SEPERATOR_CHARACTER + CUSTOM_ROUTING_SCRIPT_FILENAME
        self.__temp_netplan_configuration_filepath = SystemDefinitions.TEMP_USER_CONFIG_FILE_PATH + PATH_SEPERATOR_CHARACTER + NETPLAN_CONFIG_FOLDER_NAME

        self.__interface_information_ip_command = IP_COMMAND_PREFIX + SPACE_CHARACTER + \
                                            IP_COMMAND_STATS_OPTION + SPACE_CHARACTER + \
                                            IP_COMMAND_ALL_OPTION + SPACE_CHARACTER + \
                                            IP_COMMAND_JSON_OPTION + SPACE_CHARACTER + \
                                            IP_COMMAND_SHOW_ADDRESS_OPTION

        self.__netplan_generate_command = NETPLAN_COMMAND_PREFIX + SPACE_CHARACTER + NETPLAN_DEBUG_OPTION + SPACE_CHARACTER + NETPLAN_GENERATE_SUFFIX
        self.__netplan_apply_command = NETPLAN_COMMAND_PREFIX + SPACE_CHARACTER + NETPLAN_DEBUG_OPTION + SPACE_CHARACTER + NETPLAN_APPLY_SUFFIX

        # insert event codes and corresponding routines into this dictionary
        event_dictionary = {}
        event_dictionary[MessageCodeDefinitions.SHARE_NETWORK_INTERFACE_INFO_EVENT] =  self.__share_network_interface_information_event_routine
        event_dictionary[MessageCodeDefinitions.NETWORK_INTERFACE_CONFIGURATION_UPDATE_EVENT] =  self.__configuration_update_available_event_routine

        ServiceManager.__init__(self, data_manager=data_manager, response_manager=response_manager, event_dictionary=event_dictionary)
        self.__logger.info("TrafficSteeringManager initializer ends")


    def __share_network_interface_information_event_routine(self):
        self.__logger.info("Share network interface information event routine start")
        self._response_manager.send_response(message=self._message_dictionary,
                                            status_code=MessageCodeDefinitions.RECEIVED_NOTIFICATION_TO_SHARE_INTERFACE_INFORMATION,
                                            status_message=RECEIVED_NOTIFICATION_TO_SHARE_INTERFACE_INFO)

        interface_information_status, interface_information = self.__get_interface_information()

        if interface_information_status == True:

            try:
                destination_endpoint = self._message_dictionary[MessageDefinitions.CONTENT_KEY][MessageDefinitions.ENDPOINT_KEY]
            except Exception as exception:
                self.__logger.error(exception)

            interface_information_message = dict()
            interface_information_message["network_interfaces"] = json.loads(interface_information)

            put_data_status = self._data_manager.put_data(interface_information_message, destination_endpoint)

            if put_data_status == True:
                self._response_manager.send_response(message=self._message_dictionary,
                                                    status_code=MessageCodeDefinitions.SUCCESSFULLY_SHARED_INTERFACE_INFORMATION,
                                                    status_message=SUCCESSFULY_SHARED_NETWORK_INTERFACE_INFO)
                return True
            else:
                self._response_manager.send_response(message=self._message_dictionary,
                                                    status_code=MessageCodeDefinitions.FAILED_TO_SHARE_INTERFACE_INFORMATION,
                                                    status_message=FAILED_TO_SHARE_INTERFACE_INFO)
                return False
        else:
            return False


    def __get_interface_information(self):
        interface_information = ""

        try:
            get_interface_info = subprocess.Popen(self.__interface_information_ip_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            interface_information, ip_command_error_information = get_interface_info.communicate()
            self.__logger.debug(ip_command_error_information)

        except Exception as exception:
            self.__logger.error(exception)
            self._response_manager.send_response(message=self._message_dictionary,
                                                status_code=MessageCodeDefinitions.UNABLE_TO_GET_INTERFACE_INFORMATION_FROM_SYSTEM,
                                                status_message=UNABLE_TO_GET_INTERFACE_INFO)
            return False, interface_information

        return True, interface_information


    def __configuration_update_available_event_routine(self):
        self.__logger.info("Network interface configuration update event routine start")
        self._response_manager.send_response(message=self._message_dictionary,
                                                status_code=MessageCodeDefinitions.RECEIVED_CONFIGURATION_UPDATE_NOTIFICATION,
                                                status_message=RECEIVED_NETWORK_INTERFACE_CONFIGURATION_UPDATE_NOTIFICATION)

        fetch_network_interface_configuration_status, self.__network_interface_configuration  = self._fetch_configuration_from_endpoint()

        if fetch_network_interface_configuration_status == True:
            self._response_manager.send_response(message=self._message_dictionary,
                                                    status_code=MessageCodeDefinitions.DOWNLOADED_CONFIGURATION_FILE,
                                                    status_message=DOWNLOADED_NETWORK_INTERFACE_CONFIGURATION)

            if self.__network_interface_configuration != b"":
                if HelperFunctions.rotate_files(file_to_be_rotated_filepath=self.__netplan_configuration_filepath,
                                                    data_to_be_written_in_newfile=self.__network_interface_configuration,
                                                    logger_object=self.__logger) == True:
                    if self.__apply_network_interface_configuration() == True:
                        self._response_manager.send_response(message=self._message_dictionary,
                                                                status_code=MessageCodeDefinitions.SUCCESSFULLY_APPLIED_CONFIGURATION_DATA,
                                                                status_message=SUCCESSFULLY_APPLIED_NETWORK_INTERFACE_CONFIGURATION)
                        return True
                    else:
                        self.__logger.error("Failed to apply network interface configuration")
                        self._response_manager.send_response(message=self._message_dictionary,
                                                                status_code=MessageCodeDefinitions.FAILED_TO_APPLY_CONFIGURATION_DATA,
                                                                status_message=FAILED_TO_APPLY_NETWORK_INTERFACE_CONFIGURATION)
                        return False
                else:
                    self.__logger.error("Failed to rotate network interface configuration")
                    return False
            else:
                self.__logger.error("Empty network interface configuration data received")
                self._response_manager.send_response(message=self._message_dictionary,
                                                        status_code=MessageCodeDefinitions.EMPTY_CONFIGURATION_DATA,
                                                        status_message=EMPTY_NETWORK_INTERFACE_CONFIGURATION_DATA)
                return False

        else:
            return False


    def __apply_network_interface_configuration(self):
        self.__logger.info("Applying netplan configuration")
        if HelperFunctions.extract_files_to_directory(zip_compressed_filepath=self.__netplan_configuration_filepath,
                                                        extract_destination_directory_path=self.__temp_netplan_configuration_filepath,
                                                        logger_object=self.__logger) != True:
            return False

        if HelperFunctions.clear_directory(directory_to_be_cleared=NETPLAN_CONFIG_FILE_LOCATION,
                                            logger_object=self.__logger) != True:
            return False

        if HelperFunctions.move_files_in_directory(source_directory_path=self.__temp_netplan_configuration_filepath,
                                                    destination_directory_path=NETPLAN_CONFIG_FILE_LOCATION,
                                                    logger_object=self.__logger) != True:
            return False

        if HelperFunctions.set_executable_permission_to_file(path_to_file=self.__administrative_status_script_filepath,
                                                                logger_object=self.__logger) != True:
            return False

        if HelperFunctions.set_executable_permission_to_file(path_to_file=self.__custom_routing_script_filepath,
                                                                logger_object=self.__logger) != True:
            return False

        try:
            self.__logger.info("Running netplan generate command")
            netplan_generate_status = subprocess.run(self.__netplan_generate_command, shell=True, capture_output=True, text=True)
            self.__logger.info(netplan_generate_status.stdout)
            self.__logger.debug(netplan_generate_status.stderr)
            if netplan_generate_status.returncode != 0:
                return False

            self.__logger.info("Running netplan apply command")
            netplan_apply_status = subprocess.run(self.__netplan_apply_command, shell=True, capture_output=True, text=True)
            self.__logger.info(netplan_apply_status.stdout)
            self.__logger.debug(netplan_apply_status.stderr)
            if netplan_apply_status.returncode != 0:
                return False

            # TBD - A better solution is required for the below issue
            # 1. netplan apply command is run and the linux kernel starts acting on it
            # 2. The administrative-status.sh script brings down the respective interfaces based on user-specified administrative status for that interface
            # 3. The linux kernel acts on the netplan apply command and brings up all the configured interfaces
            # 4. Because of this even though a inteface is configured to brought down by the user, the linux system brings it up again
            # 5. This issue is solved by giving a sleep for 5 seconds after netplan apply, allowing the system to stabilize the interfaces.
            #    Then the administrative-status.sh script is run to bring down the user configured interfaces
            time.sleep(5)

            self.__logger.info("Running administrative-status script")
            admin_script_status = subprocess.run(self.__administrative_status_script_filepath, shell=True, capture_output=True, text=True)
            self.__logger.info(admin_script_status.stdout)
            self.__logger.debug(admin_script_status.stderr)
            if admin_script_status.returncode != 0:
                return False

        except Exception as exception:
            self.__logger.error(exception)
            return False

        return True
