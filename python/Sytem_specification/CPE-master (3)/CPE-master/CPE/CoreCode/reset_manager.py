import keyboard
import os

import CoreCode.service_manager_helper_functions as ServiceManagerHelperFunction
import CoreCode.service_manager_linux_helper_functions as ServiceManagerLinuxHelperFunction
import Definitions.system_definitions as SystemDefinition
import CoreCode.logger as Logger

NETPLAN_COMMAND_PREFIX = "netplan"
NETPLAN_DEBUG_OPTION = "--debug"
NETPLAN_GENERATE_SUFFIX = "generate"
NETPLAN_APPLY_SUFFIX = "apply"

PATH_SEPERATOR_CHARACTER = os.path.sep
SPACE_CHARACTER = " "

# Hotkey definitions
RESET_NETWORK_INTERFACE_HOTKEY = "alt + shift + i"

class ResetManager():
    """
    ResetManager is used for resetting the various components of the CPE device
    """

    def __init__(self):
        self.__logger = Logger.get_logger(logger_name=__name__)
         
        self.__logger.info("ResetNetworkConfigurationManager initializer starts")

        # Register the hotkey with the keyboard module
        keyboard.add_hotkey(RESET_NETWORK_INTERFACE_HOTKEY, self.__reset_network_interface)

        self.__logger.info("ResetNetworkConfigurationManager initializer ends")


    def __reset_network_interface(self):
        factory_default_network_config_source_file = SystemDefinition.NETWORK_INTERFACE_FACTORY_RESET_FOLDER_PATH + PATH_SEPERATOR_CHARACTER + SystemDefinition.NETWORK_INTERFACE_CONFIG_YAML_FILE_NAME
            
        if os.path.exists(factory_default_network_config_source_file) != True:
            self.__logger.error("{} path not found".format(factory_default_network_config_source_file))
            return False

        if ServiceManagerHelperFunction.clear_directory(directory_to_be_cleared=SystemDefinition.NETWORK_INTERFACE_CONFIG_FOLDER_PATH,logger_object=self.__logger) == True:            
            if ServiceManagerHelperFunction.copy_file(source_filepath=factory_default_network_config_source_file, 
                                                    destination_filepath=SystemDefinition.NETWORK_INTERFACE_CONFIG_FOLDER_PATH, 
                                                    logger_object=self.__logger) != True:
                self.__logger.error("Failed to copy network interface file")
                return False
        else:
            self.__logger.error("Failed to clear /etc/netplan/ directory")
            return False
        
        if self.__apply_network_interface_configuration() != True:
            self.__logger.error("Failed to apply default network interface configuration")
            return False
        
        self.__logger.info("Successfully configured factory default network interface configuration")

        return True


    def __apply_network_interface_configuration(self):

        netplan_generate_command = NETPLAN_COMMAND_PREFIX + SPACE_CHARACTER + NETPLAN_DEBUG_OPTION + SPACE_CHARACTER + NETPLAN_GENERATE_SUFFIX
        netplan_apply_command = NETPLAN_COMMAND_PREFIX + SPACE_CHARACTER + NETPLAN_DEBUG_OPTION + SPACE_CHARACTER + NETPLAN_APPLY_SUFFIX
        
        if ServiceManagerLinuxHelperFunction.execute_linux_command(command=netplan_generate_command, logger_object=self.__logger) == True:
            if ServiceManagerLinuxHelperFunction.execute_linux_command(command=netplan_apply_command, logger_object=self.__logger) != True:
                self.__logger.error("Failed to execute netplan apply command")
                return False
        else:
            self.__logger.error("Failed to execute netplan generate command")
            return False

        self.__logger.info("Successfully applied network interface configuration")

        return True
