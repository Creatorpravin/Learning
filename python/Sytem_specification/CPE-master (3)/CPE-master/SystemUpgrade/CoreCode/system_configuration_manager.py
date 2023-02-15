import json
import os

import CoreCode.logger as Logger
import Definitions.system_definitions as SystemDefinitions
import Definitions.message_definitions as MessageDefinitions


class SystemConfigurationManager:
    """
    This module is used to fetch and modify the SystemConfiguration.json
    """

    def __init__(self):
        self.__logger = Logger.get_logger(logger_name=__name__)
        self.__logger.info("SystemConfigurationManager initializer start")

        if os.path.exists(SystemDefinitions.SYS_CONFIG_FILE_PATH_NAME) and os.path.isfile(SystemDefinitions.SYS_CONFIG_FILE_PATH_NAME):
            with open(SystemDefinitions.SYS_CONFIG_FILE_PATH_NAME, SystemDefinitions.FILE_READ_MODE) as configuration_file:
                try:
                    self.__system_configuration = json.load(configuration_file)
                    self.__system_information = self.__system_configuration[SystemDefinitions.SYSTEM_INFORMATION_KEY]
                except Exception as exception:
                    # The exception is re-raised instead of catching as the SystemConfiguration.json is a critical component of the CPE Application
                    raise exception
        else:
            self.__logger.exception("SystemConfiguration.json file/path does not exist")
            raise FileNotFoundError

        self.__logger.info("SystemConfigurationManager initializer end")


    def get_device_id(self):
        """
        Returns the device id as a string

        Args    - None
        Returns - string type - containing the DeviceID
        Raises  - ValueError : when the SystemConfiguration.json does not have the "DeviceID" key present
        """
        device_id = str()

        if SystemDefinitions.DEVICE_UUID_KEY in self.__system_information:
            if self.__system_information[SystemDefinitions.DEVICE_UUID_KEY] != "":
                device_id = self.__system_information[SystemDefinitions.DEVICE_UUID_KEY]
            else:
                device_id = "NA"
        else:
            self.__logger.exception("SystemConfiguration.json does not contain DeviceID key")
            raise ValueError

        return device_id


    def get_system_information(self):
        """
        Returns the system information as a dict

        Args    - None
        Returns - dict with following contents - mac_address, os_version, model, device_id, lan_interfaces, wan_interfaces
        Raises  - ValueError : when the SystemConfiguration.json does not have the "system_information" key present
        """
        system_information_dict = {}

        if SystemDefinitions.SYSTEM_INFORMATION_KEY in self.__system_configuration:
            if self.__system_configuration[SystemDefinitions.SYSTEM_INFORMATION_KEY] != {}:
                system_information_dict = self.__system_configuration[SystemDefinitions.SYSTEM_INFORMATION_KEY]
        else:
            self.__logger.exception("SystemConfiguration.json does not contain system_information key")
            raise ValueError

        return system_information_dict


    def get_provisioning_server_uri(self):
        """
        Returns the provision_server URI as a string

        Args    - None
        Returns - string type - containing the websocket URI
        Raises  - ValueError : when the SystemConfiguration.json does not have the "provision_server_uri" key present
        """
        provision_server_uri = ""

        if SystemDefinitions.PROVISIONING_SERVER_URI_KEY in self.__system_configuration:
            if self.__system_configuration[SystemDefinitions.PROVISIONING_SERVER_URI_KEY] != {}:
                provision_server_uri = self.__system_configuration[SystemDefinitions.PROVISIONING_SERVER_URI_KEY]
        else:
            self.__logger.exception("SystemConfiguration.json does not contain provision_server_uri key")
            raise ValueError

        return provision_server_uri