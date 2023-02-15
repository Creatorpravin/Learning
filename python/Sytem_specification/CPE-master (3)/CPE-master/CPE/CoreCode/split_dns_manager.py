import os
import subprocess

import CoreCode.logger as Logger
import Definitions.system_definitions as SystemDefinitions
import Definitions.message_code_definitions as MessageCodeDefinitions

from CoreCode.service_manager import ServiceManager
import CoreCode.service_manager_helper_functions as HelperFunctions

PATH_SEPERATOR_CHARACTER = os.path.sep
SPACE_CHARACTER = " "

SYSTEMCTL_COMMAND_PREFIX = "systemctl"
SYSTEMCTL_RESTART_OPTION = "restart"

DNSMASQ_SERVICE_NAME = "dnsmasq.service"
SPLIT_DNS_CONFIG_FILENAME = "split-dns.conf"
ETC_DIRECTORY_NAME = "etc"
DNSMASQ_CONFIG_FOLDER_NAME = "dnsmasq.d"
DNSMASQ_CONFIG_FILE_LOCATION = PATH_SEPERATOR_CHARACTER + ETC_DIRECTORY_NAME + PATH_SEPERATOR_CHARACTER + DNSMASQ_CONFIG_FOLDER_NAME

SUCCESSFULLY_APPLIED_SPLIT_DNS_CONFIGURATION = "Successfully applied split DNS configuration"
RECEIVED_SPLIT_DNS_CONFIGURATION_UPDATE_NOTIFICATION = "Received split DNS configuration update notification"
DOWNLOADED_SPLIT_DNS_CONFIGURATION = "Successfully downloaded split DNS configuration"

EMPTY_DNSMASQ_CONFIGURATION_DATA = "Empty dnsmasq configuration data received"
FAILED_TO_APPLY_DNSMASQ_CONFIGURATION = "Failed to apply dnsmasq configuration"


class SplitDNSManager(ServiceManager):
    """
    SplitDNSManager is derived from ServiceManager and is used to handle operations with respect to split DNS on the CPE side
    Arguments:
    data_manager:
        An instance of DataManager must be passed. This instance is used to fetch the dnsmasq configuration files from the endpoint 
    response_manager:
        An instance of ResponseManager must be passed to send responses to the WebApp
    """

    def __init__(self, data_manager, response_manager):
        self.__logger = Logger.get_logger(__name__)
        self.__logger.info("SplitDNSManager initializer starts")

        self.__split_dns_configuration_etc_directory_filepath = DNSMASQ_CONFIG_FILE_LOCATION + PATH_SEPERATOR_CHARACTER + SPLIT_DNS_CONFIG_FILENAME
        self.__split_dns_configuration_filepath = SystemDefinitions.USER_CONFIG_FILE_PATH + PATH_SEPERATOR_CHARACTER + SPLIT_DNS_CONFIG_FILENAME
        self.__dnsmasq_restart_command = SYSTEMCTL_COMMAND_PREFIX + SPACE_CHARACTER \
                                            + SYSTEMCTL_RESTART_OPTION + SPACE_CHARACTER + DNSMASQ_SERVICE_NAME

        # insert event codes and corresponding routines into this dictionary
        event_dictionary = {}
        event_dictionary[MessageCodeDefinitions.SPLIT_DNS_CONFIGURATION_UPDATE_EVENT] = self.__split_dns_configuration_update_event_routine

        ServiceManager.__init__(self, data_manager=data_manager, response_manager=response_manager, event_dictionary=event_dictionary)
        self.__logger.info("SplitDNSManager initializer ends")


    def __split_dns_configuration_update_event_routine(self):
        self.__logger.info("Split DNS configuration update event routine start")
        self._response_manager.send_response(message=self._message_dictionary, 
                                                status_code=MessageCodeDefinitions.RECEIVED_CONFIGURATION_UPDATE_NOTIFICATION,
                                                status_message=RECEIVED_SPLIT_DNS_CONFIGURATION_UPDATE_NOTIFICATION)
        
        fetch_split_dns_configuration_status, self.__split_dns_configuration = self._fetch_configuration_from_endpoint()
        
        if fetch_split_dns_configuration_status == True:
            self._response_manager.send_response(message=self._message_dictionary, 
                                                    status_code=MessageCodeDefinitions.DOWNLOADED_CONFIGURATION_FILE,
                                                    status_message=DOWNLOADED_SPLIT_DNS_CONFIGURATION)

            if self.__split_dns_configuration != b"": 
                if HelperFunctions.rotate_files(file_to_be_rotated_filepath=self.__split_dns_configuration_filepath,
                                                    data_to_be_written_in_newfile=self.__split_dns_configuration,
                                                    logger_object=self.__logger) == True:
                    if self.__apply_split_dns_configuration() == True:
                        self._response_manager.send_response(message=self._message_dictionary, 
                                                                status_code=MessageCodeDefinitions.SUCCESSFULLY_APPLIED_CONFIGURATION_DATA,
                                                                status_message=SUCCESSFULLY_APPLIED_SPLIT_DNS_CONFIGURATION)
                        return True
                    else:
                        self.__logger.error("Failed to apply split-DNS configuration")
                        self._response_manager.send_response(message=self._message_dictionary, 
                                                                status_code=MessageCodeDefinitions.FAILED_TO_APPLY_CONFIGURATION_DATA,
                                                                status_message=FAILED_TO_APPLY_DNSMASQ_CONFIGURATION)
                        return False
                else:
                    self.__logger.error("Failed to rotate split-DNS configuration")                
                    return False
            else:
                self.__logger.error("Empty split-DNS configuration data received")
                self._response_manager.send_response(message=self._message_dictionary, 
                                                        status_code=MessageCodeDefinitions.EMPTY_CONFIGURATION_DATA,
                                                        status_message=EMPTY_DNSMASQ_CONFIGURATION_DATA)
                return False
        else:
            return False   
    

    def __apply_split_dns_configuration(self):
        self.__logger.info("Apply split-DNS configuration")
        
        # Delete the /etc/dnsmasq.d/split-dns.conf file
        if HelperFunctions.remove_file_if_exists(filepath=self.__split_dns_configuration_etc_directory_filepath, 
                                                    logger_object=self.__logger) != True:
            return False

        if HelperFunctions.copy_file(source_filepath=self.__split_dns_configuration_filepath, 
                                    destination_filepath=DNSMASQ_CONFIG_FILE_LOCATION, 
                                    logger_object=self.__logger) != True:
            return False

        try:
            self.__logger.info("Restarting dnsmasq service to apply split-DNS configuration changes")
            dnsmasq_restart_status = subprocess.run(self.__dnsmasq_restart_command, shell=True, capture_output=True, text=True)            
            self.__logger.info(dnsmasq_restart_status.stdout)
            self.__logger.debug(dnsmasq_restart_status.stderr)

            if dnsmasq_restart_status.returncode != 0:
                return False
                
        except Exception as exception:
            self.__logger.error(exception)
            return False
        
        return True
