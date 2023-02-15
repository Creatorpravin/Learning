import os
import sys
import shutil

import CoreCode.logger as Logger
import Definitions.message_code_definitions as MessageCodeDefinition
import Definitions.system_definitions as SystemDefinition
import CoreCode.service_manager_helper_functions as ServiceManagerHelperFunction
import CoreCode.service_manager_linux_helper_functions as ServiceManagerLinuxHelperFunction
from CoreCode.service_manager import ServiceManager

RECEIVED_DELETE_DEVICE_NOTIFICATION = "Received delete device message"
DEVICE_DELETED_SUCCESSFULLY_NOTIFICATION = "Device deleted successfully"
FAILED_TO_RESET_USER_CONFIG_NOTIFICATION = "Device failed to reset user configuration"
FAILED_TO_RESET_NETWORK_INTERFACE_CONFIG_NOTIFICATION = "Device failed to reset network interface configuration"
FAILED_TO_RESET_SYSTEM_PROVISIONING_CONFIG_NOTIFICATION = "Device failed to reset system provisioning configuration"
FAILED_TO_RESET_DNSMASQ_CONFIG_NOTIFICATION = "Device failed to reset dnsmasq configuration"
FAILED_TO_RESET_OPENVPN_AND_ROUTING_CONFIG_NOTIFICATION = "Device failed to reset openvpn and routing configuration"

OPENVPN_SERVICE_NAME = "openvpn.service"
DNSMASQ_SERVICE_NAME = "dnsmasq.service"
FRR_SERVICE_NAME = "frr.service"

PATH_SEPERATOR_CHARACTER = os.path.sep
SPACE_CHARACTER = " "
TRAFFIC_STEERING_CONFIGURATION_FILE_DIRECTORY = "traffic-steering-configuration"
FRR_OWNERSHIP_NAME = "frr"

NETPLAN_COMMAND_PREFIX = "netplan"
NETPLAN_DEBUG_OPTION = "--debug"
NETPLAN_GENERATE_SUFFIX = "generate"
NETPLAN_APPLY_SUFFIX = "apply"
IPTABLES_RESTORE_COMMAND = "iptables-restore"
INPUT_REDIRECTION_OPERATOR = "<"
IPTABLES_CONFIG_FILE_NAME = "initial-configuration.txt"

PYTHON_COMMAND = "python"


class DeleteDeviceManager(ServiceManager):
    """
    DeleteDeviceManager is derived from ServiceManager and is used to detach the device from the web application
    portal by reseting device configuration and get the CPE device tp provisioning state.
    Arguments:
    data_manager:
        An instance of DataManager must be passed.
    response_manager:
        An instance of ResponseManager must be passed to send responses to the WebApp
    """
    def __init__(self, data_manager, response_manager):
        self.__logger = Logger.get_logger(__name__)
        self.__logger.info("DeleteDeviceManager initializer starts")

        event_dictionary = {}
        event_dictionary[MessageCodeDefinition.DEVICE_DELETE_EVENT] = self.__delete_device_event_routine

        self._response_manager = response_manager

        ServiceManager.__init__(self, data_manager=data_manager, response_manager=response_manager, event_dictionary=event_dictionary)      
        
        self.__logger.info("DeleteDeviceManager initializer ends")


    def __delete_device_event_routine(self):
        self.__logger.info("Delete device event routine start")
        self._response_manager.send_response(message=self._message_dictionary, 
                                                status_code=MessageCodeDefinition.RECEIVED_DELETE_DEVICE_MESSAGE,
                                                status_message=RECEIVED_DELETE_DEVICE_NOTIFICATION)

        if self.__reset_config() == True:
            if ServiceManagerLinuxHelperFunction.restart_system_service(service_name=SystemDefinition.SYSTEM_UPGRADE_SERVICE, logger_object=self.__logger) != True:
                self.__logger.error("Failed to restart system upgrade service")
                return False

            self._response_manager.send_response(message=self._message_dictionary, 
                                                status_code=MessageCodeDefinition.SUCCESSFULLY_DELETED_DEVICE,
                                                status_message=DEVICE_DELETED_SUCCESSFULLY_NOTIFICATION)

            if self.__restart_network_interface_config() != True:
                self.__logger.error("Failed to restart network interface configuration")
                return False
            
            self.__logger.info("Device deleted successfully.Relaunching CPE application")
            
            try:
                os.execv(sys.executable, [PYTHON_COMMAND] + [sys.argv[0]])
            except OSError as os_error:
                self.__logger.error(os_error)
                # TBD -- Figureout what to do if relaunch failed
                return False
        else:
            self.__logger.error("Device deletion failed")
            return False


    def __reset_config(self):
        if os.path.exists(SystemDefinition.FACTORY_RESET_FOLDER_PATH) != True:
            self.__logger.error(SystemDefinition.FACTORY_RESET_FOLDER_PATH, " path not found")
            return False

        if self.__reset_network_interface_config() == False:
            self._response_manager.send_response(message=self._message_dictionary, 
                                                status_code=MessageCodeDefinition.FAILED_TO_RESET_NETWORK_INTERFACE_CONFIG,
                                                status_message=FAILED_TO_RESET_NETWORK_INTERFACE_CONFIG_NOTIFICATION)

            self.__logger.error(FAILED_TO_RESET_NETWORK_INTERFACE_CONFIG_NOTIFICATION)
            return False

        if self.__reset_dnsmasq_config() == False:
            self._response_manager.send_response(message=self._message_dictionary, 
                                                status_code=MessageCodeDefinition.FAILED_TO_RESET_DNSMASQ_CONFIG,
                                                status_message=FAILED_TO_RESET_DNSMASQ_CONFIG_NOTIFICATION)

            self.__logger.error(FAILED_TO_RESET_DNSMASQ_CONFIG_NOTIFICATION)
            return False

        if self.__reset_openvpn_and_frr_config() == False:
            self._response_manager.send_response(message=self._message_dictionary, 
                                                status_code=MessageCodeDefinition.FAILED_TO_RESET_OPENVPN_AND_ROUTING_CONFIG,
                                                status_message=FAILED_TO_RESET_OPENVPN_AND_ROUTING_CONFIG_NOTIFICATION)
            
            self.__logger.error(FAILED_TO_RESET_OPENVPN_AND_ROUTING_CONFIG_NOTIFICATION)
            return False

        if self.__reset_user_config() == False:
            self._response_manager.send_response(message=self._message_dictionary, 
                                                status_code=MessageCodeDefinition.FAILED_TO_RESET_USER_CONFIG,
                                                status_message=FAILED_TO_RESET_USER_CONFIG_NOTIFICATION)

            self.__logger.error(FAILED_TO_RESET_USER_CONFIG_NOTIFICATION)
            return False

        if self.__reset_provision_config() == False:
            self._response_manager.send_response(message=self._message_dictionary, 
                                                status_code=MessageCodeDefinition.FAILED_TO_RESET_SYSTEM_PROVISIONING_CONFIG,
                                                status_message=FAILED_TO_RESET_SYSTEM_PROVISIONING_CONFIG_NOTIFICATION)

            self.__logger.error(FAILED_TO_RESET_SYSTEM_PROVISIONING_CONFIG_NOTIFICATION)
            return False

        return True


    def __reset_provision_config(self):
        if ServiceManagerHelperFunction.remove_file_if_exists(filepath=SystemDefinition.WEBSOCKET_SERVER_URI_PATH_NAME, logger_object=self.__logger) != True:
            self.__logger.error("Failed to remove Websocket_server_uri.json file")
            return False

        if ServiceManagerHelperFunction.remove_file_if_exists(filepath=SystemDefinition.SYSTEMUPGRADE_SERVER_URI_PATH_NAME, logger_object=self.__logger) != True:
            self.__logger.error("Failed to remove SystemUpgradeServerUri.json file")
            return False
        
        if ServiceManagerHelperFunction.remove_file_if_exists(filepath=SystemDefinition.SYSTEM_PROVISION_PATH_NAME, logger_object=self.__logger) != True:
            self.__logger.error("Failed to remove SystemProvision.json file")
            return False

        return True


    def __reset_network_interface_config(self):
        factory_default_network_config_source_file = SystemDefinition.NETWORK_INTERFACE_FACTORY_RESET_FOLDER_PATH + PATH_SEPERATOR_CHARACTER + SystemDefinition.NETWORK_INTERFACE_CONFIG_YAML_FILE_NAME
        
        if os.path.exists(factory_default_network_config_source_file) != True:
            self.__logger.error("{} path not found".format(factory_default_network_config_source_file))
            return False
    
        if ServiceManagerHelperFunction.clear_directory(directory_to_be_cleared=SystemDefinition.NETWORK_INTERFACE_CONFIG_FOLDER_PATH, logger_object=self.__logger) == True:            
            if ServiceManagerHelperFunction.copy_file(source_filepath=factory_default_network_config_source_file, 
                                                    destination_filepath=SystemDefinition.NETWORK_INTERFACE_CONFIG_FOLDER_PATH, 
                                                    logger_object=self.__logger) != True:
                self.__logger.error("Failed to copy network interface file")
                return False
        else:
            self.__logger.error("Failed to clear /etc/netplan/ directory")
            return False
   
        return True


    def __restart_network_interface_config(self):
        netplan_generate_command = NETPLAN_COMMAND_PREFIX + SPACE_CHARACTER + NETPLAN_DEBUG_OPTION + SPACE_CHARACTER + NETPLAN_GENERATE_SUFFIX
        netplan_apply_command = NETPLAN_COMMAND_PREFIX + SPACE_CHARACTER + NETPLAN_DEBUG_OPTION + SPACE_CHARACTER + NETPLAN_APPLY_SUFFIX
        
        if ServiceManagerLinuxHelperFunction.execute_linux_command(command=netplan_generate_command, logger_object=self.__logger) == True:
            if ServiceManagerLinuxHelperFunction.execute_linux_command(command=netplan_apply_command, logger_object=self.__logger) != True:
                self.__logger.error("Failed to execute netplan apply command")
                return False
        else:
            self.__logger.error("Failed to execute netplan generate command")
            return False
        
        return True


    def __reset_dnsmasq_config(self):
        factory_default_dnsmasq_config_source_file = SystemDefinition.DNSMASQ_FACTORY_RESET_FOLDER_PATH + PATH_SEPERATOR_CHARACTER + SystemDefinition.DNSMASQ_CONFIG_FILE_NAME

        if os.path.exists(factory_default_dnsmasq_config_source_file) != True:
            self.__logger.error("{} path not found".format(factory_default_dnsmasq_config_source_file))
            return False

        if ServiceManagerHelperFunction.clear_directory(directory_to_be_cleared=SystemDefinition.DNSMASQ_CONFIG_FOLDER_PATH, logger_object=self.__logger) == True:
            dnsmasq_config_destination_file_path = SystemDefinition.DNSMASQ_CONFIG_FOLDER_PATH + PATH_SEPERATOR_CHARACTER + SystemDefinition.DNSMASQ_CONFIG_FILE_NAME

            if ServiceManagerHelperFunction.copy_file(source_filepath=factory_default_dnsmasq_config_source_file, 
                                                    destination_filepath=dnsmasq_config_destination_file_path, 
                                                    logger_object=self.__logger) == True:
                if ServiceManagerLinuxHelperFunction.restart_system_service(service_name=DNSMASQ_SERVICE_NAME, logger_object=self.__logger) != True:
                    self.__logger.error("Failed to restart dnsmasq service")
                    return False 
            else:
                self.__logger.error("Failed to copy dnsmasq configuration file")
                return False
        else:
            self.__logger.error("Failed to clear /etc/dnsmasq.d/ directory")
            return False
    
        return True


    def __reset_openvpn_and_frr_config(self):
        if os.path.exists(SystemDefinition.OPENVPN_FACTORY_RESET_FOLDER_PATH) != True:
            self.__logger.error("{} path not found".format(SystemDefinition.OPENVPN_FACTORY_RESET_FOLDER_PATH))
            return False

        if os.path.exists(SystemDefinition.OPENVPN_CONFIG_FOLDER_PATH):
            if ServiceManagerHelperFunction.remove_file_if_exists(filepath=SystemDefinition.OPENVPN_CONFIG_FOLDER_PATH + PATH_SEPERATOR_CHARACTER + SystemDefinition.VPN_UP_FILE_NAME, logger_object=self.__logger) != True:
                self.__logger.error("Failed to remove vpn-up.sh file")
                return False

            if ServiceManagerHelperFunction.remove_file_if_exists(filepath=SystemDefinition.OPENVPN_CONFIG_FOLDER_PATH + PATH_SEPERATOR_CHARACTER + SystemDefinition.VPN_DOWN_FILE_NAME, logger_object=self.__logger) != True:
                self.__logger.error("Failed to remove vpn-down.sh file")
                return False

            for filename in os.listdir(SystemDefinition.OPENVPN_CONFIG_FOLDER_PATH):
                if SystemDefinition.OPENVPN_FILE_EXTENSION in filename:
                    filepath = SystemDefinition.OPENVPN_CONFIG_FOLDER_PATH + PATH_SEPERATOR_CHARACTER + str(filename)
                    if ServiceManagerHelperFunction.remove_file_if_exists(filepath=filepath, logger_object=self.__logger) != True:
                        self.__logger.error("Failed to remove ", filename, " file")
                        return False

            if ServiceManagerLinuxHelperFunction.restart_system_service(service_name=OPENVPN_SERVICE_NAME, logger_object=self.__logger) != True:
                self.__logger.error("Failed to restart openvpn service")
                return False
        else:
            self.__logger.error("/etc/openvpn folder not found")
            return False

        if os.path.exists(SystemDefinition.ROUTING_FACTORY_RESET_FOLDER_PATH) != True:
            self.__logger.error("{} path not found".format(SystemDefinition.ROUTING_FACTORY_RESET_FOLDER_PATH))
            return False

        if os.path.exists(SystemDefinition.ROUTING_CONFIG_FOLDER_PATH):
            if ServiceManagerHelperFunction.clear_directory(directory_to_be_cleared=SystemDefinition.ROUTING_CONFIG_FOLDER_PATH, logger_object=self.__logger) == True:
                for filename in os.listdir(SystemDefinition.ROUTING_FACTORY_RESET_FOLDER_PATH):
                    if ServiceManagerHelperFunction.copy_file(source_filepath=SystemDefinition.ROUTING_FACTORY_RESET_FOLDER_PATH + PATH_SEPERATOR_CHARACTER + filename,
                                                                destination_filepath=SystemDefinition.ROUTING_CONFIG_FOLDER_PATH, 
                                                                logger_object=self.__logger) != True: 
                        self.__logger.error("Failed to copy ", filename, " file to ", SystemDefinition.ROUTING_CONFIG_FOLDER_PATH)
                        return False

                if ServiceManagerLinuxHelperFunction.change_directory_and_its_files_ownership(user_name=FRR_OWNERSHIP_NAME, 
                                                                                                group_name=FRR_OWNERSHIP_NAME,
                                                                                                directory_path=SystemDefinition.ROUTING_CONFIG_FOLDER_PATH, 
                                                                                                logger_object=self.__logger) != True:
                    self.__logger.error("Failed to change ownership to ", FRR_OWNERSHIP_NAME, " file")
                    return False

                if ServiceManagerLinuxHelperFunction.restart_system_service(service_name=FRR_SERVICE_NAME, logger_object=self.__logger) != True:
                    self.__logger.error("Failed to restart frr service")
                    return False
            else:
                self.__logger.error("Failed to clear /etc/frr directory")
                return False
        else:
            self.__logger.error("/etc/frr folder not found")
            return False

        return True


    def __reset_user_config(self):
        if os.path.exists(SystemDefinition.USER_CONFIG_FILE_PATH):
            try:
                # Removing all the /var/SDWAN/ConfigurationFiles directory
                shutil.rmtree(SystemDefinition.USER_CONFIG_FILE_PATH)
            except OSError as os_error:
                self.__logger.error(os_error)
                return False

        try:
            # Creating /var/SDWAN/ConfigurationFiles directory
            os.mkdir(SystemDefinition.USER_CONFIG_FILE_PATH)
        except OSError as os_error:
            self.__logger.error(os_error)
            return False
        
        # Reseting QOS configuration
        factory_default_qos_config_source_file_path = SystemDefinition.QOS_FACTORY_RESERT_FOLDER_PATH + PATH_SEPERATOR_CHARACTER + SystemDefinition.QOS_CONFIG_FILE_NAME
        qos_config_destination_file_path = SystemDefinition.USER_CONFIG_FILE_PATH + PATH_SEPERATOR_CHARACTER + SystemDefinition.QOS_CONFIG_FILE_NAME

        if os.path.exists(factory_default_qos_config_source_file_path):
            if ServiceManagerHelperFunction.copy_file(source_filepath=factory_default_qos_config_source_file_path, 
                                                    destination_filepath=qos_config_destination_file_path, 
                                                    logger_object=self.__logger) == True:
                if ServiceManagerHelperFunction.set_executable_permission_to_file(path_to_file=qos_config_destination_file_path, logger_object=self.__logger) != True:
                    self.__logger.error("Failed to change permission to ", qos_config_destination_file_path, " file")
                    return False
            else:
                self.__logger.error("Failed to copy ", factory_default_qos_config_source_file_path, " file to ", qos_config_destination_file_path)
                return False
        else:
            self.__logger.error("{} path not found".format(factory_default_qos_config_source_file_path))
            return False

        if ServiceManagerLinuxHelperFunction.execute_script(filepath=qos_config_destination_file_path, logger_object=self.__logger) != True:
            self.__logger.error("Failed to execute qos script")
            return False
        
        # Reseting traffic steering configuration
        traffic_steering_config_destination_folder_path = SystemDefinition.USER_CONFIG_FILE_PATH + PATH_SEPERATOR_CHARACTER + TRAFFIC_STEERING_CONFIGURATION_FILE_DIRECTORY
        factory_default_traffic_steering_config_source_file_path = SystemDefinition.TRAFFIC_STEERING_FACTORY_RESET_FOLDER_PATH + PATH_SEPERATOR_CHARACTER + SystemDefinition.IPTABLES_CONFIG_FILE_NAME            

        try:
            # Creating /var/SDWAN/ConfigurationFiles/traffic-steering-configuration directory
            os.mkdir(traffic_steering_config_destination_folder_path)
        except OSError as os_error:
            self.__logger.error(os_error)
            return False
            
        if os.path.exists(factory_default_traffic_steering_config_source_file_path):
            if ServiceManagerHelperFunction.copy_file(source_filepath=factory_default_traffic_steering_config_source_file_path, 
                                                        destination_filepath=traffic_steering_config_destination_folder_path, 
                                                        logger_object=self.__logger) != True:
                self.__logger.error("Failed to copy ", factory_default_traffic_steering_config_source_file_path, " file to ", traffic_steering_config_destination_folder_path)
                return False
        else: 
            self.__logger.error("{} path not found".format(factory_default_traffic_steering_config_source_file_path))
            return False

        iptables_configuration_restore_command = IPTABLES_RESTORE_COMMAND + SPACE_CHARACTER + INPUT_REDIRECTION_OPERATOR + SPACE_CHARACTER + traffic_steering_config_destination_folder_path + PATH_SEPERATOR_CHARACTER + SystemDefinition.IPTABLES_CONFIG_FILE_NAME

        if ServiceManagerLinuxHelperFunction.execute_linux_command(command=iptables_configuration_restore_command, logger_object=self.__logger) != True:
            self.__logger.error("Failed to restore iptables")
            return False

        return True
        