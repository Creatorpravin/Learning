import json
import os
import threading
import signal

import CoreCode.logger as Logger
import CoreCode.chiefnet_exception as ChiefnetException
import Definitions.system_definitions as SystemDefinitions
import Definitions.message_definitions as MessageDefinitions

UTF8_DECODING_FORMAT = "utf-8"

PROVISIONED_RESPONSE_ERROR_INDEX_VALUE = 0


class ProvisionManager():
    """
    ProvisionManager module manages system provisioning 

    Arguments: 
    system_configuration_manager: 
        Instance of SystemConfigurationManager 
    communication_manager:
        Instance of CommunicationManager
    """

    def __init__(self, system_configuration_manager, communication_manager):
        self.__logger = Logger.get_logger(__name__)
        self.__logger.info("ProvisionManager initializer starts")

        self.__system_provision_dict = {}
        self.__websocket_server_uri_dict = {}
        self.__websocket_server_uri = ""

        self.__system_upgrade_websocket_server_uri_dict = {}
        self.__system_upgrade_websocket_server_uri = ""

        self.__is_system_provisioned = False

        self.__system_configuration_manager = system_configuration_manager
        self.__communication_manager = communication_manager

        self.__system_provisioning_retry_event = threading.Event()

        if os.path.exists(SystemDefinitions.SYSTEM_PROVISION_PATH_NAME) and os.path.isfile(SystemDefinitions.SYSTEM_PROVISION_PATH_NAME):
            try:
                with open(SystemDefinitions.SYSTEM_PROVISION_PATH_NAME, SystemDefinitions.FILE_READ_MODE) as system_provision_file:
                    self.__system_provision_dict = json.load(system_provision_file)
                    self.__is_system_provisioned = self.__system_provision_dict[SystemDefinitions.PROVISIONING_STATUS_KEY]

                    if self.__system_provision_dict[SystemDefinitions.PROVISIONING_STATUS_KEY] == True:
                        self.__logger.info("Device already provisioned")
            except Exception as exception:
                self.__logger.error(exception)

        if os.path.exists(SystemDefinitions.WEBSOCKET_SERVER_URI_PATH_NAME) and os.path.isfile(SystemDefinitions.WEBSOCKET_SERVER_URI_PATH_NAME):
            try:
                with open(SystemDefinitions.WEBSOCKET_SERVER_URI_PATH_NAME, SystemDefinitions.FILE_READ_MODE) as websocket_server_uri_file:
                    self.__is_system_provisioned = True
                    self.__websocket_server_uri_dict = json.load(websocket_server_uri_file)
                    self.__update_provision_status()
                    self.__logger.info("Device already provisioned. Found websocket uri file")
            except Exception as exception:
                self.__logger.error(exception)
        else:
            self.__is_system_provisioned = False

        while self.__is_system_provisioned != True:
            if self.__device_provisioning() == True:
                self.__logger.info("Device provisioned successfully")
                break

            self.__system_provisioning_retry_event.wait(SystemDefinitions.PROVISIONING_RETRY_TIMEOUT)
            self.__logger.info("Retrying device proviosioning")

        # The below section will be modified by IPC mechanism. 
        # Notify the system upgrade application that deice is provisioned.
        if os.path.exists(SystemDefinitions.SYSTEM_UPGRADE_PID) == True:
            with open(SystemDefinitions.SYSTEM_UPGRADE_PID, SystemDefinitions.FILE_READ_MODE) as pid_file:
                systemUpgrade_pid = pid_file.read()

                try:
                    os.kill(int(systemUpgrade_pid), signal.SIGUSR1)
                except Exception as exception:
                    self.__logger.error(exception)

        self.__logger.info("ProvisionManager initializer ends")


    def __device_provisioning(self):
        response_data = b""
        response_status = False
        json_response_data_dict = {}
        post_request_dict = {}

        post_request_dict[SystemDefinitions.PROVISIONINS_DETAILS_KEY] = self.__system_configuration_manager.get_system_information()

        if os.path.exists(SystemDefinitions.CPE_VERSION_FILE_PATH) and os.path.isfile(SystemDefinitions.CPE_VERSION_FILE_PATH):
            try:
                with open(SystemDefinitions.CPE_VERSION_FILE_PATH, SystemDefinitions.FILE_READ_MODE) as version_file:
                    post_request_dict[SystemDefinitions.PROVISIONINS_DETAILS_KEY][SystemDefinitions.PACKAGE_VERSION_KEY] = version_file.read()

            except Exception as exception:
                self.__logger.error(exception)

        try:
            # Receiving response_data as byte stream
            response_data, response_status = self.__communication_manager.post_data_with_response(post_request_dict, self.__system_configuration_manager.get_provisioning_server_uri())
            # Decode the byte stream to string and load it as json
            json_response_data_dict = json.loads(response_data.decode(UTF8_DECODING_FORMAT))
        except Exception as exception:
            self.__logger.error(exception)

        if response_status == True:
            if SystemDefinitions.WEBSOCKET_SERVER_URI_KEY in json_response_data_dict:
                self.__websocket_server_uri = json_response_data_dict[SystemDefinitions.WEBSOCKET_SERVER_URI_KEY]
                self.__system_upgrade_websocket_server_uri = json_response_data_dict[SystemDefinitions.SYSTEMUPGRADE_SERVER_URI_KEY]
                self.__is_system_provisioned = True
                self.__update_websocket_uri()
                self.__update_system_upgrade_websocket_uri()
                self.__update_provision_status()
        else:
            if MessageDefinitions.ERROR_RESPONSE_MESSAGE_KEY in json_response_data_dict:    
                provision_error_response = json_response_data_dict[MessageDefinitions.ERROR_RESPONSE_MESSAGE_KEY]

                if provision_error_response[PROVISIONED_RESPONSE_ERROR_INDEX_VALUE] == MessageDefinitions.DEVICE_ALREADY_PROVISIONED_VALUE:
                    self.__is_system_provisioned = True
                    self.__update_provision_status()
                    self.__logger.info(provision_error_response[PROVISIONED_RESPONSE_ERROR_INDEX_VALUE])

                if provision_error_response[PROVISIONED_RESPONSE_ERROR_INDEX_VALUE] == MessageDefinitions.NO_DEVICE_FOUND_VALUE:
                    self.__is_system_provisioned = False
                    self.__logger.error(provision_error_response[PROVISIONED_RESPONSE_ERROR_INDEX_VALUE])
            else:
                self.__is_system_provisioned = False
                self.__logger.error("Device provisioning failed")

        return self.__is_system_provisioned

    def __update_system_upgrade_websocket_uri(self):
        with open(SystemDefinitions.SYSTEMUPGRADE_SERVER_URI_PATH_NAME, SystemDefinitions.FILE_WRITE_MODE) as system_upgrade_websocket_server_uri_file:
            self.__system_upgrade_websocket_server_uri_dict[SystemDefinitions.SYSTEMUPGRADE_SERVER_URI_KEY] = self.__system_upgrade_websocket_server_uri
            json.dump(self.__system_upgrade_websocket_server_uri_dict, system_upgrade_websocket_server_uri_file)

    def __update_websocket_uri(self):
        with open(SystemDefinitions.WEBSOCKET_SERVER_URI_PATH_NAME, SystemDefinitions.FILE_WRITE_MODE) as websocket_server_uri_file:
            self.__websocket_server_uri_dict[SystemDefinitions.WEBSOCKET_SERVER_URI_KEY] = self.__websocket_server_uri
            json.dump(self.__websocket_server_uri_dict, websocket_server_uri_file)


    def __update_provision_status(self):            
        with open(SystemDefinitions.SYSTEM_PROVISION_PATH_NAME, SystemDefinitions.FILE_WRITE_MODE) as system_provision_file:
            self.__system_provision_dict[SystemDefinitions.PROVISIONING_STATUS_KEY] = self.__is_system_provisioned
            json.dump(self.__system_provision_dict, system_provision_file)


    def get_websocket_server_uri(self):
        """
        Returns the websocket server URI as a string

        Args    - None
        Returns - string type - containing the websocket URI
        Raises  - ValueError : when the WebsocketServerUri.json does not contain the "websocket_server_uri" key present
        """

        websocket_server_uri = ""

        if SystemDefinitions.WEBSOCKET_SERVER_URI_KEY in self.__websocket_server_uri_dict:

            if self.__websocket_server_uri_dict[SystemDefinitions.WEBSOCKET_SERVER_URI_KEY] != {}:
                websocket_server_uri = self.__websocket_server_uri_dict[SystemDefinitions.WEBSOCKET_SERVER_URI_KEY]
        else:
            self.__logger.exception("WebsocketServerUri.json does not contain websocket_server_uri key")
            # WebsocketServerUri is a critical information which is manadatory parameter without which CPE can not function. 
            raise ValueError

        return websocket_server_uri