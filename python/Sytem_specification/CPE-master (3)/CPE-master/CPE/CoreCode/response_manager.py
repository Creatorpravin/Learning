import time
import json
import uuid

import CoreCode.logger as Logger
import Definitions.message_definitions as MessageDefinitions


class ResponseManager():
    """
    ResponseManager frames all type of response and sends it to the server using CommunicationManager 

    Arguments:
    communication_manager:
        Instance of CommunicationManager
    system_configuration_manager:
        Instance of SystemConfigurationManager
    """

    def __init__(self, communication_manager, system_configuration_manager):
        self.__logger = Logger.get_logger(logger_name=__name__)

        self.__logger.info("ResponseManager initializer starts")

        self.__communication_manager = communication_manager
        self.__system_configuration_manager = system_configuration_manager

        self.__logger.info("ResponseManager initializer ends")
    

    def send_response(self, message, status_code, status_message):
        """
        This method is used to frames and sends response to the server 
        If frame_Response got any exception this function sends empty string to the server
        Args   - message : dict type - message for which we are sending the response
                 status_code : int type - code of the succes/error status
        Return - True on Success
                 False on Failure
        Raises - None
        """
        try:
            framed_response = self.__frame_response(message_uid=message[MessageDefinitions.MESSAGE_UID_KEY],
                                                        service_code=message[MessageDefinitions.SERVICE_CODE_KEY], 
                                                        event_code=message[MessageDefinitions.CONTENT_KEY][MessageDefinitions.EVENT_CODE_KEY], 
                                                        status_code=status_code, status_message=status_message)
        except Exception as exceptions:
            self.__logger.error(exceptions)
            framed_response = ""
        
        if framed_response != "":
            try:
                self.__communication_manager.send_data(data=framed_response)

                self.__logger.info("Response status of {0} for message with MessageUID : {1} sent successfully"
                                    .format(status_code, message[MessageDefinitions.MESSAGE_UID_KEY]))
                return True
            except Exception as exception:
                self.__logger.error(exception)
                return False
        else:
            self.__logger.error("Empty Framed Response")
            return False


    def __frame_response(self, message_uid, service_code, event_code, status_code, status_message):
        response_message_dict = {}

        framed_response = ""
        response_message_uid = ""
        timestamp = 0

        try:
            timestamp = int(time.time())
        except Exception as exception:
            self.__logger.error(exception)
            return framed_response

        try:
            response_message_uid = str(uuid.uuid4())
        except Exception as exception:
            self.__logger.error(exception)
            return framed_response

        response_message_dict[MessageDefinitions.TIMESTAMP_KEY] = timestamp
        response_message_dict[MessageDefinitions.MESSAGE_UID_KEY] = response_message_uid
        response_message_dict[MessageDefinitions.DEVICE_ID_KEY] = self.__system_configuration_manager.get_device_id()
        response_message_dict[MessageDefinitions.SERVICE_CODE_KEY] = service_code

        response_message_dict[MessageDefinitions.CONTENT_KEY] = {}
        response_message_dict[MessageDefinitions.CONTENT_KEY][MessageDefinitions.EVENT_CODE_KEY] = event_code
        response_message_dict[MessageDefinitions.CONTENT_KEY][MessageDefinitions.STATUS_CODE_KEY] = status_code
        response_message_dict[MessageDefinitions.CONTENT_KEY][MessageDefinitions.STATUS_MESSAGE_KEY] = status_message
        response_message_dict[MessageDefinitions.CONTENT_KEY][MessageDefinitions.RESPOSNE_TO_MESSAGE_UID_KEY] = message_uid

        try:
            framed_response = json.dumps(response_message_dict) 
        except Exception as exception:
            self.__logger.error(exception)

        return framed_response