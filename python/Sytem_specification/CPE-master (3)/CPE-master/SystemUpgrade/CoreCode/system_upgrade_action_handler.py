import json
import threading
import queue

import CoreCode.logger as Logger
import Definitions.message_definitions as MessageDefinitions
import Definitions.message_code_definitions as MessageCodeDefinitions

UNREGISTERED_SERVICE_CODE = "Unregistered service code"


class SystemUgradeActionHandler:
    """
    Action handler is used to forward the data received from the websocket manager to the respective service managers 
    The service managers requiring to receive a message from the cloud must be registered with the action handler
    along with their service codes in order to receive messages.

    Arguments:
    system_configuration_manager:
        An instance of SystemConfigurationManager must be constructed and passed to the SystemUgradeActionHandler. This instance will 
        be used to validate the message contents with the device specific parameters
    """

    def __init__(self, system_configuration_manager, response_manager):
        self.__logger = Logger.get_logger(logger_name=__name__)
        self.__logger.info("SystemUgradeActionHandler object initialization starts")

        self.__system_configuration_manager = system_configuration_manager
        self.__response_manager = response_manager

        self.__message_received_callback_dictionary = {}
        self.__received_message_queue = queue.Queue()
        
        self.__message_received_event = threading.Event()
        self.__message_received_event.clear()

        self.__message_handler_thread = threading.Thread(target=self.__message_handler_thread_function, daemon=True)
        self.__message_handler_thread.start()

        self.__logger.info("SystemUgradeActionHandler object initialization ends")


    def register_message_received_callback(self, service_code, callback_function):
        """
        This function is used to register the service manager callbacks with the action handler.
        Each service manager has a unique service code which must be provided while registering the callback
        Args   - service_code - integer type service code corresponding to the service manager being registered
                 service_manager - an instance of type ServiceManager must be registered
        Return - None
        Raises - None
        """
        self.__message_received_callback_dictionary[service_code] = callback_function


    def message_receive_callback(self, message):
        """
        This callback is registered with the communication module. A message received from the user
        through the communication module is passed as an argument to this callback function
        Args   - message - placeholder to receive message from the user
        Return - None
        Raises - None
        """
        self.__received_message_queue.put(message)
        self.__message_received_event.set()
    

    def __message_handler_thread_function(self):
        # TBD - Once the internal flag is set, this acts as a while TRUE loop
        # If cleared immediately after wait has returned, data loss occurs
        while self.__message_received_event.wait():       
            message = self.__received_message_queue.get()          
            if len(message) > 0:
                if self.__validate_message(message) == True:
                    try:
                        if self.__parsed_message[MessageDefinitions.DEVICE_ID_KEY] == self.__system_configuration_manager.get_device_id():
                            if self.__parsed_message[MessageDefinitions.SERVICE_CODE_KEY] in self.__message_received_callback_dictionary:
                                self.__message_received_callback_dictionary[self.__parsed_message[MessageDefinitions.SERVICE_CODE_KEY]](self.__parsed_message)
                            else:
                                self.__logger.error("User specified service code not registered with action_handler")
                                self.__response_manager.send_response(message=self.__parsed_message, 
                                                                        status_code=MessageCodeDefinitions.UNREGISTERED_SERVICE_CODE,
                                                                        status_message=UNREGISTERED_SERVICE_CODE)
                        else:
                            self.__logger.error("Message DeviceID different from configured device ID")
                    except Exception as exception:
                        self.__logger.error(exception)
                else:
                    self.__logger.error("JSON validation failed")    
            else:
                self.__logger.error("Empty message from websocket")


    def __validate_message(self, message):
        return_value = True
        try:
            self.__parsed_message = json.loads(message)
            
            # parsed JSON object can be 'dict' or 'list' depending on whether the JSON string contains object or array
            # simple strings qualify for a valid JSON. Hence checking if the received message is a JSON object
            if type(self.__parsed_message) != dict:
                self.__logger.error("Received JSON message not a JSON object")
                return_value = False

        # The best practice is to capture the JsonDecodeError instead of ValueError while using JSON data  
        except json.JSONDecodeError:
            self.__logger.error("Message is not a valid JSON")
            return_value = False
        except Exception as exception:
            self.__logger.error(exception)
            return_value = False
        
        return return_value
