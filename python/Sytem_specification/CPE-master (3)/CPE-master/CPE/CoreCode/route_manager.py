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
import CoreCode.service_manager_linux_helper_functions as LinuxHelperFunctions

PATH_SEPERATOR_CHARACTER = os.path.sep
STATIC_ROUTING_CONFIGURATION_FILE_NAME = "static_routing.zip"
STATIC_ROUTING_CONFIGURATION_FOLDER_NAME = "static_routing"

ETC_FOLDER_NAME = "etc"
FRR_FOLDER_NAME = "frr"
FRR_SERVICE_NAME = "frr.service"
FRR_OWNERSHIP_NAME = "frr"

FRR_SYSTEM_CONFIGURATION_FILE_PATH = PATH_SEPERATOR_CHARACTER + ETC_FOLDER_NAME + PATH_SEPERATOR_CHARACTER + FRR_FOLDER_NAME +PATH_SEPERATOR_CHARACTER

IP_COMMAND_PREFIX = "ip"
IP_COMMAND_JSON_OPTION = "-json"
IP_COMMAND_ALL_TABLE_OPTION = "table all"
IP_COMMAND_LIST_ROUTE_TABLE_OPTION = "route list"
SPACE_CHARACTER = " "

SUCCESSFULY_SHARED_ROUTING_INFO = "Successfully shared routing information"
RECEIVED_NOTIFICATION_TO_SHARE_ROUTING_INFO = "Received notification to share routing information"
UNABLE_TO_GET_ROUTING_INFO = "Unable to get routing information from the system"
FAILED_TO_SHARE_ROUTING_INFO = "Failed to share routing information"

RECEIVED_ROUTINNG_CONFIGURATION_UPDATE_NOTIFICATION = "Received routing configuration update"
DOWNLOADED_ROUTING_CONFIGURATION = "Successfully downloaded routing configuration"
SUCCESSFULLY_APPLIED_ROUTING_CONFIGURATION = "Successfully applied routing configuration"
FAILED_TO_APPLY_ROUTING_CONFIGURATION = "Failed to apply routing configuration"
EMPTY_ROUTING_CONFIGURATION_DATA = "Empty routing configuration data"


class RouteManager(ServiceManager):
    """
    RouteManager is derived from ServiceManager and is used to execute operations with respect to the routing configuration
    Arguments:
    data_manager:
        An instance of DataManager must be passed. This instance is used to fetch the configuration file from the endpoint 
        and also to send the routing information to the Backend
    response_manager:
        An instance of ResponseManager must be passed
    """
    def __init__(self, data_manager, response_manager):
        self.__logger = Logger.get_logger(__name__)
        self.__logger.info("RouteManager initializer starts")

        self.__static_routing_configuration_filepath = SystemDefinitions.USER_CONFIG_FILE_PATH + PATH_SEPERATOR_CHARACTER + STATIC_ROUTING_CONFIGURATION_FILE_NAME
        self.__temp_static_routing_configuration_filepath = SystemDefinitions.TEMP_USER_CONFIG_FILE_PATH + PATH_SEPERATOR_CHARACTER + STATIC_ROUTING_CONFIGURATION_FOLDER_NAME

        self.__routing_information_ip_command = IP_COMMAND_PREFIX + SPACE_CHARACTER + \
                                                IP_COMMAND_JSON_OPTION + SPACE_CHARACTER + \
                                                IP_COMMAND_LIST_ROUTE_TABLE_OPTION + SPACE_CHARACTER + \
                                                IP_COMMAND_ALL_TABLE_OPTION
                                            
        event_dictionary = {}
        event_dictionary[MessageCodeDefinitions.SHARE_ROUTE_INFO_EVENT] =  self.__share_route_information_event_routine
        event_dictionary[MessageCodeDefinitions.ROUTE_CONFIGURATION_UPDATE_EVENT] =  self.__configuration_update_available_event_routine

        ServiceManager.__init__(self, data_manager=data_manager, response_manager=response_manager, event_dictionary=event_dictionary)
        self.__logger.info("RouteManager initializer ends")


    def __share_route_information_event_routine(self):
        self.__logger.info("Share route information event routine start")
        self._response_manager.send_response(message=self._message_dictionary,
                                            status_code=MessageCodeDefinitions.RECEIVED_NOTIFICATION_TO_SHARE_ROUTING_INFORMATION,
                                            status_message=RECEIVED_NOTIFICATION_TO_SHARE_ROUTING_INFO)

        route_command_execution_status, route_information = self.__get_route_information()   

        if route_command_execution_status == True:

            try:
                destination_endpoint = self._message_dictionary[MessageDefinitions.CONTENT_KEY][MessageDefinitions.ENDPOINT_KEY]
            except Exception as exception:
                self.__logger.error(exception)

            route_information_message = dict()
            route_information_message["routes"] = json.loads(route_information)

            put_data_status = self._data_manager.put_data(route_information_message, destination_endpoint)

            if put_data_status == True:
                self._response_manager.send_response(message=self._message_dictionary,
                                                   status_code=MessageCodeDefinitions.SUCCESSFULLY_SHARED_ROUTING_INFORMATION,
                                                   status_message=SUCCESSFULY_SHARED_ROUTING_INFO)
                return True
            else:
                self._response_manager.send_response(message=self._message_dictionary,
                                                    status_code=MessageCodeDefinitions.FAILED_TO_SHARE_ROUTING_INFORMATION,
                                                    status_message=FAILED_TO_SHARE_ROUTING_INFO)
                return False 
        else:
            return False


    def __get_route_information(self):
        routing_information = ""

        try:
            get_routing_info = subprocess.Popen(self.__routing_information_ip_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            routing_information, ip_command_error_information = get_routing_info.communicate()
            self.__logger.debug(ip_command_error_information)
            
        except Exception as exception:
            self.__logger.error(exception)
            self._response_manager.send_response(message=self._message_dictionary,
                                                status_code=MessageCodeDefinitions.UNABLE_TO_GET_ROUTING_INFORMATION_FROM_SYSTEM,
                                                status_message=UNABLE_TO_GET_ROUTING_INFO)
            return False, routing_information

        return True, routing_information
    

    def __configuration_update_available_event_routine(self):
        self.__logger.info("Route configuration update event routine start")
        self._response_manager.send_response(message=self._message_dictionary, 
                                                status_code=MessageCodeDefinitions.RECEIVED_CONFIGURATION_UPDATE_NOTIFICATION,
                                                status_message=RECEIVED_ROUTINNG_CONFIGURATION_UPDATE_NOTIFICATION)
        
        fetch_routing_configuration_status, self.__routing_configuration  = self._fetch_configuration_from_endpoint()

        if fetch_routing_configuration_status == True:
            self._response_manager.send_response(message=self._message_dictionary, 
                                                    status_code=MessageCodeDefinitions.DOWNLOADED_CONFIGURATION_FILE,
                                                    status_message=DOWNLOADED_ROUTING_CONFIGURATION)

            if self.__routing_configuration != b"": 
                if HelperFunctions.rotate_files(file_to_be_rotated_filepath=self.__static_routing_configuration_filepath,
                                                    data_to_be_written_in_newfile=self.__routing_configuration,
                                                    logger_object=self.__logger) == True:
                    if self.__apply_route_configuration() == True:
                        self.__logger.info("Configuration Applied successfully")
                        self._response_manager.send_response(message=self._message_dictionary, 
                                                                status_code=MessageCodeDefinitions.SUCCESSFULLY_APPLIED_CONFIGURATION_DATA,
                                                                status_message=SUCCESSFULLY_APPLIED_ROUTING_CONFIGURATION)
                        return True
                    else:
                        self.__logger.error("Failed to apply routing configuration")
                        self._response_manager.send_response(message=self._message_dictionary, 
                                                                status_code=MessageCodeDefinitions.FAILED_TO_APPLY_CONFIGURATION_DATA,
                                                                status_message=FAILED_TO_APPLY_ROUTING_CONFIGURATION)
                        return False
                else:
                    self.__logger.error("Failed to rotate routing configuration")                
                    return False
            else:
                self.__logger.error("Empty routing configuration data received")
                self._response_manager.send_response(message=self._message_dictionary, 
                                                        status_code=MessageCodeDefinitions.EMPTY_CONFIGURATION_DATA,
                                                        status_message=EMPTY_ROUTING_CONFIGURATION_DATA)
                return False

        else:
            return False   
    

    def __apply_route_configuration(self):
        self.__logger.info("Applying frr configuration")

        if HelperFunctions.extract_files_to_directory(zip_compressed_filepath=self.__static_routing_configuration_filepath,
                                                        extract_destination_directory_path=self.__temp_static_routing_configuration_filepath,
                                                        logger_object=self.__logger) == False:
            return False

        if HelperFunctions.clear_directory(directory_to_be_cleared=FRR_SYSTEM_CONFIGURATION_FILE_PATH, logger_object=self.__logger) == False:
            return False
        
        temp_frr_static_routing_configuration_directory_path = self.__temp_static_routing_configuration_filepath + PATH_SEPERATOR_CHARACTER + FRR_FOLDER_NAME
        if HelperFunctions.move_files_in_directory(source_directory_path=temp_frr_static_routing_configuration_directory_path,
                                                    destination_directory_path=FRR_SYSTEM_CONFIGURATION_FILE_PATH, 
                                                    logger_object= self.__logger) == False:
            return False

        if LinuxHelperFunctions.change_directory_and_its_files_ownership(user_name=FRR_OWNERSHIP_NAME, group_name=FRR_OWNERSHIP_NAME,
                                                                            directory_path=FRR_SYSTEM_CONFIGURATION_FILE_PATH,
                                                                            logger_object=self.__logger) == False:
            return False

        if LinuxHelperFunctions.restart_system_service(service_name=FRR_SERVICE_NAME,
                                                            logger_object=self.__logger) == False:
            return False
        
        return True
