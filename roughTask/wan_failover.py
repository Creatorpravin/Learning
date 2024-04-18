import time

def __analyze_threshold_percent(self, wan_interface_threshold):
    current_dict = dict()
    for configuration in self.__wan_failover_threshold_dict:
        primary = self.__wan_failover_threshold_dict[configuration][PRIMARY_INTERFACE_KEYWORD]
        try:
            if self.__wan_failover_threshold_dict[configuration]["backup"] != "False":
                backup = self.__wan_failover_threshold_dict[configuration][CONFIGURATION_KEYWORD][BACKUP_INTERFACE_KEYWORD][0]
                interface_performance_score = dict()
                interface_performance_score[primary] = 3
                interface_performance_score[backup] = 3
                if primary in wan_interface_threshold:
                    if wan_interface_threshold[primary][THRESHOLD_NAME_LIST[0]] < MAXIMUM_PACKET_LOSS_THRESHOLD_VALUE:
                        for metrics in THRESHOLD_NAME_LIST:
                            if wan_interface_threshold[primary][metrics] < self.__wan_failover_threshold_dict[configuration][CONFIGURATION_KEYWORD][primary][metrics]:
                                interface_performance_score[primary] -= 1
                if interface_performance_score[primary]:         
                    if backup in wan_interface_threshold:
                        if wan_interface_threshold[backup][THRESHOLD_NAME_LIST[0]] < MAXIMUM_PACKET_LOSS_THRESHOLD_VALUE:         
                            for metrics in THRESHOLD_NAME_LIST:
                                if wan_interface_threshold[backup][metrics] < self.__wan_failover_threshold_dict[configuration][CONFIGURATION_KEYWORD][backup][metrics]:
                                    interface_performance_score[backup] -= 1
                        else:
                            current_dict[configuration] = primary
                        best_interface = min(interface_performance_score, key=interface_performance_score.get)
                        current_dict[configuration] = best_interface
                    else:
                        current_dict[configuration] = primary
                else:
                    current_dict[configuration] = primary
            else:
                current_dict[configuration] = primary
        except Exception as exception:
            self.__logger.error(exception)
    return current_dict


def perform_wan_failover_analysis(self, wan_interface_threshold):
    current_dict = self.__analyze_threshold_percent(wan_interface_threshold)
    # Check if WAN 1 latency is causing issues
    if current_dict["wan_1_configuration"] == "wan_1" and wan_interface_threshold["wan_1"]["latency"] > MAX_LATENCY_THRESHOLD:
        print("WAN 1 latency issue detected. Waiting for one minute before analyzing failover...")
        time.sleep(60)  # Wait for one minute before analyzing failover again
        current_dict = self.__analyze_threshold_percent(wan_interface_threshold)
    return current_dict
