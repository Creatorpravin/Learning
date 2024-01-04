# current = dict()
# current = {"1":"primary","2":"backup","3":"backup"}
# previous = {"1":"primary","2":"priary","3":"backup"}
# print(list(current.keys()) == list(previous.keys()))

# changed_dict = {config : current[config] for config in current if config in previous and current[config] != previous[config]}
# print(changed_dict)
# data = {
#        "1":{
#           "primary_interface" : "enp1s0",
#           "loss":1,
#           "latency":1,
#           "jitter":1,
#           "backup":True,
#           "configuration":{
#              "backup_interface" : "enp2s0",
#              "delete":"-D 1 CN_PREROUTING",
#              "primary":"-A 1 CN_PREROUTING -d 8.8.8.8 -j MARK --set-mark 0x10001/0xffffff",
#              "backup":"-A 1 CN_PREROUTING -d 8.8.8.8 -j MARK --set-mark 0x10002/0xffffff",
#              "backup_latency" : 1,
#              "backup_jitter": 1,
#              "backup_loss": 1
#           }
#        },
#        "2":{
#           "primary_interface" : "enp2s0",           
#           "loss":1,
#           "latency":1,
#           "jitter":1,
#           "backup":False,
#           "configuration":{
#              "backup_interface" : "",
#               "delete":"",
#              "primary":"-A CN_PORSTROUTING -d 8.8.8.8 -j MARK --set-mark 0x10001/0xffffff",
#              "backup":"",
#              "backup_latency" : 1,
#              "backup_jitter": 1,
#              "backup_loss": 1
#           }
#        }
#     }

# if data["1"]["configuration"]["delete"]:
#     print(True)
# else:
#     print(False)
# sample = dict()
# a = 45
# b = 25
# c = 26
# interface = "enp1s0"
# user_thershold = {
#        "1":{
#           "primary_interface" : "enp1s0",
#           "loss":1,
#           "latency":1,
#           "jitter":1,
#           "backup":True,
#           "configuration":{
#              "backup_interface" : "enp2s0",
#              "delete":"-D 1 CN_PREROUTING",
#              "primary":"-A 1 CN_PREROUTING -d 8.8.8.8 -j MARK --set-mark 0x10001/0xffffff",
#              "backup":"-A 1 CN_PREROUTING -d 8.8.8.8 -j MARK --set-mark 0x10002/0xffffff",
#              "backup_latency" : 1,
#              "backup_jitter": 1,
#              "backup_loss": 1
#           }
#        },
#        "2":{
#           "primary_interface" : "enp2s0",           
#           "loss":1,
#           "latency":1,
#           "jitter":1,
#           "backup":False,
#           "configuration":{
#              "backup_interface" : "",
#               "delete":"",
#              "primary":"-A CN_PORSTROUTING -d 8.8.8.8 -j MARK --set-mark 0x10001/0xffffff",
#              "backup":"",
#              "backup_latency" : 1,
#              "backup_jitter": 1,
#              "backup_loss": 1
#           }
#        }
#     }
# # for i in range (0,4):
# #     sample[interface+str(i)] = {"jitter":a+i,"latency":b+i,"loss":c+i}
# actual_threshold = {"enp1s0": {"jitter": 45, "latency": 25, "loss": 96}, "enp2s0": {"jitter": 46, "latency": 26, "loss": 27}, "enp3s0": {"jitter": 47, "latency": 27, "loss": 28}, "enp4s0": {"jitter": 48, "latency": 28, "loss": 29}}
# current_dict = dict()
# interface_performance_score = {"enp1s0" : 0, "enp2s0" : 0}
# for config in user_thershold:
#     primary = user_thershold[config]["primary_interface"]
#     backup = user_thershold[config]["configuration"]["backup_interface"]
    
#     if user_thershold[config]["backup"] != False:
#        if primary in actual_threshold:
#          if actual_threshold[primary]["latency"] <= 100 and actual_threshold[primary]["loss"] <= 100 and actual_threshold[primary]["jitter"] <= 100:
#             for metrics in ["jitter", "latency", "loss"]:
#                if actual_threshold[primary][metrics] <= user_thershold[config][metrics]:
#                   interface_performance_score[backup] +=1

#          elif actual_threshold[backup]["latency"] <= 100 and actual_threshold[backup]["loss"] <= 100 and actual_threshold[backup]["jitter"] <= 100:         
#             for metrics in ["jitter", "latency", "loss"]:
#                if actual_threshold[backup][metrics] <= user_thershold[config]["configuration"]["backup_"+metrics]:
#                   interface_performance_score[backup] +=1
#          else:
#             current_dict[config] = primary
         
#          best_interface = max(interface_performance_score, key=interface_performance_score.get)
#          current_dict[config] = best_interface 

# print(current_dict)

# a = ["tap0", "tap1", "enp1s0", "enp2s0"]
# s = ""
# d = {"tap0" : "192.168.1.23", "tap1" : "192.168.2.23"}
# for i in a:
#     if "tap" in i:
#         ip = (d[i].split("."))
#         ip[-1] = "1"
#         jo = ".".join(ip)
#         print(jo)

import os
import subprocess
import threading
import json
import asyncio
import syslog # for logging WAN interface state to the syslog
import jc # for converting the iptables string to json format
import psutil # for live network interface monitoring purpose
import re 

import CoreCode.logger as Logger
import CoreCode.service_manager_helper_functions as HelperFunctions
import CoreCode.service_manager_linux_helper_functions as LinuxHelperFunctions
import Definitions.system_definitions as SystemDefinitions
import Definitions.message_code_definitions as MessageCodeDefinitions
import Definitions.message_definitions as MessageDefinitions

from CoreCode.service_manager import ServiceManager

IPTABLES_RESTORE_COMMAND = "iptables-restore"
INPUT_REDIRECTION_OPERATOR = "<"
IPTABLES_CONFIG_FILE_NAME = "initial-configuration.txt"
TRAFFIC_STEERING_CONFIGURATION_FILE_ZIP = "traffic-steering-configuration.zip"
TRAFFIC_STEERING_CONFIGURATION_FILE_DIRECTORY = "traffic-steering-configuration"
WAN_INTERFACE_LIST_JSON_FILE_NAME = "wan-interface.json"
WAN_FAILOVER_THRESHOLD_JSON_FILE_NAME = "primary-backup-user-threshold.json"
WAN_FAILOVER_BACKUP_PREFIX_FILE_NAME = "-backup-"
IPTABLES_MANGLE = "mangle"
IPTABLES_COMMAND = "iptables"
IPTABLES_TABLES_OPTION = "-t"
IPTABLES_LIST_LINE_NUMBER_OPTION = "-L --line-number -n -v"
DEFAULT_THRESHOLD_VALUES = {"packet_loss": 30, "jitter": 40, "Latency": 20}
CONFIGURATION_KEYWORD = "configuration"
DELETE_KEYWORD = "delete"
IPTABLES_TABLE_LIST = ["nat", "mangle", "filter"]
THRESHOLD_NAME_LIST = ["loss",  "latency", "jitter"]
IPTABLES_COMMAND_KEYWORD = "iptables_command"

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

WAN_INTERFACE_STATE_CHECK_INTERVAL_IN_SECONDS = 5

STATE_BASED_FAILOVER_INTERFACE_PREFIX_LIST = ["tap", "tun", "prisma", "ipsec"]


# Status Message
SUCCESSFULLY_APPLIED_IPTABLES_CONFIGURATION = "iptables configuration applied successfully"
RECEIVED_TRAFFIC_STEERING_CONFIGURATION_UPDATE_NOTIFICATION = "Received traffic steering configuration update notification"
DOWNLOADED_TRAFFIC_STEERING_CONFIGURATION = "traffic steering configuration downloaded successfully"
EMPTY_TRAFFIC_STEERING_CONFIGURATION_DATA = "Empty traffic steering configuration data"
FAILED_TO_APPLY_INITIAL_IPTABLES_CONFIGURATION = "Failed to apply initial iptables configuration"

RECEIVED_NOTIFICATION_TO_SHARE_TRAFFIC_STEERING_STATS = "Received notification to share traffic steering stats"
UNABLE_TO_GET_TRAFFIC_STEERING_STATS = "Unable to get Traffic steering statistics"
SUCCESSFULY_SHARED_TRAFFIC_STEERING_STATS = "Traffic steering statistics shared successfully"
FAILED_TO_SHARE_TRAFFIC_STEERING_STATS = "Failed to share the Traffic steering statistics"


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
        event_dictionary[MessageCodeDefinitions.SHARE_TRAFFIC_STEERING_STATISTICS_EVENT] = self.__share_traffic_steering_statistics

        ServiceManager.__init__(self, data_manager=data_manager, response_manager=response_manager, event_dictionary=event_dictionary)

        # Applying the iptables configuration when the TrafficSteerinManager instace is created, to restore the previous configuration when the CPE application starts.
        self.__apply_initial_iptables_configuration()

        self.__wan_interface_list = dict()
        self.__wan_interface_list_lock = threading.Lock()

        self.__wan_failover_threshold_dict = dict()
        self.__wan_failover_threshold_dict_lock = threading.Lock()

        self.__update_wan_interface_list_flag = True

        self.__wan_interface_ping_state = {}
        self.__interface_operstate = {}

        # Getting the list of WAN interfaces that need to be monitored
        self.__get_list_of_wan_interfaces()
        self.__get_wan_failover_threshold_value()

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
                            self.__get_wan_failover_threshold_value()
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


    async def __ping_destination_via_wan_interface(self, wan_interface_name, wan_failover_destination):
        
        ping_command = PING_COMMAND_NAME + SPACE_CHARACTER + str(wan_failover_destination) + SPACE_CHARACTER + \
                      PING_OPTIONS + SPACE_CHARACTER + str(wan_interface_name)
        wan_interface_state_dict = {}


        packet_loss_list = []
        latency_list = []
        jitter_list = []
        
        for i in range(PING_ITERATION_COUNT):
            ping_process = await asyncio.create_subprocess_shell(
                                        ping_command,
                                        stdout=asyncio.subprocess.PIPE,
                                        stderr=asyncio.subprocess.PIPE)

            stdout, stderr = await ping_process.communicate()

            if ping_process.returncode != 0:
                packet_loss_percentage = 100
                rtt_avg = 100
                jitter = 100

            else:
                packet_loss_percentage = str(stdout).split(',')[2].split('%')[0].strip()
                rtt_min = str(stdout).split("mdev =")[1].split("/")[0]
                rtt_avg = str(stdout).split("mdev =")[1].split("/")[1]
                rtt_max = str(stdout).split("mdev =")[1].split("/")[2]
                jitter = float(rtt_max) - float(rtt_min)
            packet_loss_list.append(float(packet_loss_percentage))
            latency_list.append(float(rtt_avg))
            jitter_list.append(float(jitter))


        average_packet_loss_percentage = sum(packet_loss_list) / len(packet_loss_list)
        calculated_packet_loss_percentage = round(average_packet_loss_percentage)
            
        average_latency_ms = sum(latency_list) / len(latency_list)
        calculated_packet_latency = round(average_latency_ms)

        average_jitter_ms = sum(jitter_list) / len(jitter_list)
        calculated_packet_jitter = round(average_jitter_ms)
            

        wan_interface_state_dict[wan_interface_name] = {THRESHOLD_NAME_LIST[0]:calculated_packet_loss_percentage,THRESHOLD_NAME_LIST[1]:calculated_packet_latency,THRESHOLD_NAME_LIST[2]:calculated_packet_jitter}
        return wan_interface_state_dict


    def __set_iptables_for_wan_interfaces(self, configurtion_name, wan_interface_state):
        iptables_wan_rules_command = ""
        iptables_wan_rules_delete_command = ""
        if self.__wan_failover_threshold_dict[str(configurtion_name)][CONFIGURATION_KEYWORD][DELETE_KEYWORD]:
            iptables_wan_rules_delete_command = IPTABLES_COMMAND + SPACE_CHARACTER + IPTABLES_TABLES_OPTION + SPACE_CHARACTER + IPTABLES_MANGLE + SPACE_CHARACTER + self.__wan_failover_threshold_dict[str(configurtion_name)][CONFIGURATION_KEYWORD][DELETE_KEYWORD]
            iptables_wan_delete_rules_process = subprocess.run(iptables_wan_rules_delete_command, capture_output=True, shell=True)
            if iptables_wan_delete_rules_process.returncode != 0:
                iptables_wan_rules_command = IPTABLES_COMMAND + SPACE_CHARACTER + IPTABLES_TABLES_OPTION + SPACE_CHARACTER + IPTABLES_MANGLE + SPACE_CHARACTER + self.__wan_failover_threshold_dict[str(configurtion_name)][CONFIGURATION_KEYWORD][wan_interface_state][IPTABLES_COMMAND_KEYWORD]
                iptables_wan_rules_process = subprocess.run(iptables_wan_rules_command, capture_output=True, shell=True)
                if iptables_wan_rules_process.returncode != 0:
                   self.__logger.info("{} is applied on configuration {}".format(wan_interface_state,configurtion_name))
                else:
                    self.__logger.info("{} is failed to applied configuration {}".format(wan_interface_state,configurtion_name))
                    return iptables_wan_rules_process.returncode
            else:
                self.__logger.info("Failed to delete {}".format(configurtion_name))
                return iptables_wan_delete_rules_process.returncode
        else:
            iptables_wan_rules_command = IPTABLES_COMMAND + SPACE_CHARACTER + IPTABLES_TABLES_OPTION + SPACE_CHARACTER + IPTABLES_MANGLE + SPACE_CHARACTER + self.__wan_failover_threshold_dict[str(configurtion_name)][CONFIGURATION_KEYWORD][wan_interface_state][IPTABLES_COMMAND_KEYWORD]
            iptables_wan_rules_process = subprocess.run(iptables_wan_rules_command, capture_output=True, shell=True)
            if iptables_wan_rules_process.returncode != 0:
                   self.__logger.info("{} is applied on configuration {}".format(wan_interface_state,configurtion_name))
                   return iptables_wan_rules_process.returncode
            else:
                self.__logger.info("{} is failed to applied configuration {}".format(wan_interface_state,configurtion_name))
                return iptables_wan_rules_process.returncode                            

        return iptables_wan_rules_process.returncode


    async def __wan_interface_failover_handler(self):
        wait_event = threading.Event()
        current_configuration_state_dict = dict()
        previous_configuration_state_dict = dict()
        state_changed_config_dict = dict()
        self.__logger.info("WAN interface failover handler task started")

        while True:
            # locking wan_interface_list resource as it could be updated by new user configuration
            with self.__wan_interface_list_lock:
                wan_interface_list_local = self.__wan_interface_list.copy()

            with self.__wan_failover_threshold_dict_lock:
                wan_failover_threshold_dict_local = self.__wan_failover_threshold_dict.copy()

            if self.__update_wan_interface_list_flag == True:
                wan_interface_list_local = []
                self.__update_wan_interface_list_flag = False


            if len(wan_interface_list_local) != 0:
                # add ping tasks for each WAN interface
                ping_task_list = list()
                ping_task_promises_dict = dict()
                ping_task_promises_list = list()
                tunnel_state_list = list()

                for interface in wan_interface_list_local:
                        ping_task_list.append(asyncio.ensure_future(self.__ping_destination_via_wan_interface(wan_interface_name=list(interface)[0], wan_failover_destination=list(interface.values())[0])))

                ping_task_promises_list = await asyncio.gather(*ping_task_list)
                ping_task_promises_dict = dict(map(lambda d: list(d.items())[0], ping_task_promises_list))
                wan_interface_current_state = ping_task_promises_dict.copy()
                previous_configuration_state_dict = current_configuration_state_dict.copy()

                current_configuration_state_dict = self.__analyze_threshold_percent(wan_interface_threshold=wan_interface_current_state)

                for interface in wan_interface_current_state:
                    syslog.syslog(syslog.LOG_INFO, "chiefnet | {} interface status is {}".format(interface, wan_interface_current_state[interface]))

                if previous_configuration_state_dict:
                   if list(current_configuration_state_dict.keys()) == list(previous_configuration_state_dict.keys()):
                       state_changed_config_dict = {config : current_configuration_state_dict[config] for config in current_configuration_state_dict if config in previous_configuration_state_dict and current_configuration_state_dict[config] != previous_configuration_state_dict[config]}
                else:
                    state_changed_config_dict = current_configuration_state_dict

                for configuration_name, wan_interface_state in state_changed_config_dict.items():
                    if self.__set_iptables_for_wan_interfaces(configuration_name, wan_interface_state=wan_interface_state) != 0:
                        self.__logger.error("{} interface iptables configuration failed to set".format(configuration_name))
            else:                
                self.__logger.info("No WAN interfaces to be monitored")

            # This is a non-blocking call and suspends the thread
            wait_event.wait(WAN_INTERFACE_MONITORING_INTERVAL_IN_SECONDS)
            await asyncio.sleep(0)


    async def __get_interface_status(self, interface_name):
        try:
            # Get the network interface stats for the specified interface
            interface = psutil.net_if_stats().get(interface_name)

            # check if the interface object exists and is up
            if interface is not None and interface.isup:
                return True
            else:
                return False
        except Exception as exceptions:
            self.__logger.info(exceptions)
            return False


    async def __monitor_interface_state(self):
        interface_list = psutil.net_if_stats().keys()
        interface_states = {}

        while True:
            for interface in interface_list:
                interface_status = await self.__get_interface_status(interface)

                # check if the interface state has changed
                if interface not in interface_states or interface_status != interface_states[interface]:
                    interface_states[interface] = interface_status
                    self.__interface_operstate[interface] = interface_status

            await asyncio.sleep(WAN_INTERFACE_STATE_CHECK_INTERVAL_IN_SECONDS)


    def __wan_interface_management_thread_function(self, wan_interface_monitoring_event_loop):
        self.__logger.info("WAN interface management thread start")
        asyncio.set_event_loop(wan_interface_monitoring_event_loop)
        wan_interface_monitoring_event_loop.create_task(self.__wan_interface_failover_handler())
        wan_interface_monitoring_event_loop.create_task(self.__monitor_interface_state())
        wan_interface_monitoring_event_loop.run_forever()


    def __get_iptables_statistics(self):
        iptables_stats_dict = {}

        # Get iptables statistics of each table present in the IPTABLES_TABLE_LIST
        for iptables_table in IPTABLES_TABLE_LIST:
            parsed_iptables_stats = ""
            iptables_stats_command  = IPTABLES_COMMAND + SPACE_CHARACTER + IPTABLES_TABLES_OPTION + SPACE_CHARACTER \
                                                   + iptables_table + SPACE_CHARACTER + IPTABLES_LIST_LINE_NUMBER_OPTION

            try:
                iptables_stats_command_result = subprocess.run(iptables_stats_command , shell=True, capture_output=True)

                if iptables_stats_command_result.returncode == 0:
                    iptables_stats_std_output = (iptables_stats_command_result.stdout).decode("utf-8")

                    # Convert the statistics of iptables as json using python jc module
                    parsed_iptables_stats = jc.parse(IPTABLES_COMMAND, iptables_stats_std_output)

            except Exception as exception:
                self.__logger.error(exception)
                return False, parsed_iptables_stats

            # Append each tables of iptables in a single dictonary
            iptables_stats_dict[iptables_table] = parsed_iptables_stats

        return True, iptables_stats_dict


    def __share_traffic_steering_statistics(self):
        self.__logger.info("Share Traffic Steering statistics event routine start")

        self._response_manager.send_response(message=self._message_dictionary,
                                            status_code=MessageCodeDefinitions.RECEIVED_NOTIFICATION_TO_SHARE_TRAFFIC_STEERING_STATS,
                                            status_message=RECEIVED_NOTIFICATION_TO_SHARE_TRAFFIC_STEERING_STATS)

        traffic_steering_information_status, traffic_steering_statistics = self.__get_iptables_statistics()

        if traffic_steering_information_status == True:

            try:
                destination_endpoint = self._message_dictionary[MessageDefinitions.CONTENT_KEY][MessageDefinitions.ENDPOINT_KEY]
            except Exception as exception:
                self.__logger.error(exception)
            traffic_steering_stats_message = dict()
            traffic_steering_stats_message["iptables_stats"] = traffic_steering_statistics
            traffic_steering_stats_message["interface_state"] = self.__wan_interface_ping_state

            put_data_status = self._data_manager.put_data(traffic_steering_stats_message, destination_endpoint)

            if put_data_status == True:
                self._response_manager.send_response(message=self._message_dictionary,
                                                    status_code=MessageCodeDefinitions.SUCCESSFULLY_SHARED_TRAFFIC_STEERING_STATS,
                                                    status_message=SUCCESSFULY_SHARED_TRAFFIC_STEERING_STATS)
                return True
            else:
                self._response_manager.send_response(message=self._message_dictionary,
                                                    status_code=MessageCodeDefinitions.FAILED_TO_SHARE_TRAFFIC_STEERING_STATS,
                                                    status_message=FAILED_TO_SHARE_TRAFFIC_STEERING_STATS)
                return False
        else:
            return False        
    def get_all_ip_addresses(self):
        try:
            # Run the 'ip address' command to get information about all interfaces
            result = subprocess.run(['ip', 'address'], capture_output=True, text=True)
            
            # Extract interface names and corresponding IP addresses using regular expression
            ip_pattern = re.compile(r'inet (\d+\.\d+\.\d+\.\d+).*?scope global (.+)')
            matches = ip_pattern.findall(result.stdout)
            print(matches)
            # Create a dictionary of interface names and IP addresses
            ip_addresses = {interface: ip for ip, interface in matches}
            
            if ip_addresses:
               for interface, ip in ip_addresses.items():
                   test = interface.split(" ")
                   self.__interface_ip_dict[test[-1]] = ip
    
    
            return ip_addresses
        
        except Exception as e:
            print(f"Error getting IP addresses: {e}")
            return None        
    def __get_wan_failover_threshold_value(self):
        wan_failover_threshold_json_filepath = self.__traffic_steering_configuration_extract_filepath + PATH_SEPERATOR_CHARACTER + WAN_FAILOVER_THRESHOLD_JSON_FILE_NAME
        if os.path.isfile(wan_failover_threshold_json_filepath):
            with open(wan_failover_threshold_json_filepath, SystemDefinitions.FILE_READ_MODE) as wan_interface_json_file:
                with self.__wan_failover_threshold_dict_lock:
                    try:
                        self.__wan_failover_threshold_dict = json.loads(wan_interface_json_file.read())
                    except Exception as exception:
                        self.__logger.error(exception)
        else:
            self.__logger.error("{} file does not exist".format(wan_failover_threshold_json_filepath))

    def __analyze_threshold_percent(self, wan_interface_threshold):
       
       current_dict = dict()
       for configuration in self.__wan_failover_threshold_dict:
            primary = self.__wan_failover_threshold_dict[configuration]["primary_interface"]
            if self.__wan_failover_threshold_dict[configuration]["backup"] != "False":
               backup = self.__wan_failover_threshold_dict[configuration]["configuration"]["backup_interface"][0]
               interface_performance_score = dict()
               interface_performance_score[primary] = 3
               interface_performance_score[backup] = 3
               if primary in wan_interface_threshold:
                 if wan_interface_threshold[primary]["latency"] <= 100 and wan_interface_threshold[primary]["loss"] <= 100 and wan_interface_threshold[primary]["jitter"] <= 100:
                    for metrics in THRESHOLD_NAME_LIST:
                       if wan_interface_threshold[primary][metrics] <= self.__wan_failover_threshold_dict[configuration][CONFIGURATION_KEYWORD][primary][metrics]:
                          interface_performance_score[primary] -=1
                 if wan_interface_threshold[backup]["latency"] <= 100 and wan_interface_threshold[backup]["loss"] <= 100 and wan_interface_threshold[backup]["jitter"] <= 100:         
                    for metrics in THRESHOLD_NAME_LIST:
                       if wan_interface_threshold[backup][metrics] <= self.__wan_failover_threshold_dict[configuration][CONFIGURATION_KEYWORD][backup][metrics]:
                          interface_performance_score[backup] -=1
                 else:
                    current_dict[configuration] = primary
                 best_interface = min(interface_performance_score, key=interface_performance_score.get)
                 current_dict[configuration] = best_interface
            else:
                current_dict[configuration] = primary
       return current_dict
