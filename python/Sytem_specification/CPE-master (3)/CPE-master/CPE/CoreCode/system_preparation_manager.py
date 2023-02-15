import subprocess
import json
import re
import os

import CoreCode.logger as Logger
import Definitions.system_definitions as SystemDefinitions

from CoreCode import service_manager_linux_helper_functions as LinuxHelperFunction
from CoreCode import service_manager_helper_functions as HelperFunction

HOSTNAME_FILE_PATH = "/etc/hostname"
HOSTS_FILE_PATH = "/etc/hosts"
LOOPBACK_INTERFACE_NAME = "lo"

FIRST_WAN_INTERFACE_INDEX_VALUE = 2

OS_INFO_COMMAND = "lsb_release -r -s"
CPU_INFO_COMMAND = "lshw -json -c processor"
SHOW_INTERFACE_INFORMATION_COMMAND = "ip -json address show"

TUNNEL_INTERFACE_PREFIX_VALUE = "tun"
TAP_INTERFACE_PREFIX_VALUE = "tap"
BRIDGE_INTERFACE_PREFIX_VALUE = "br"
VLAN_INTERFACE_MATCH_VALUE = r"\."
WIRELESS_INTERFACE_PREFIX_VALUE = "wl"

SYSTEM_INTERFACE_INFORMATION_INTERFACE_INDEX_KEY = "ifindex"
SYSTEM_INTERFACE_INFORMATION_INTERFACE_ADDRESS_KEY = "address"
SYSTEM_INTERFACE_INFORMATION_INTERFACE_NAME_KEY = "ifname"

PHYSICAL_INTERFACE_KEY = "physical"
PHYSICAL_WAN_INTERFACE_KEY = "wan"
PHYSICAL_LAN_INTERFACE_KEY = "lan"
TUNNEL_INTERFACE_KEY = "tun"
TAP_INTERFACE_KEY = "tap"
VLAN_INTERFACE_KEY = "vlan"
BRIDGE_INTERFACE_KEY = "bridge"
WIRELESS_INTERFACE_KEY = "wireless"


class SystemPrepartionManager:
    def __init__(self):
        self.__logger = Logger.get_logger(logger_name=__name__)
        self.__logger.info("System Prepartion Manager initializer starts")

        if os.path.exists(SystemDefinitions.SYS_CONFIG_FILE_PATH_NAME) is False:

            self.__interface_information = self.__get_interface_information()
            if not self.__interface_information:
                self.__logger.error("Empty Interface information")
                raise Exception

            self.__parsed_interface_info = self.__get_parsed_interface_info()
            if not self.__parsed_interface_info:
                self.__logger.error("Empty Parsed Interface information")
                raise Exception

            self.__mac_address = self.__get_mac_address()
            if not self.__mac_address:
                self.__logger.error("Empty MAC address information")
                raise Exception

            self.__uuid = self.__mac_address.upper()
            if not self.__uuid:
                self.__logger.error("Empty UUID infromation")
                raise Exception

            self.__logger.info("Dependency information excecuted successfully")
            if self.__update_hostname() is False:
                raise Exception

            self.__logger.info("Hostname Updated Successfully")
            if self.__create_system_configuration_json_file() is False:
                raise Exception

            self.__logger.info("System Configuration json Updated Successfully")
            if self.__generate_ignore_carrier_configuration(physical_lan_interface_list=self.__parsed_interface_info[PHYSICAL_INTERFACE_KEY][PHYSICAL_LAN_INTERFACE_KEY]) is False:
                raise Exception

            self.__logger.info("Ignore carrier Configuration is Generated Successfully")
            if LinuxHelperFunction.reboot_system(logger_object=self.__logger) is False:
                raise Exception

        else:
            self.__logger.info(SystemDefinitions.SYS_CONFIG_FILE_PATH_NAME + " file already exist")

        self.__logger.info("System Prepartion Manager initializer ends")


    def __update_hostname(self):
        current_hostname = self.__get_hostname()

        parsed_uuid = "".join(self.__uuid.split(":"))
        new_hostname = SystemDefinitions.HOSTNAME_PREFIX + parsed_uuid

        if not current_hostname:
            return False

        if not new_hostname:
            return False

        if self.__replace_hostname(existing_hostname=current_hostname, new_hostname=new_hostname) is False:
            return False

        return True


    def __get_hostname(self):
        hostname = ""

        try:
            with open(HOSTNAME_FILE_PATH, SystemDefinitions.FILE_READ_MODE) as hostname_file:
                hostname = hostname_file.read()
        except Exception as exceptions:
            self.__logger.error(exceptions)
            hostname = ""

        return hostname


    def __get_mac_address(self):
        mac_address = ""
        interface_information_list = self.__interface_information

        if interface_information_list != "":
            for interface in interface_information_list:
                if interface[SYSTEM_INTERFACE_INFORMATION_INTERFACE_INDEX_KEY] == FIRST_WAN_INTERFACE_INDEX_VALUE:
                    mac_address = interface[SYSTEM_INTERFACE_INFORMATION_INTERFACE_ADDRESS_KEY]

        return mac_address


    def __get_os_version(self):
        version = ""

        try:
            os_info_command_result = subprocess.run(OS_INFO_COMMAND, shell=True, capture_output=True, check=True)
            version = ((os_info_command_result.stdout).decode("utf-8")).strip()
        except Exception as exceptions:
            self.__logger.error(exceptions)

        return version


    def __get_cpu_information(self):
        cpu_info = ""

        try:
            cpu_info_command_result = subprocess.run(CPU_INFO_COMMAND, shell=True, capture_output=True, check=True)

            if cpu_info_command_result.returncode == 0:
                cpu_info_output = (cpu_info_command_result.stdout).decode("utf-8")
                cpu_info = json.loads(cpu_info_output)

        except Exception as exceptions:
            self.__logger.error(exceptions)

        return cpu_info


    def __get_interface_information(self):
        interface_information_output = ""

        try:
            interface_information_command_result = subprocess.run(SHOW_INTERFACE_INFORMATION_COMMAND, capture_output=True, shell=True, check=True)

            if interface_information_command_result.returncode == 0:
                interface_information_output = (interface_information_command_result.stdout).decode("utf-8")
                interface_information_list = json.loads(interface_information_output)

        except Exception as exceptions:
            self.__logger.error(exceptions)

        return interface_information_list


    def __replace_hostname(self, existing_hostname, new_hostname):

        new_data = ""
        existing_data = ""

        try:
            with open(HOSTNAME_FILE_PATH, SystemDefinitions.FILE_READ_MODE) as hostname_file:
                existing_data = hostname_file.read()

            new_data = existing_data.replace(existing_hostname, new_hostname)

            with open(HOSTNAME_FILE_PATH, SystemDefinitions.FILE_WRITE_MODE) as hostname_file:
                hostname_file.write(new_data)

            existing_data = ""

            with open(HOSTS_FILE_PATH, SystemDefinitions.FILE_READ_MODE) as hosts_file:
                existing_data = hosts_file.read()

            new_data = existing_data.replace(existing_hostname, (new_hostname + "\n"))

            with open(HOSTS_FILE_PATH, SystemDefinitions.FILE_WRITE_MODE) as hosts_file:
                hosts_file.write(new_data)

        except Exception as exceptions:
            self.__logger.error(exceptions)
            return False

        return True


    def __create_system_configuration_json_file(self):
        interface_info = self.__interface_information
        parsed_interface_info = self.__parsed_interface_info

        cpu_info = self.__get_cpu_information()
        os_version = self.__get_os_version()

        if not cpu_info:
            return False

        if not os_version:
            return False

        physical_wan_interface_list = parsed_interface_info[PHYSICAL_INTERFACE_KEY][PHYSICAL_WAN_INTERFACE_KEY]
        physical_lan_interface_list = parsed_interface_info[PHYSICAL_INTERFACE_KEY][PHYSICAL_LAN_INTERFACE_KEY]
        tap_interface_list = parsed_interface_info[TAP_INTERFACE_KEY]
        tun_interface_list = parsed_interface_info[TUNNEL_INTERFACE_KEY]

        wan_interface_list = physical_wan_interface_list + tun_interface_list + tap_interface_list

        if (not wan_interface_list) and (not physical_lan_interface_list):
            return False

        if self.__generate_system_configuration_json(uuid=self.__uuid, os_version=os_version,
                                                     mac_address=self.__mac_address, \
                                                     device_model=SystemDefinitions.DEVICE_MODEL, \
                                                     wan_interface_list=wan_interface_list, \
                                                     lan_interface_list=physical_lan_interface_list, \
                                                     operation_mode=SystemDefinitions.OPERATION_MODE, \
                                                     cpu_info=cpu_info, ip_info=interface_info) is False:
            return False

        return True


    def __get_parsed_interface_info(self):
        parsed_interface_info_dic = {}

        temp_interface_information = []
        temp_interface_information = self.__interface_information

        tap_interface_list = []
        bridge_interface_list = []
        tun_interface_list = []
        vlan_interface_list = []
        wireless_interface_list = []
        physical_interface_list = []

        try:
            # sort the given array
            temp_interface_information.sort(key=lambda interface: interface[SYSTEM_INTERFACE_INFORMATION_INTERFACE_INDEX_KEY])
            sorted_interface_information = temp_interface_information

            for interface_info in sorted_interface_information:
                if (re.findall(TAP_INTERFACE_PREFIX_VALUE, interface_info[SYSTEM_INTERFACE_INFORMATION_INTERFACE_NAME_KEY])) != []:
                    tap_interface_list.append(interface_info[SYSTEM_INTERFACE_INFORMATION_INTERFACE_NAME_KEY])

            for interface_info in sorted_interface_information:
                if (re.findall(TUNNEL_INTERFACE_PREFIX_VALUE, interface_info[SYSTEM_INTERFACE_INFORMATION_INTERFACE_NAME_KEY])) != []:
                    tun_interface_list.append(interface_info[SYSTEM_INTERFACE_INFORMATION_INTERFACE_NAME_KEY])

            for interface_info in sorted_interface_information:
                if (re.findall(VLAN_INTERFACE_MATCH_VALUE, interface_info[SYSTEM_INTERFACE_INFORMATION_INTERFACE_NAME_KEY])) != []:
                    vlan_interface_list.append(interface_info[SYSTEM_INTERFACE_INFORMATION_INTERFACE_NAME_KEY])

            for interface_info in sorted_interface_information:
                if (re.findall(BRIDGE_INTERFACE_PREFIX_VALUE, interface_info[SYSTEM_INTERFACE_INFORMATION_INTERFACE_NAME_KEY])) != []:
                    bridge_interface_list.append(interface_info[SYSTEM_INTERFACE_INFORMATION_INTERFACE_NAME_KEY])

            for interface_info in sorted_interface_information:
                if (re.findall(WIRELESS_INTERFACE_PREFIX_VALUE, interface_info[SYSTEM_INTERFACE_INFORMATION_INTERFACE_NAME_KEY])) != []:
                    wireless_interface_list.append(interface_info[SYSTEM_INTERFACE_INFORMATION_INTERFACE_NAME_KEY])

            for interface_info in sorted_interface_information:
                if ((interface_info[SYSTEM_INTERFACE_INFORMATION_INTERFACE_NAME_KEY] != LOOPBACK_INTERFACE_NAME) and \
                    (interface_info[SYSTEM_INTERFACE_INFORMATION_INTERFACE_NAME_KEY] not in wireless_interface_list) and \
                    (interface_info[SYSTEM_INTERFACE_INFORMATION_INTERFACE_NAME_KEY] not in tap_interface_list) and \
                    (interface_info[SYSTEM_INTERFACE_INFORMATION_INTERFACE_NAME_KEY] not in tun_interface_list) and \
                    (interface_info[SYSTEM_INTERFACE_INFORMATION_INTERFACE_NAME_KEY] not in bridge_interface_list) and \
                    (interface_info[SYSTEM_INTERFACE_INFORMATION_INTERFACE_NAME_KEY] not in vlan_interface_list)) is True:

                    physical_interface_list.append(interface_info[SYSTEM_INTERFACE_INFORMATION_INTERFACE_NAME_KEY])

            physical_wan_interface_list = [physical_interface_list[i] for i in range(len(physical_interface_list)) if i < SystemDefinitions.WAN_INTERFACE_COUNT]
            physical_lan_interface_list = [physical_interface_list[i] for i in range(len(physical_interface_list)) if i >= SystemDefinitions.WAN_INTERFACE_COUNT]

            parsed_interface_info_dic[PHYSICAL_INTERFACE_KEY] = {}
            parsed_interface_info_dic[PHYSICAL_INTERFACE_KEY][PHYSICAL_WAN_INTERFACE_KEY] = physical_wan_interface_list
            parsed_interface_info_dic[PHYSICAL_INTERFACE_KEY][PHYSICAL_LAN_INTERFACE_KEY] = physical_lan_interface_list
            parsed_interface_info_dic[WIRELESS_INTERFACE_KEY] = wireless_interface_list
            parsed_interface_info_dic[VLAN_INTERFACE_KEY] = vlan_interface_list
            parsed_interface_info_dic[BRIDGE_INTERFACE_KEY] = bridge_interface_list
            parsed_interface_info_dic[TUNNEL_INTERFACE_PREFIX_VALUE] = tun_interface_list
            parsed_interface_info_dic[TAP_INTERFACE_KEY] = tap_interface_list
        except Exception as exceptions:
            self.__logger.info(exceptions)
            return parsed_interface_info_dic

        return parsed_interface_info_dic


    def __generate_system_configuration_json(self, uuid, os_version, mac_address,
                                             device_model, wan_interface_list, lan_interface_list,
                                             cpu_info, ip_info, operation_mode=SystemDefinitions.OPERATION_MODE):

        system_information_key = "system_information"
        system_provisioing_server_uri_key = "provisioning_server_uri"

        uuid_key = "uuid"
        os_version_key = "os_version"
        mac_address_key = "mac_address"
        model_key = "model"
        lan_interface_key = "lan_interfaces"
        wan_interface_key = "wan_interfaces"
        cpu_info_key = "cpu_info"
        ip_info_key = "ip_info"

        system_configuration_dict = {}
        system_information_dict = {}
        system_information_dict[uuid_key] = uuid
        system_information_dict[os_version_key] = os_version
        system_information_dict[mac_address_key] = mac_address
        system_information_dict[model_key] = device_model
        system_information_dict[lan_interface_key] = lan_interface_list
        system_information_dict[wan_interface_key] = wan_interface_list
        system_information_dict[cpu_info_key] = cpu_info
        system_information_dict[ip_info_key] = ip_info

        system_configuration_dict[system_information_key] = system_information_dict

        if operation_mode == SystemDefinitions.DEVELOPMENT_SYSTEM_OPERATION_MODE:
            system_configuration_dict[system_provisioing_server_uri_key] = SystemDefinitions.DEVELOPMENT_PROVISIONING_URL
        elif operation_mode == SystemDefinitions.PRODUCTION_SYSTEM_OPERATION_MODE:
            system_configuration_dict[system_provisioing_server_uri_key] = SystemDefinitions.PRODUCTION_PROVISIONING_URL

        try:
            with open(SystemDefinitions.SYS_CONFIG_FILE_PATH_NAME, SystemDefinitions.FILE_WRITE_MODE) as configuration_file:
                json.dump(system_configuration_dict, configuration_file)
        except Exception as exceptions:
            self.__logger.error(exceptions)
            # Remove file if there is any exception raises
            HelperFunction.remove_file_if_exists(filepath=SystemDefinitions.SYS_CONFIG_FILE_PATH_NAME, logger_object=self.__logger)
            return False

        return True


    def __generate_ignore_carrier_configuration(self, physical_lan_interface_list):
        ignore_carrier_configuration_file = "chiefnet-ignore-carier.conf"
        network_manager_configuration_filepath = "/etc/NetworkManager/conf.d"
        static_ignore_carrier_configuration = "[main]\nignore-carrier="
        interface_name_key = "interface-name:="
        comman_delimiter = ","

        ignore_carrier_configuration_filepath = network_manager_configuration_filepath + os.path.sep + ignore_carrier_configuration_file

        physical_lan_interface_count = len(physical_lan_interface_list)

        temp_configuration_string = ""
        for i in range(physical_lan_interface_count):
            if i > 0:
                temp_configuration_string = temp_configuration_string + comman_delimiter + interface_name_key + str(physical_lan_interface_list[i])
            else:
                temp_configuration_string = interface_name_key + str(physical_lan_interface_list[i])

        configuration_data = static_ignore_carrier_configuration + temp_configuration_string
        try:
            with open(ignore_carrier_configuration_filepath, "w") as ignore_carrier_file:
                ignore_carrier_file.write(configuration_data)
        except Exception as exceptions:
            self.__logger.error(exceptions)
            return False

        return True
