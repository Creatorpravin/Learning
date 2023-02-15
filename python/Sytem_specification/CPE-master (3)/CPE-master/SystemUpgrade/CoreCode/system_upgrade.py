import os
import json

import CoreCode.logger as Logger
import CoreCode.service_manager_linux_helper_functions as LinuxHelperFunctions
import Definitions.message_definitions as MessageDefinitions
import Definitions.message_code_definitions as MessageCodeDefinition
import Definitions.system_definitions as SystemDefinitions
import Definitions.message_definitions as MessageDefinitions

SPACE_CHARACTER = " "
NEW_LINE_CHARACTER = "\n"

RECEIVED_SYSTEM_UPGRADE_NOTIFICATION = "Received system upgrade message"
SYSTEM_UPGRADE_SUCCESSFUL_NOTIFICATION = "System upgraded successfully"
SYSTEM_UPDATED_PACKAGE_LIST_UPDATED_SUCCESSFULLY_NOTIFICATION = "System update package list updated"
RECEIVED_SYSTEM_UPGRADE_PACKAGE_NOTIFICATION = "System upgrade package received successfully"
SYSTEM_UPGRADE_PACKAGE_INSTALLED_SUCCESSFULLY_NOTIFICATION = "System upgrade package installed successfully"
SYSTEM_UPDATED_PACKAGE_LIST_UPDATE_FAILED_NOTIFICATION = "Failed to update package list"
FAILED_TO_UPGRADE_PYTHON_DEPENDENT_MODULES_NOTIFICATION = "Failed to install CPE dependent python modules"
FAILED_TO_INSTALL_DEPENDENT_SYSTEM_UTILITES_NOTIFICATION = "Failed to install CPE dependent system utility"
FAILED_TO_INSTALL_CHIEFNET_ROLLBACK_VERSION_NOTIFICATION = "Failed to install chiefnet rollback version"
ROLLING_BACK_CHIEFNET_APPLICATION_NOTIFICATION = "Rolling back chiefnet application"
CHIEFNET_ROLLBACK_VERSION_NOT_FOUND_NOTIFICATION = "Rollback version for the chiefnet application is not present"

FAILED_TO_RECEIVE_SYSTEM_UPGRADE_PACKAGE_NOTIFICATION = "Failed to system update  receive package"
FAILED_TO_INSTALL_SYSTEM_UPGRADE_PACKAGE_NOTIFICATION = "Failed to install system upgrade package"
FAILED_TO_STOP_CHIEFNET_SERVICE_NOTIFICATION = "Failed to stop chiefnet service"
FAILED_TO_START_CHIEFNET_SERVICE_NOTIFICATION = "Failed to start chiefnet service"
FAILED_TO_GET_CPE_VERSION_NOTIFICATION = "Failed to get cpe version information"

class SystemUpgrade():
    """
    SystemUpgrade is used to upgrade system packages

    Arguments:
    response_manager:
        An instance of ResponseManager must be passed to send responses to the WebApp
    """

    def __init__(self, response_manager):
        self.__logger = Logger.get_logger(logger_name=__name__)

        self.__logger.info("SystemUpgrade initializer starts")
        
        self._response_manager = response_manager

        self.__logger.info("SystemUpgrade initializer ends")


    def system_upgrade_request_callback(self, system_upgrade_request_message):
        """
        system_upgrade_request_callback preform the upgrade process for the package with the version specified in 
        the system upgrade request message 

        Args    - System upgrade request message from server
        Returns - True  - If system upgrade process is success
                  False - If system upgrade process is failed          
        """ 
        self._response_manager.send_response(message=system_upgrade_request_message, 
                                                status_code=MessageCodeDefinition.RECEIVED_SYSTEM_UPGRADED_MESSAGE,
                                                status_message=RECEIVED_SYSTEM_UPGRADE_NOTIFICATION)

        self.__system_upgrade_request_message = system_upgrade_request_message

        return self.__perform_system_upgrade()


    def __perform_system_upgrade(self):
        self.__logger.info("Performing system upgrade")

        if self.__stop_chiefnet_service() != True:
            return False

        if self.__update_package_list() != True:
            if self.__start_chiefnet_service() != True:
                return False
            
            if self.__send_chiefnet_version_to_server() != True:
                return False

            return False

        chiefnet_version = ""

        if MessageDefinitions.PACKAGE_VERSION_KEY in self.__system_upgrade_request_message[MessageDefinitions.CONTENT_KEY]:
            chiefnet_version = self.__system_upgrade_request_message[MessageDefinitions.CONTENT_KEY][MessageDefinitions.PACKAGE_VERSION_KEY]

        if self.__install_chiefnet_application(chiefnet_version) != True:
            self._response_manager.send_response(message=self.__system_upgrade_request_message, 
                                    status_code=MessageCodeDefinition.ROLLING_BACK_CHIEFNET_APPLICATION,
                                    status_message=ROLLING_BACK_CHIEFNET_APPLICATION_NOTIFICATION)
            self.__logger.info(ROLLING_BACK_CHIEFNET_APPLICATION_NOTIFICATION)

            chiefnet_rollback_version = ""

            if MessageDefinitions.ROLLBACK_PACKAGE_VERSION_KEY in self.__system_upgrade_request_message[MessageDefinitions.CONTENT_KEY]:
                chiefnet_rollback_version = self.__system_upgrade_request_message[MessageDefinitions.CONTENT_KEY][MessageDefinitions.ROLLBACK_PACKAGE_VERSION_KEY]

                if self.__install_chiefnet_application(chiefnet_rollback_version) != True:
                    self._response_manager.send_response(message=self.__system_upgrade_request_message, 
                                                    status_code=MessageCodeDefinition.FAILED_TO_INSTALL_CHIEFNET_ROLLBACK_VERSION,
                                                    status_message=FAILED_TO_INSTALL_CHIEFNET_ROLLBACK_VERSION_NOTIFICATION)
                    self.__logger.error(FAILED_TO_INSTALL_CHIEFNET_ROLLBACK_VERSION_NOTIFICATION)
                    return False
            else:
                self._response_manager.send_response(message=self.__system_upgrade_request_message, 
                                                    status_code=MessageCodeDefinition.CHIEFNET_ROLLBACK_VERSION_NOT_FOUND,
                                                    status_message=CHIEFNET_ROLLBACK_VERSION_NOT_FOUND_NOTIFICATION)
                self.__logger.error(CHIEFNET_ROLLBACK_VERSION_NOT_FOUND_NOTIFICATION)
                return False

        if self.__start_chiefnet_service() != True:
            return False

        if self.__send_chiefnet_version_to_server() != True:
            return False

        self.__logger.info(SYSTEM_UPGRADE_SUCCESSFUL_NOTIFICATION)

        return True


    def __install_chiefnet_application(self, version):
        if self.__upgrade_chiefnet_application(version) != True:
            return False

        if self.__upgrade_utilities() != True:
            return False

        if self.__upgrade_python_modules() != True:
            return False

        return True


    def __upgrade_chiefnet_application(self, version):
        chiefnet_package_name = self.__system_upgrade_request_message[MessageDefinitions.CONTENT_KEY][MessageDefinitions.PACKAGE_KEY]

        if LinuxHelperFunctions.install_package(chiefnet_package_name, version, logger_object=self.__logger) == True:
            self._response_manager.send_response(message=self.__system_upgrade_request_message, 
                                                status_code=MessageCodeDefinition.SYSTEM_UPGRADE_PACKAGE_INSTALLED_SUCCESSFULLY,
                                                status_message=SYSTEM_UPGRADE_PACKAGE_INSTALLED_SUCCESSFULLY_NOTIFICATION)
            self.__logger.info(SYSTEM_UPGRADE_PACKAGE_INSTALLED_SUCCESSFULLY_NOTIFICATION)
        else:
            self._response_manager.send_response(message=self.__system_upgrade_request_message, 
                                                status_code=MessageCodeDefinition.FAILED_TO_INSTALL_SYSTEM_UPGRADE_PACKAGE,
                                                status_message=FAILED_TO_INSTALL_SYSTEM_UPGRADE_PACKAGE_NOTIFICATION)
            self.__logger.error(FAILED_TO_INSTALL_SYSTEM_UPGRADE_PACKAGE_NOTIFICATION)
            return False

        return True


    def __upgrade_utilities(self):
        # Installing system utilities
        if os.path.exists(SystemDefinitions.SYSTEM_UPGRADE_JSON_FILE_PATH) == True:
            self.__logger.info("Installing system dependent modules for CPE")

            with open(SystemDefinitions.SYSTEM_UPGRADE_JSON_FILE_PATH, SystemDefinitions.FILE_READ_MODE) as system_upgrade_json:
                try:
                    package_list = json.load(system_upgrade_json)
                except ValueError as value_error:
                    self.__logger.error(value_error)
                    return False

            utilities_package_list = package_list[SystemDefinitions.SYSTEM_UPGRADE_UTILITIES_KEY]

            for utility_package in utilities_package_list:
                utility_package_version = ""
                utility_package_name = utility_package[SystemDefinitions.SYSTEM_UPGRADE_UTILITIES_PACKAGE_KEY]
                
                if SystemDefinitions.SYSTEM_UPGRADE_UTILITIES_VERSION_KEY in utility_package:
                    utility_package_version = utility_package[SystemDefinitions.SYSTEM_UPGRADE_UTILITIES_VERSION_KEY]

                if LinuxHelperFunctions.install_package(utility_package_name, utility_package_version, logger_object=self.__logger) != True:
                    utility_install_failed_error_message = FAILED_TO_INSTALL_DEPENDENT_SYSTEM_UTILITES_NOTIFICATION + SPACE_CHARACTER \
                                                + utility_package_name \
                                                + SPACE_CHARACTER + utility_package_version

                    self._response_manager.send_response(message=self.__system_upgrade_request_message, 
                                                        status_code=MessageCodeDefinition.FAILED_TO_INSTALL_DEPENDENT_SYSTEM_UTILITY,
                                                        status_message=utility_install_failed_error_message)
                    self.__logger.error(utility_install_failed_error_message)

                    return False
                else:
                    self.__logger.info("Installed - {}".format(utility_package[SystemDefinitions.SYSTEM_UPGRADE_UTILITIES_PACKAGE_KEY]) )
        else:
            self.__logger.info("No SystemUpgrade.json found") 

        return True


    def __upgrade_python_modules(self):
        # Installing python modules
        if os.path.exists(SystemDefinitions.PYTHON_REQUIREMENTS_FILE_PATH) == True:
            self.__logger.info("Installing python dependent modules for CPE")

            if LinuxHelperFunctions.execute_script(filepath=SystemDefinitions.PYTHON_UPGRADE_SCRIPT, logger_object=self.__logger) != True:
                self._response_manager.send_response(message=self.__system_upgrade_request_message, 
                                                    status_code=MessageCodeDefinition.FAILED_TO_UPGRADE_PYTHON_DEPENDENT_MODULES,
                                                    status_message=FAILED_TO_UPGRADE_PYTHON_DEPENDENT_MODULES_NOTIFICATION)
                self.__logger.error(FAILED_TO_UPGRADE_PYTHON_DEPENDENT_MODULES_NOTIFICATION)

                return False
            else:
                self.__logger.info("Installed python dependent modules for CPE")
        else:
            self.__logger.info("No requirements.txt found")              
        
        return True


    def __update_package_list(self):
        if LinuxHelperFunctions.update_package_list(logger_object=self.__logger) == True:
            self._response_manager.send_response(message=self.__system_upgrade_request_message, 
                                                status_code=MessageCodeDefinition.SYSTEM_UPDATED_PACKAGE_LIST_UPDATED_SUCCESSFULLY,
                                                status_message=SYSTEM_UPDATED_PACKAGE_LIST_UPDATED_SUCCESSFULLY_NOTIFICATION)
            self.__logger.info(SYSTEM_UPDATED_PACKAGE_LIST_UPDATED_SUCCESSFULLY_NOTIFICATION)
        else:
            self._response_manager.send_response(message=self.__system_upgrade_request_message, 
                                                status_code=MessageCodeDefinition.SYSTEM_UPDATED_PACKAGE_LIST_UPDATE_FAILED,
                                                status_message=SYSTEM_UPDATED_PACKAGE_LIST_UPDATE_FAILED_NOTIFICATION)
            self.__logger.error(SYSTEM_UPDATED_PACKAGE_LIST_UPDATE_FAILED_NOTIFICATION)

            return False

        return True


    def __start_chiefnet_service(self):
        if LinuxHelperFunctions.start_system_service(service_name=SystemDefinitions.CHIEFNET_SERVICE, logger_object=self.__logger) != True:
            self._response_manager.send_response(message=self.__system_upgrade_request_message, 
                                                status_code=MessageCodeDefinition.FAILED_TO_START_CHIEFNET_SERVICE,
                                                status_message=FAILED_TO_START_CHIEFNET_SERVICE_NOTIFICATION)
            self.__logger.error(FAILED_TO_START_CHIEFNET_SERVICE_NOTIFICATION)

            return False
        else:
            self.__logger.info("Starting chiefnet service")

        return True


    def __stop_chiefnet_service(self):
        if LinuxHelperFunctions.stop_system_service(service_name=SystemDefinitions.CHIEFNET_SERVICE, logger_object=self.__logger) == True:
            self.__logger.info("Chiefnet service stopped")
        else:
            self._response_manager.send_response(message=self.__system_upgrade_request_message, 
                                                status_code=MessageCodeDefinition.FAILED_TO_STOP_CHIEFNET_SERVICE,
                                                status_message=FAILED_TO_STOP_CHIEFNET_SERVICE_NOTIFICATION)
            self.__logger.error(FAILED_TO_STOP_CHIEFNET_SERVICE_NOTIFICATION)

            return False

        return True


    def __send_chiefnet_version_to_server(self):
        if os.path.exists(SystemDefinitions.CPE_VERSION_FILE_PATH) and os.path.isfile(SystemDefinitions.CPE_VERSION_FILE_PATH):
            try:
                with open(SystemDefinitions.CPE_VERSION_FILE_PATH, SystemDefinitions.FILE_READ_MODE) as version_file:
                    cpe_version = version_file.read()
                    self._response_manager.send_response(message=self.__system_upgrade_request_message, 
                                status_code=MessageCodeDefinition.SYSTEM_UPGRADED_SUCCESSFULLY,
                                status_message=cpe_version)
            except Exception as exception:
                self.__logger.error(exception)
        else:
            self._response_manager.send_response(message=self.__system_upgrade_request_message, 
                                status_code=MessageCodeDefinition.FAILED_TO_GET_CPE_VERSION,
                                status_message=FAILED_TO_GET_CPE_VERSION_NOTIFICATION)
            self.__logger.error(FAILED_TO_GET_CPE_VERSION_NOTIFICATION)
            
            return False

        return True
