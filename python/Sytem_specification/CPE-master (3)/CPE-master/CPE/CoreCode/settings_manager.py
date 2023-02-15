import os

import CoreCode.logger as Logger
import Definitions.system_definitions as SystemDefinitions
import Definitions.message_code_definitions as MessageCodeDefinitions

from CoreCode.service_manager import ServiceManager
import CoreCode.service_manager_helper_functions as HelperFunctions

PATH_SEPERATOR_CHARACTER = os.path.sep
FACTORY_CONFIG_FILE_NAME = "FactoryReset.zip"
FACTORY_CONFIG_FOLDER_NAME = "FactoryReset"
DEFAULT_FACTORY_CONFIG_FILE_LOCATION = SystemDefinitions.BASE_DIRECTORY + FACTORY_CONFIG_FOLDER_NAME

RECEIVED_FACTORY_RESET_CONFIGURATION_UPDATE_NOTIFICATION = "Received factory resetconfiguration update"
DOWNLOADED_FACTORY_RESET_CONFIGURATION = "Successfully downloaded factory resetconfiguration"
SUCCESSFULLY_APPLIED_FACTORY_RESET_CONFIGURATION = "Successfully applied factory resetconfiguration"
FAILED_TO_APPLY_FACTORY_RESET_CONFIGURATION = "Failed to apply factory resetconfiguration"
EMPTY_FACTORY_RESET_CONFIGURATION_DATA = "Empty factory resetconfiguration data"


class SettingsManager(ServiceManager):
    """
    SettingsManager is derived from ServiceManager and is used to execute operations with respect to the system settings
    Arguments:
    data_manager:
        An instance of DataManager must be passed. This instance is used to fetch the setting file from the endpoint
    response_manager:
        An instance of ResponseManager must be passed
    """
    def __init__(self, data_manager, response_manager):
        self.__logger = Logger.get_logger(__name__)
        self.__logger.info("SettingsManager initializer starts")

        self.__factory_reset_configuration_filepath = SystemDefinitions.USER_CONFIG_FILE_PATH + PATH_SEPERATOR_CHARACTER + FACTORY_CONFIG_FILE_NAME
        self.__temp_factory_reset_configuration_filepath = SystemDefinitions.TEMP_USER_CONFIG_FILE_PATH + PATH_SEPERATOR_CHARACTER + FACTORY_CONFIG_FOLDER_NAME + PATH_SEPERATOR_CHARACTER

        self.__factory_reset_configuration = ""

        # insert event codes and corresponding routines into this dictionary
        event_dictionary = {}
        event_dictionary[MessageCodeDefinitions.FACTORY_RESET_CONFIGURATION_UPDATE_EVENT] = self.__update_factory_default_configuration_event_routine

        ServiceManager.__init__(self, data_manager=data_manager, response_manager=response_manager, event_dictionary=event_dictionary)
        self.__logger.info("SettingsManager initializer ends")


    def __update_factory_reset_configuration(self):
        if HelperFunctions.rotate_files(file_to_be_rotated_filepath=self.__factory_reset_configuration_filepath,
                                        data_to_be_written_in_newfile=self.__factory_reset_configuration,
                                        logger_object=self.__logger) is False:
            return False

        if HelperFunctions.extract_files_to_directory(zip_compressed_filepath=self.__factory_reset_configuration_filepath,
                                                      extract_destination_directory_path=self.__temp_factory_reset_configuration_filepath,
                                                      logger_object=self.__logger) is False:
            return False

        if HelperFunctions.clear_directory(directory_to_be_cleared=DEFAULT_FACTORY_CONFIG_FILE_LOCATION,
                                           logger_object=self.__logger) is False:
            return False

        if HelperFunctions.move_files_in_directory(source_directory_path=self.__temp_factory_reset_configuration_filepath,
                                                   destination_directory_path=DEFAULT_FACTORY_CONFIG_FILE_LOCATION,
                                                   logger_object=self.__logger) is False:
            return False

        self.__logger.info("Factory reset configuration updated successfully")
        return True


    def __update_factory_default_configuration_event_routine(self):
        self.__logger.info("Factory Reset configuration update event routine start")
        self._response_manager.send_response(message=self._message_dictionary,
                                             status_code=MessageCodeDefinitions.RECEIVED_CONFIGURATION_UPDATE_NOTIFICATION,
                                             status_message=RECEIVED_FACTORY_RESET_CONFIGURATION_UPDATE_NOTIFICATION)

        fetch_factory_reset_configuration_status, self.__factory_reset_configuration = self._fetch_configuration_from_endpoint()

        if fetch_factory_reset_configuration_status is True:
            self._response_manager.send_response(message=self._message_dictionary,
                                                 status_code=MessageCodeDefinitions.DOWNLOADED_CONFIGURATION_FILE,
                                                 status_message=DOWNLOADED_FACTORY_RESET_CONFIGURATION)

            if self.__factory_reset_configuration != b"":

                if self.__update_factory_reset_configuration() is True:
                    self._response_manager.send_response(message=self._message_dictionary,
                                                         status_code=MessageCodeDefinitions.SUCCESSFULLY_APPLIED_CONFIGURATION_DATA,
                                                         status_message=SUCCESSFULLY_APPLIED_FACTORY_RESET_CONFIGURATION)
                    return True
                else:
                    self._response_manager.send_response(message=self._message_dictionary,
                                                         status_code=MessageCodeDefinitions.FAILED_TO_APPLY_CONFIGURATION_DATA,
                                                         status_message=FAILED_TO_APPLY_FACTORY_RESET_CONFIGURATION)
                    return False

            else:
                self.__logger.error("Empty factory resetconfiguration data received")
                self._response_manager.send_response(message=self._message_dictionary,
                                                     status_code=MessageCodeDefinitions.EMPTY_CONFIGURATION_DATA,
                                                     status_message=EMPTY_FACTORY_RESET_CONFIGURATION_DATA)
                return False

        else:
            self.__logger.error("Failed to fetch factory reset configuration")
            return False
