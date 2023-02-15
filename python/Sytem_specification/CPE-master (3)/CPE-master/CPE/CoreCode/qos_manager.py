import os
import subprocess

import CoreCode.logger as Logger
import Definitions.system_definitions as SystemDefinitions
import Definitions.message_definitions as MessageDefinitions
import Definitions.message_code_definitions as MessageCodeDefinitions

from CoreCode.service_manager import ServiceManager
import CoreCode.chiefnet_exception as ChiefnetException
import CoreCode.service_manager_helper_functions as HelperFunctions

QOS_CONFIGURATION_SCRIPT_FILENAME = "qos-configuration.sh"

PATH_SEPERATOR_CHARACTER = os.path.sep

RECEIVED_QOS_CONFIGURATION_UPDATE_NOTIFICATION = "Received QoS configuration update notification"
DOWNLOADED_QOS_CONFIGURATION_FILE = "Downloaded QoS configuration file"
SUCCESSFULLY_APPLIED_QOS_CONFIGURATION = "Successfully run qos configuration script"
FAILED_TO_APPLY_QOS_CONFIGURATION = "Failed to apply qos configuration script"
EMPTY_QOS_CONFIGURATION_DATA = "Empty qos configuration data received"


class QoSManager(ServiceManager):
    """
    QoSManager is derived from ServiceManager and is used to execute operations with respect to the system's Quality of Service(QoS)
    Arguments:
    data_manager:
        An instance of DataFetcher must be passed. 
    response_manager:
        An instance of ResponseManager must be passed.
    """
    def __init__(self, data_manager, response_manager):
        self.__logger = Logger.get_logger(__name__)
        self.__logger.info("QoSManager initializer starts")

        self.__qos_configuration_filepath = SystemDefinitions.USER_CONFIG_FILE_PATH + PATH_SEPERATOR_CHARACTER + QOS_CONFIGURATION_SCRIPT_FILENAME

        # insert event codes and corresponding routines into this dictionary
        event_dictionary = {}
        event_dictionary[MessageCodeDefinitions.QOS_CONFIGURATION_UPDATE_EVENT] = self.__configuration_update_available_event_routine

        ServiceManager.__init__(self, data_manager=data_manager, response_manager=response_manager, event_dictionary=event_dictionary)          

        # Applying the qos configuration when the QoSManager instance is created, to restore the previous configuration when the CPE application starts. 
        self.__apply_qos_configuration()

        self.__logger.info("QoSManager initializer ends")


    def __configuration_update_available_event_routine(self):
        self.__logger.info("QOS configuration update event routine start")
        
        self._response_manager.send_response(message=self._message_dictionary, 
                                                status_code=MessageCodeDefinitions.RECEIVED_CONFIGURATION_UPDATE_NOTIFICATION,
                                                status_message=RECEIVED_QOS_CONFIGURATION_UPDATE_NOTIFICATION)
        
        fetch_qos_configuration_status, self.__qos_configuration_data = self._fetch_configuration_from_endpoint()

        if fetch_qos_configuration_status == True:
            self._response_manager.send_response(message=self._message_dictionary, 
                                                    status_code=MessageCodeDefinitions.DOWNLOADED_CONFIGURATION_FILE,
                                                    status_message=DOWNLOADED_QOS_CONFIGURATION_FILE)
            
            if self.__qos_configuration_data != b"":
                if HelperFunctions.rotate_files(file_to_be_rotated_filepath=self.__qos_configuration_filepath,
                                                    data_to_be_written_in_newfile=self.__qos_configuration_data,
                                                    logger_object=self.__logger) == True:
                        if HelperFunctions.set_executable_permission_to_file(path_to_file=self.__qos_configuration_filepath, 
                                                                                logger_object=self.__logger) == True:
                            if self.__apply_qos_configuration() == True:
                                self._response_manager.send_response(message=self._message_dictionary, 
                                                                        status_code=MessageCodeDefinitions.SUCCESSFULLY_APPLIED_CONFIGURATION_DATA,
                                                                        status_message=SUCCESSFULLY_APPLIED_QOS_CONFIGURATION)
                                return True
                            else:
                                self.__logger.error("Failed to apply qos configuration settings")
                                self._response_manager.send_response(message=self._message_dictionary, 
                                                                        status_code=MessageCodeDefinitions.FAILED_TO_APPLY_CONFIGURATION_DATA,
                                                                        status_message=FAILED_TO_APPLY_QOS_CONFIGURATION)
                                return False
                        else:
                            self.__logger.error("Unable to set executable permission to qos_configuration.sh")
                else:
                    self.__logger.error("Failed to rotate qos configuration files")                
                    return False
            else:
                self.__logger.error("Empty qos configuration data received")
                self._response_manager.send_response(message=self._message_dictionary, 
                                                        status_code=MessageCodeDefinitions.EMPTY_CONFIGURATION_DATA,
                                                        status_message=EMPTY_QOS_CONFIGURATION_DATA)
                return False
        else:
            return False
            

    def __apply_qos_configuration(self):
        # since we are running a script to apply the qos configuration, checking for the exit code will not be 
        # the proper way of validating whether the configuration has been applied without any error.
        # TBD - Validating whether the configuration is applied successfully

        if os.path.exists(self.__qos_configuration_filepath):
            try:
                result = subprocess.run(self.__qos_configuration_filepath, capture_output=True)    
            
                self.__logger.info(result.stdout)
                self.__logger.debug(result.stderr)

                self.__logger.info("{} configuration applied successfully".format(self.__qos_configuration_filepath))
                return True
            
            # In subprocess.run() if check is true, and the process exits with a non-zero exit code, a CalledProcessError exception will be raised. 
            # Attributes of that exception hold the arguments, the exit code, and stdout and stderr if they were captured.
            # We can use this to verify if each command of the script has been executed successfully.
            except Exception as exception:
                self.__logger.error(exception)
                return False
    
        else:
            self.__logger.error("{} configuration file does not exist".format(self.__qos_configuration_filepath))
            return False
