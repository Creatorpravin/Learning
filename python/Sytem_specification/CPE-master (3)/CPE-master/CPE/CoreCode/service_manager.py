import os 

import CoreCode.logger as Logger
import CoreCode.chiefnet_exception as ChiefnetException
import Definitions.system_definitions as SystemDefinitions
import Definitions.message_definitions as MessageDefinitions
import Definitions.message_code_definitions as MessageCodeDefinitions

UNREGISTERED_EVENT_CODE_MESSAGE = "Unregistered event code"
FILENAME_EXTENSION_SEPARATOR = "."
OLD_CONFIGURATION_FILENAME_SUFFIX = "-old"
FILENAME_INDEX = 0
FILE_EXTENSION_INDEX = 1


class ServiceManager():
    """
    ServiceManager is the base class for all services

    Arguments:
    data_manager:
        An instance of the DataManager must be passed. This is used to fetch/post data from the provided endpoint.
    response_manager:
        An instance of the ResponseManager must be passed.
    event_dictionary:
        A dictionary containing event code and there corresponding event routines.
    new_configuration_filepath:
        String containing the name and path of configuration file in which the received configuration will be return. 
    """
    # TBD - Must figure out the proper way to manage logger objects across inheritance
    logger = Logger.get_logger(__name__)

    def __init__(self, data_manager, response_manager, event_dictionary):
        ServiceManager.logger.info("ServiceManager initializer starts")

        self._data_manager = data_manager
        self._response_manager = response_manager

        self.__event_dictionary = event_dictionary

        ServiceManager.logger.info("ServiceManager initializer ends")


    def service_handler_function(self, message_dictionary):
        """
        This function must be registered with action handler to receive data from the user
        Args    - message_dictionary : dict type - the JSON message sent by the Websocket server parsed into a dictionary
        Returns - None
        Raises  - None
        """
        self._message_dictionary = message_dictionary        

        try:
            event_code = self._message_dictionary[MessageDefinitions.CONTENT_KEY][MessageDefinitions.EVENT_CODE_KEY]
            service_code = self._message_dictionary[MessageDefinitions.SERVICE_CODE_KEY]
        except KeyError as key_error:
            ServiceManager.logger.error(key_error)
        except Exception as exception:
            ServiceManager.logger.error(exception)

        event_routine = self.__fetch_event_routine(event_code=event_code)

        ServiceManager.logger.info("Service {} Event {} starts".format(service_code, event_code))

        if event_routine() == True: 
            ServiceManager.logger.info("Service {} Event {} successful".format(service_code, event_code))
        else:
            ServiceManager.logger.error("Service {} Event {} failed/unavailable".format(service_code, event_code))

        ServiceManager.logger.info("Service {} Event {} ends".format(service_code, event_code))


    def __fetch_event_routine(self, event_code):        
        if event_code not in self.__event_dictionary:
            self._response_manager.send_response(message=self._message_dictionary, 
                                                    status_code=MessageCodeDefinitions.UNREGISTERED_EVENT_CODE,
                                                    status_message=UNREGISTERED_EVENT_CODE_MESSAGE)

        return self.__event_dictionary.get(event_code, lambda : False)
   

    def _fetch_configuration_from_endpoint(self):
        configuration_data = ""

        try:
            endpoint = self._message_dictionary[MessageDefinitions.CONTENT_KEY][MessageDefinitions.ENDPOINT_KEY]
            checksum = self._message_dictionary[MessageDefinitions.CONTENT_KEY][MessageDefinitions.CONFIG_FILE_CHECKSUM_KEY]
        except KeyError as key_error:
            ServiceManager.logger.error(key_error)
            return False, configuration_data
        except Exception as exception:
            ServiceManager.logger.error(exception)
            return False, configuration_data

        try:
            configuration_data = self._data_manager.get_data(endpoint=endpoint, checksum=checksum)
        except ChiefnetException.DataFetchFailedException as data_fetch_failed_exception:
            ServiceManager.logger.error(data_fetch_failed_exception)
            self._response_manager.send_response(message=self._message_dictionary, 
                                                    status_code=MessageCodeDefinitions.DATA_FETCH_FAILED,
                                                    status_message=str(data_fetch_failed_exception))
            return False, configuration_data

        except ChiefnetException.ChecksumMismatchException as checksum_mismatch_exception:
            ServiceManager.logger.error(checksum_mismatch_exception)
            self._response_manager.send_response(message=self._message_dictionary, 
                                                    status_code=MessageCodeDefinitions.CONFIGURATION_FILE_CHECKSUM_MISMATCH,
                                                    status_message=str(checksum_mismatch_exception))
            return False, configuration_data
        
        return True, configuration_data