import os
import subprocess
import threading
import json
import asyncio
import syslog # for logging WAN interface state to the syslog

import CoreCode.logger as Logger
import CoreCode.service_manager_helper_functions as HelperFunctions
import CoreCode.service_manager_linux_helper_functions as LinuxHelperFunctions
import Definitions.system_definitions as SystemDefinitions
import Definitions.message_code_definitions as MessageCodeDefinitions

from CoreCode.service_manager import ServiceManager

IPTABLES_RESTORE_COMMAND = "iptables-restore"
INPUT_REDIRECTION_OPERATOR = "<"
IPTABLES_CONFIG_FILE_NAME = "initial-configuration.txt"
TRAFFIC_STEERING_CONFIGURATION_FILE_ZIP = "traffic-steering-configuration.zip"
TRAFFIC_STEERING_CONFIGURATION_FILE_DIRECTORY = "traffic-steering-configuration"
WAN_INTERFACE_LIST_JSON_FILE_NAME = "wan-interface.json"

IPSET_DOMAIN_CONFIG_FILE_NAME = "ipset-domain.conf"
IPSET_CONFIG_SCRIPT_FILE_NAME = "ipset-configuration.sh"

DNSMASQ_CONFIG_FILE_PATH = "/etc/dnsmasq.d"
DNSMASQ_SERVICE_NAME = "dnsmasq.service"

SPACE_CHARACTER = " "
PATH_SEPERATOR_CHARACTER = os.path.sep

# WAN Failover constants
PING_COMMAND_NAME = "ping"
PING_DESTINATION_IP = "8.8.8.8"
PING_OPTIONS = "-c 3 -i 1 -w 3 -I"
IPTABLES_RESTORE_NO_FLUSH_OPTION = "--noflush"
IPTABLES_FILENAME_SEPERATOR = "-"
IPTABLES_FILENAME_EXTENSION = ".txt"
IPTABLES_PRIMARY_FILENAME_KEYWORD = "primary"
IPTABLES_BACKUP_FILENAME_KEYWORD = "backup"
WAN_INTERFACE_MONITORING_INTERVAL_IN_SECONDS = 3
WAN_INTERFACE_PACKET_LOSS_PERCENTAGE_THRESHOLD = 100
PING_ITERATION_COUNT = 5

# Status Message
SUCCESSFULLY_APPLIED_IPTABLES_CONFIGURATION = "iptables configuration applied successfully"
RECEIVED_TRAFFIC_STEERING_CONFIGURATION_UPDATE_NOTIFICATION = "Received traffic steering configuration update notification"
DOWNLOADED_TRAFFIC_STEERING_CONFIGURATION = "traffic steering configuration downloaded successfully"
EMPTY_TRAFFIC_STEERING_CONFIGURATION_DATA = "Empty traffic steering configuration data"
FAILED_TO_APPLY_INITIAL_IPTABLES_CONFIGURATION = "Failed to apply initial iptables configuration"


class TrafficSteeringManager(ServiceManager):
    """
    TrafficSteeringManager is derived from ServiceManager and is used to execute operations with respect to the traffic steering feature.
    Arguments:
    data_manager:
        An instance of DataManager must be passed. This instance is used to fetch the iptables configuration file from the endpoint.
    response_manager:
        An instance of ResponseManager must be passed
    """
    def __init__(self, data_manager, response_manager):
        self.__logger = Logger.get_logger(__name__)
        self.__logger.info("TrafficSteeringManager initializer starts")

        self.__traffic_steering_configuration_filepath = SystemDefinitions.USER_CONFIG_FILE_PATH + PATH_SEPERATOR_CHARACTER + TRAFFIC_STEERING_CONFIGURATION_FILE_ZIP
        self.__traffic_steering_configuration_extract_filepath = SystemDefinitions.USER_CONFIG_FILE_PATH + PATH_SEPERATOR_CHARACTER + TRAFFIC_STEERING_CONFIGURATION_FILE_DIRECTORY
        self.__initial_iptables_configuration_filepath = SystemDefinitions.USER_CONFIG_FILE_PATH + PATH_SEPERATOR_CHARACTER + TRAFFIC_STEERING_CONFIGURATION_FILE_DIRECTORY + PATH_SEPERATOR_CHARACTER + IPTABLES_CONFIG_FILE_NAME
        self.__ipset_configuration_script_filepath = SystemDefinitions.USER_CONFIG_FILE_PATH + PATH_SEPERATOR_CHARACTER + TRAFFIC_STEERING_CONFIGURATION_FILE_DIRECTORY + PATH_SEPERATOR_CHARACTER + IPSET_CONFIG_SCRIPT_FILE_NAME
        self.__ipset_domain_configuration_filepath = SystemDefinitions.USER_CONFIG_FILE_PATH + PATH_SEPERATOR_CHARACTER + TRAFFIC_STEERING_CONFIGURATION_FILE_DIRECTORY + PATH_SEPERATOR_CHARACTER + IPSET_DOMAIN_CONFIG_FILE_NAME

        self.__temp_traffic_steering_configuration_extract_filepath = SystemDefinitions.TEMP_USER_CONFIG_FILE_PATH + PATH_SEPERATOR_CHARACTER + TRAFFIC_STEERING_CONFIGURATION_FILE_DIRECTORY

        # insert event codes and corresponding routines into this dictionary
        event_dictionary = {}
        event_dictionary[MessageCodeDefinitions.IPTABLES_CONFIGURATION_UPDATE_EVENT] = self.__configuration_update_available_event_routine

        ServiceManager.__init__(self, data_manager=data_manager, response_manager=response_manager, event_dictionary=event_dictionary)

        # Applying the iptables configuration when the TrafficSteerinManager instace is created, to restore the previous configuration when the CPE application starts.
        self.__apply_initial_iptables_configuration()

        self.__wan_interface_list = list()
        self.__wan_interface_list_lock = threading.Lock()

        self.__update_wan_interface_list_flag = True

        # Getting the list of WAN interfaces that need to be monitored
        self.__get_list_of_wan_interfaces()

        wan_interface_monitoring_event_loop = asyncio.new_event_loop()
        wan_interface_management_thread = threading.Thread(target=self.__wan_interface_management_thread_function, args=(wan_interface_monitoring_event_loop,) ,daemon=True)
        wan_interface_management_thread.start()

        self.__logger.info("TrafficSteeringManager initializer ends")


    def __configuration_update_available_event_routine(self):
        self.__logger.info("Traffic steering configuration update event routine start")

        self._response_manager.send_response(message=self._message_dictionary,
                                                status_code=MessageCodeDefinitions.RECEIVED_CONFIGURATION_UPDATE_NOTIFICATION,
                                                status_message=RECEIVED_TRAFFIC_STEERING_CONFIGURATION_UPDATE_NOTIFICATION)

        fetch_traffic_steering_configuration_status, self.__traffic_steering_configuration_data =  self._fetch_configuration_from_endpoint()

        if fetch_traffic_steering_configuration_status == True:
            self._response_manager.send_response(message=self._message_dictionary,
                                                    status_code=MessageCodeDefinitions.DOWNLOADED_CONFIGURATION_FILE,
                                                    status_message=DOWNLOADED_TRAFFIC_STEERING_CONFIGURATION)
            if self.__traffic_steering_configuration_data != b"":
                if HelperFunctions.rotate_files(file_to_be_rotated_filepath=self.__traffic_steering_configuration_filepath,
                                                    data_to_be_written_in_newfile=self.__traffic_steering_configuration_data,
                                                    logger_object=self.__logger) == True:
                    if HelperFunctions.extract_files_to_directory(zip_compressed_filepath=self.__traffic_steering_configuration_filepath,
                                                                extract_destination_directory_path=self.__temp_traffic_steering_configuration_extract_filepath,
                                                                logger_object=self.__logger) == True:

                        # Clear the contents of traffic-steering-configuration directory only if it exists
                        # Create the traffic-steering-configuration directory if it doesn't exist
                        try:
                            if os.path.exists(self.__traffic_steering_configuration_extract_filepath):
                                if HelperFunctions.clear_directory(directory_to_be_cleared=self.__traffic_steering_configuration_extract_filepath,
                                                                    logger_object=self.__logger) != True:
                                    return False
                            else:
                                os.mkdir(self.__traffic_steering_configuration_extract_filepath)
                        except Exception as exception:
                            self.__logger.error(exception)

                        if HelperFunctions.move_files_in_directory(source_directory_path=self.__temp_traffic_steering_configuration_extract_filepath,
                                                                    destination_directory_path=self.__traffic_steering_configuration_extract_filepath,
                                                                    logger_object=self.__logger) != True:
                            return False

                        if self.__configure_ipset_hashtable() != True:
                            self.__logger.debug("Failed to configure IPSET hash table Configuration")
                            return False

                        if self.__configure_ipset_domain() != True:
                            self.__logger.debug("Failed to configure IPSET domain")
                            return False

                        if self.__apply_initial_iptables_configuration() == True:
                            self._response_manager.send_response(message=self._message_dictionary,
                                                                    status_code=MessageCodeDefinitions.SUCCESSFULLY_APPLIED_CONFIGURATION_DATA,
                                                                    status_message=SUCCESSFULLY_APPLIED_IPTABLES_CONFIGURATION)
                            # Once the initial iptables configuration have been successfully set,
                            # the wan interfaces to be monitored for connectivity are fetched
                            self.__get_list_of_wan_interfaces()
                            self.__update_wan_interface_list_flag = True
                            return True
                        else:
                            self.__logger.error("Failed to apply initial iptables configuration settings")
                            self._response_manager.send_response(message=self._message_dictionary,
                                                                    status_code=MessageCodeDefinitions.FAILED_TO_APPLY_CONFIGURATION_DATA,
                                                                    status_message=FAILED_TO_APPLY_INITIAL_IPTABLES_CONFIGURATION)
                            return False
                    else:
                        self.__logger.error("Failed to extract traffic steering configuration file")
                        return False
                else:
                    self.__logger.error("Failed to rotate traffic steering configuration files")   
                    return False
            else:
                self.__logger.error("Empty traffic steering configuration data received")
                self._response_manager.send_response(message=self._message_dictionary,
                                                        status_code=MessageCodeDefinitions.EMPTY_CONFIGURATION_DATA,
                                                        status_message=EMPTY_TRAFFIC_STEERING_CONFIGURATION_DATA)
                return False
        else:
            return False


    def __configure_ipset_hashtable(self):
        self.__logger.info("Configure IPSET hash table starts")

        if os.path.exists(self.__ipset_configuration_script_filepath) != True:
            self.__logger.error("{} file not exist".format(self.__ipset_configuration_script_filepath))
            return False

        if HelperFunctions.set_executable_permission_to_file(path_to_file=self.__ipset_configuration_script_filepath, logger_object=self.__logger) != True:
            self.__logger.error("Falied to set executable permission to {}".format(self.__ipset_configuration_script_filepath))
            return False

        # The return code will tell whether the script execution is success or not.
        # There is no proper way to identify the logical operaton of the script is success or not
        # Hence the return status of the subprocess.run is not validated
        try:
            result = subprocess.run(self.__ipset_configuration_script_filepath, capture_output=True)

            self.__logger.info(result.stdout)
            self.__logger.debug(result.stderr)

            self.__logger.info("{} configuration applied successfully".format(self.__ipset_configuration_script_filepath))
            return True

        except Exception as exception:
            self.__logger.error(exception)
            return False

        return True


    def __configure_ipset_domain(self):
        self.__logger.info("Configuring IPSET domain starts")

        if os.path.exists(self.__ipset_domain_configuration_filepath) != True:
            self.__logger.error("{} not exist".format(self.__ipset_domain_configuration_filepath))
            return False

        system_ipset_config_file = DNSMASQ_CONFIG_FILE_PATH + PATH_SEPERATOR_CHARACTER + IPSET_DOMAIN_CONFIG_FILE_NAME
        if HelperFunctions.remove_file_if_exists(filepath=system_ipset_config_file, logger_object=self.__logger) != True:
            self.__logger.error("Failed to remove existing {} file".format(system_ipset_config_file))
            return False

        if HelperFunctions.copy_file(source_filepath=self.__ipset_domain_configuration_filepath, destination_filepath=DNSMASQ_CONFIG_FILE_PATH, logger_object=self.__logger) != True:
            self.__logger.error("Failed to copy file from {} to {}".format(self.__ipset_domain_configuration_filepath, DNSMASQ_CONFIG_FILE_PATH))
            return False

        if LinuxHelperFunctions.restart_system_service(service_name=DNSMASQ_SERVICE_NAME, logger_object=self.__logger) != True:
            self.__logger.error("Failed to restart the {}".format(DNSMASQ_SERVICE_NAME))
            return False

        return True


    def __apply_initial_iptables_configuration(self):
        if os.path.isfile(self.__initial_iptables_configuration_filepath):
            # The initial-configuration.txt with the updated configuration is used as an input to the iptables-restore command to apply the changes to the system's iptables
            iptables_configuration_restore_command = IPTABLES_RESTORE_COMMAND + SPACE_CHARACTER + INPUT_REDIRECTION_OPERATOR + SPACE_CHARACTER + self.__initial_iptables_configuration_filepath

            try:
                iptables_restore_command_result = subprocess.run(iptables_configuration_restore_command, shell=True, capture_output=True, text=True)
            except Exception as exception:
                self.__logger.error(exception)
                return False

            if iptables_restore_command_result.returncode != 0:
                self.__logger.error("Failed to apply initial iptables configuration, iptables-restore result {}".format(iptables_restore_command_result))
                return False
            else:
                self.__logger.info("Successfully applied initial iptables configuration present at {}".format(self.__initial_iptables_configuration_filepath))
                return True
        else:
            self.__logger.error("{} configuration file does not exist".format(self.__initial_iptables_configuration_filepath))
            return False


    def __get_list_of_wan_interfaces(self):
        wan_interface_list_json_filepath = self.__traffic_steering_configuration_extract_filepath + PATH_SEPERATOR_CHARACTER + WAN_INTERFACE_LIST_JSON_FILE_NAME
        if os.path.isfile(wan_interface_list_json_filepath):
            with open(wan_interface_list_json_filepath, SystemDefinitions.FILE_READ_MODE) as wan_interface_json_file:
                with self.__wan_interface_list_lock:
                    try:
                        self.__wan_interface_list = json.loads(wan_interface_json_file.read())
                    except Exception as exception:
                        self.__logger.error(exception)
        else:
            self.__logger.error("{} file does not exist".format(wan_interface_list_json_filepath))


    async def __ping_destination_via_wan_interface(self, wan_interface_name):
        ping_command = PING_COMMAND_NAME + SPACE_CHARACTER + PING_DESTINATION_IP + SPACE_CHARACTER + \
                    PING_OPTIONS + SPACE_CHARACTER + str(wan_interface_name)

        packet_loss_list = []

        for i in range(PING_ITERATION_COUNT):
            ping_process = await asyncio.create_subprocess_shell(
                                        ping_command,
                                        stdout=asyncio.subprocess.PIPE,
                                        stderr=asyncio.subprocess.PIPE)

            stdout, stderr = await ping_process.communicate()

            if ping_process.returncode != 0:
                packet_loss_percentage = 100
            else:
                packet_loss_percentage = str(stdout).split(',')[2].split('%')[0].strip()

            packet_loss_list.append(float(packet_loss_percentage))

        average_packet_loss_percentage = sum(packet_loss_list) / len(packet_loss_list)
        calculated_packet_loss_percentage = round(average_packet_loss_percentage)

        wan_interface_state = True

        if calculated_packet_loss_percentage == WAN_INTERFACE_PACKET_LOSS_PERCENTAGE_THRESHOLD:
            wan_interface_state = False

        return wan_interface_name, wan_interface_state


    def __set_iptables_for_wan_interfaces(self, wan_interface_name, wan_interface_state):
        iptables_wan_rules_command = ""

        if wan_interface_state == False:
            self.__logger.info("{} interface is INACTIVE".format(wan_interface_name))

            iptables_wan_rules_command = IPTABLES_RESTORE_COMMAND + SPACE_CHARACTER + IPTABLES_RESTORE_NO_FLUSH_OPTION + SPACE_CHARACTER + INPUT_REDIRECTION_OPERATOR + SPACE_CHARACTER + \
                                            self.__traffic_steering_configuration_extract_filepath + PATH_SEPERATOR_CHARACTER + str(wan_interface_name) + IPTABLES_FILENAME_SEPERATOR + IPTABLES_BACKUP_FILENAME_KEYWORD + IPTABLES_FILENAME_EXTENSION
        else:
            self.__logger.info("{} interface is ACTIVE".format(wan_interface_name))

            iptables_wan_rules_command = IPTABLES_RESTORE_COMMAND + SPACE_CHARACTER + IPTABLES_RESTORE_NO_FLUSH_OPTION + SPACE_CHARACTER + INPUT_REDIRECTION_OPERATOR + SPACE_CHARACTER + \
                                            self.__traffic_steering_configuration_extract_filepath + PATH_SEPERATOR_CHARACTER + str(wan_interface_name) + IPTABLES_FILENAME_SEPERATOR + IPTABLES_PRIMARY_FILENAME_KEYWORD + IPTABLES_FILENAME_EXTENSION

        iptables_wan_rules_process = subprocess.run(iptables_wan_rules_command, capture_output=True, shell=True)

        return iptables_wan_rules_process.returncode


    async def __wan_interface_failover_handler(self):
        wait_event = threading.Event()
        wan_interface_current_state_dict = dict()
        wan_interface_previous_state_dict = dict()
        self.__logger.info("WAN interface failover handler task started")

        while True:
            # locking wan_interface_list resource as it could be updated by new user configuration
            with self.__wan_interface_list_lock:
                wan_interface_list_local = self.__wan_interface_list.copy()

            if self.__update_wan_interface_list_flag == True:
                wan_interface_list_local = []
                self.__update_wan_interface_list_flag = False

            # The list of user-provided wan interfaces is checked everytime with the list of state-monitored wan interfaces
            # If a change is detected, the list of state-monitored wan interfaces is cleared and updated with the latest list of user-provided wan interfaces
            if set(wan_interface_list_local) != set(wan_interface_current_state_dict):
                wan_interface_current_state_dict.clear()
                for interface_name in wan_interface_list_local:
                    wan_interface_current_state_dict[str(interface_name)] = True

            if len(wan_interface_list_local) != 0:
                # add ping tasks for each WAN interface
                ping_task_promises_list = list()
                for wan_interface_name in wan_interface_list_local:
                    ping_task_promises_list.append(asyncio.ensure_future(self.__ping_destination_via_wan_interface(wan_interface_name=wan_interface_name)))

                # get the WAN interface name and return code of each ping task
                ping_task_futures = await asyncio.gather(*ping_task_promises_list)

                wan_interface_previous_state_dict = wan_interface_current_state_dict.copy()

                for wan_interface_name, wan_interface_ping_state in ping_task_futures:
                    wan_interface_current_state_dict[str(wan_interface_name)] = wan_interface_ping_state

                    # TBD - this is a code to log the status of WAN interface into the syslog after every ping
                    # This code has been added for easy querying of WAN interface status in the CPE logs, by the telegraf-graffana utilities
                    if wan_interface_ping_state == True:
                        syslog.syslog(syslog.LOG_INFO, "chiefnet | {} interface is ACTIVE".format(wan_interface_name))
                    else:
                        syslog.syslog(syslog.LOG_INFO, "chiefnet | {} interface is INACTIVE".format(wan_interface_name))

                state_changed_wan_interface_dict = {wan_interface: wan_interface_current_state_dict[str(wan_interface)] \
                                                    for wan_interface in wan_interface_current_state_dict \
                                                    if wan_interface in wan_interface_previous_state_dict \
                                                    and wan_interface_current_state_dict[str(wan_interface)] != wan_interface_previous_state_dict[str(wan_interface)]}

                for wan_interface_name, wan_interface_state in state_changed_wan_interface_dict.items():
                    if self.__set_iptables_for_wan_interfaces(wan_interface_name=wan_interface_name, wan_interface_state=wan_interface_state) != 0:
                        self.__logger.error("{} interface iptables configuration failed to set".format(wan_interface_name))
            else:
                self.__logger.info("No WAN interfaces to be monitored")

            # This is a non-blocking call and suspends the thread
            wait_event.wait(WAN_INTERFACE_MONITORING_INTERVAL_IN_SECONDS)

        await asyncio.sleep(0)


    def __wan_interface_management_thread_function(self, wan_interface_monitoring_event_loop):
        self.__logger.info("WAN interface management thread start")
        asyncio.set_event_loop(wan_interface_monitoring_event_loop)
        wan_interface_monitoring_event_loop.create_task(self.__wan_interface_failover_handler())
        wan_interface_monitoring_event_loop.run_forever()