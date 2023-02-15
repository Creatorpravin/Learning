import os
import string

import CoreCode.logger as Logger
import Definitions.system_definitions as SystemDefinitions

QUERY_SYMBOL = "?"
DEVICE_ID_KEY = "device_id"
EQUALTO_SYMBOL = "="
AMPERSAND_SYMBOL = "&"
CPE_APP_PACKAGE_VERSION_KEY = "cpe_app_package_version"


class URIManager:
    """
    This module is used to frame the system upgrade websocket uri.

    Arguments:
    websocket_server_base_uri:
        Argument of type string, which consists of websocket server base URI
    cpe_version_file_path:
        Argument of type string, which consists of CPE version file path
    system_configuration_manager:
        Instance of SystemConfigurationManager
    """

    def __init__(self, websocket_server_base_uri, cpe_version_file_path, system_configuration_manager):
        self.__logger = Logger.get_logger(__name__)
        self.__logger.info("URIManager initialization start")

        self.__websocket_server_base_uri = websocket_server_base_uri
        self.__cpe_version_file_path = cpe_version_file_path
        self.__device_id = system_configuration_manager.get_device_id()

        self.__logger.info("URIManager initialization end")


    def get_server_connection_uri(self):
        """
        Returns the system upgrade websocket uri as a string.

        Args    - None
        Returns - string type - containing the system upgrade websocket uri
        """

        if os.path.exists(self.__cpe_version_file_path) and os.path.isfile(self.__cpe_version_file_path):
            try:
                with open(self.__cpe_version_file_path, SystemDefinitions.FILE_READ_MODE) as version_file:
                    cpe_version_file_content = version_file.read().strip()

                    if cpe_version_file_content in string.whitespace:
                        cpe_version = "NoVersionFound"
                    else:
                        cpe_version = cpe_version_file_content
            except Exception as exception:
                cpe_version = "FileReadError"
                self.__logger.error(exception)
        else:
            cpe_version = "FileNotFound"
            self.__logger.error("Failed to get cpe version information")

        websocket_server_uri = self.__websocket_server_base_uri + QUERY_SYMBOL + \
                                DEVICE_ID_KEY + EQUALTO_SYMBOL + self.__device_id + \
                                AMPERSAND_SYMBOL + CPE_APP_PACKAGE_VERSION_KEY + EQUALTO_SYMBOL + cpe_version

        return websocket_server_uri
