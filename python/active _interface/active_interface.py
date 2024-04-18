import psutil
import json
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(name)s | %(message)s')

file_handler = logging.FileHandler('/var/SDWAN/Monitoring/interface_monitoring.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s | %(name)s | %(message)s'))

logging.getLogger('').addHandler(file_handler)

STILL_WORD = "still"
TO_WORD = "to"
FROM_WORD = "from"
INTERFACE_WORD = "interface"
TIMESTAMP_WORD = "timestamp"
INTERVAL_WORD = "interval"
STATS_WORD  = "stats"
UP_WORD = "up"
DOWN_WORD = "down"
JSON_WRITE_WORD = "w"
JSON_READ_WORD = "r"
PRISMA_IPSEC_NAME_LIST = ["prisma", "ipsec"]

ACTIVE_INTERFACE_JSON_FILE_PATH = "/var/SDWAN/Monitoring/active_interfaces.json"
INACTIVE_INTERFACE_JSON_FILE_PATH = "/var/SDWAN/Monitoring/inactive_interfaces.json"

class NetworkInterfaceMonitor:
    def __init__(self):
        self.__interfaces = psutil.net_if_stats()
        self.__logger = logging.getLogger(self.__class__.__name__)
    
    def load_previous_active_interfaces(self):
        try:
            with open(ACTIVE_INTERFACE_JSON_FILE_PATH, JSON_READ_WORD) as file:
                return json.load(file)
        except FileNotFoundError:
            return []
    
    def load_previous_inactive_interfaces(self):
        try:
            with open(INACTIVE_INTERFACE_JSON_FILE_PATH, JSON_READ_WORD) as file:
                return json.load(file)
        except FileNotFoundError:
            return []
    
    def interface_states(self):
        interfaces = self.__interfaces
        active_interfaces = []
        inactive_interfaces = []
        
        current_time = int(time.time())
        try:
            for interface, stats in interfaces.items():
                if PRISMA_IPSEC_NAME_LIST[0] not in interface and PRISMA_IPSEC_NAME_LIST[1] not in interface:
                    state = UP_WORD if stats.isup else DOWN_WORD
            
                    if state == UP_WORD:
                        active_interfaces.append({INTERFACE_WORD: interface, TIMESTAMP_WORD: current_time})
                    else:
                        inactive_intervals = [{FROM_WORD: current_time, TO_WORD: STILL_WORD, INTERVAL_WORD: 0}]
                        inactive_interfaces.append({INTERFACE_WORD: interface, STATS_WORD : inactive_intervals})
                        self.__logger.info("{0} : {1} - {2} : {3}".format(interface,current_time,STILL_WORD,0))
            
                    with open(ACTIVE_INTERFACE_JSON_FILE_PATH, JSON_WRITE_WORD) as active_file:
                       json.dump(active_interfaces, active_file, indent=4)
            
                    with open(INACTIVE_INTERFACE_JSON_FILE_PATH, JSON_WRITE_WORD) as inactive_file:
                       json.dump(inactive_interfaces, inactive_file, indent=4)
            
            return True
        
        except  Exception as e:
            print("An error occurred while getting the network interface states.")
            return False
    
    
    def get_interface_states(self, previous_active_interfaces, previous_inactive_interfaces):
        interfaces = self.__interfaces
    
        active_interfaces = []
        inactive_interfaces = []
        
        previous_inactive_interfaces_list = [item[INTERFACE_WORD] for item in previous_inactive_interfaces]
        previous_inactive_to_status = [item[STATS_WORD][-1][TO_WORD] for item in previous_inactive_interfaces]
        previous_value_dict = dict(zip(previous_inactive_interfaces_list,previous_inactive_to_status))
    
        current_time = int(time.time())
        
        for interface, stats in interfaces.items():
            if PRISMA_IPSEC_NAME_LIST[0] not in interface and PRISMA_IPSEC_NAME_LIST[1] not in interface:
                state = UP_WORD if stats.isup else DOWN_WORD
                if state == UP_WORD:
                    active_interfaces.append({INTERFACE_WORD: interface, TIMESTAMP_WORD: current_time})
                
                elif interface not in previous_inactive_interfaces_list:
                    inactive_intervals = [{FROM_WORD: current_time, TO_WORD: STILL_WORD, INTERVAL_WORD: 0}]
                    previous_inactive_interfaces.append({INTERFACE_WORD: interface, STATS_WORD: inactive_intervals})
                    self.__logger.info("{0} : {1} - {2} : 0".format(interface,current_time,STILL_WORD))         
                
                elif interface in previous_inactive_interfaces_list:
                    if interface in previous_inactive_interfaces_list:
                        if previous_value_dict[interface] == STILL_WORD:
                            pass
                        else:
                          if isinstance(previous_value_dict[interface], int):
                            for index,stats in enumerate(previous_inactive_interfaces):
                              if stats[INTERFACE_WORD]==interface:
                                inactive_intervals = {FROM_WORD: current_time, TO_WORD: STILL_WORD, INTERVAL_WORD: 0}
                                previous_inactive_interfaces[index][STATS_WORD].append(inactive_intervals)
                                self.__logger.info("{0} : {1} - {2} : 0".format(interface,current_time,STILL_WORD))       
    
        active_interface_list = [item[INTERFACE_WORD] for item in active_interfaces]
    
         
        for index,stats in enumerate(previous_inactive_interfaces):
            if stats[STATS_WORD][-1][TO_WORD] == STILL_WORD:
                if stats[INTERFACE_WORD] in active_interface_list:
                    interval_time = current_time - previous_inactive_interfaces[index][STATS_WORD][-1][FROM_WORD]
                    previous_inactive_interfaces[index][STATS_WORD][-1][INTERVAL_WORD] = interval_time
                    previous_inactive_interfaces[index][STATS_WORD][-1][TO_WORD] = current_time
                    self.__logger.info("{0} : {1} - {2} : {3}".format(previous_inactive_interfaces[index][INTERFACE_WORD],previous_inactive_interfaces[index][STATS_WORD][-1][FROM_WORD],current_time,interval_time))         
                else:
                    interval_time = current_time - previous_inactive_interfaces[index][STATS_WORD][-1][FROM_WORD]
                    previous_inactive_interfaces[index][STATS_WORD][-1][INTERVAL_WORD] = interval_time
                    self.__logger.info("{0} : {1} - {2} : {3}".format(previous_inactive_interfaces[index][INTERFACE_WORD],previous_inactive_interfaces[index][STATS_WORD][-1][FROM_WORD],STILL_WORD,interval_time))
    
        inactive_interfaces = previous_inactive_interfaces
     
        return active_interfaces, inactive_interfaces


network_interface_monitor = NetworkInterfaceMonitor()


previous_active_interfaces = network_interface_monitor.load_previous_active_interfaces()
previous_inactive_interfaces = network_interface_monitor.load_previous_inactive_interfaces()


if not previous_active_interfaces and not previous_inactive_interfaces:
    interface_state = network_interface_monitor.interface_states()
    if interface_state == False:
        print("Failed to create JSON files")
else:
    active_interfaces, inactive_interfaces = network_interface_monitor.get_interface_states(previous_active_interfaces, previous_inactive_interfaces)

    with open(ACTIVE_INTERFACE_JSON_FILE_PATH, JSON_WRITE_WORD) as active_file:
        json.dump(active_interfaces, active_file, indent=4)

    with open(INACTIVE_INTERFACE_JSON_FILE_PATH, JSON_WRITE_WORD) as inactive_file:
        json.dump(inactive_interfaces, inactive_file, indent=4)

    print("Active interfaces written to active_interfaces.json")
    print("Inactive interfaces written to inactive_interfaces.json")
