#!/usr/bin/env python
# -*- coding: utf-8 -*-
import geocoder as geo
import json
import subprocess
import re
import logging

CUSTOM_SCRIPT_LOCATION = "/etc/telegraf/custom_scripts/"
logging.basicConfig(filename="iftop.log", format='%(asctime)s %(message)s',
                    filemode='w')
__logger = logging.getLogger()
# def get_ip_flag(ip):
__logger.setLevel(logging.DEBUG)


def ip_locator(ip):
    __logger.info("ip_locator initialized")
    geo_ip_lookup_cmd = "geoiplookup " + str(ip)

    geo_ip_status, geo_location = execute_command(geo_ip_lookup_cmd)

    if geo_ip_status == 0:
        if "IP Address not found" in geo_location:
            return ""
        else:
            location_list = re.sub(r'[^\w]', ' ', geo_location).split(" ")
            with open(file="/etc/telegraf/custom_scripts/CountryCode.json", mode="r") as country_code:
                country_code_and_flag_list = json.load(country_code)
                for country_flag in country_code_and_flag_list:
                    if country_flag['code'] == location_list[4]:
                        return ":"+country_flag['flag']
        return ""
    else:
        return ""


def execute_command(command, decode=True):
    __logger.info("execute command initialized")
    try:
        result = subprocess.run(command, shell=True, capture_output=True)

        if result.returncode == 0:
            if decode == True:
                return result.returncode, (result.stdout).decode("utf-8")
            else:
                return result.returncode, result.stdout
        else:
            return result.returncode, ""
    except Exception as exceptions:
        return 1, ""


def bit_conversion(val):
    """
    Parsing the value in Bytes for a given value.
    """
    __logger.info("bit conversion initialized")
    val = val.lower()
    if (val[-1] == "b"):
        val = val[:-1]

        if ("g" in val):
            return val.lower().replace("g", "0"*9)
        elif ("m" in val):
            return val.lower().replace("m", "0"*6)
        elif ("k" in val):
            return val.lower().replace("k", "0"*3)
        else:
            return val
    else:
        return "0"


# def get_iftop_output(interface):
#     iftop_command = "iftop -nNb -i " + interface +" -s 1s -o 10s -L 100 -t"

#     #execution_status, execution_output = execute_command(iftop_command)
#     command = f'iftop -nNb -i {interface} -s 1s -o 10s -L 100 -t'

#     # For inserting password in cmd line
#     #cmd1 = subprocess.Popen(['echo',sudo_password], stdout=subprocess.PIPE)
#     # Getting iftop command output
#     cmd2 = subprocess.Popen(command.split(), stdout=subprocess.PIPE)

#     # decoding output from cmd
#     execution_output = cmd2.stdout.read().decode()
#     execution_status = 0
#     if execution_status == 0:
#         splited_newline_output_list = execution_output.split("\n")

#         for iteration,stdout_line in enumerate(splited_newline_output_list):
#             stdout_lst = stdout_line.split()

#             try :
#                 sender,sent_bytes,receiver,received_bytes = 0,0,0,0

#                 if(len(stdout_lst)>1):

#                     if (stdout_lst[0].isdigit()):

#                         if(len(stdout_lst) == 7):
#                             sender,sent_bytes = (stdout_lst[1],bit_conversion(val=stdout_lst[4]))

#                         nxt_stdout_line_lst = splited_newline_output_list[iteration+1].split()

#                         if(len(nxt_stdout_line_lst) == 6):
#                             receiver,received_bytes =(nxt_stdout_line_lst[0],bit_conversion(val=nxt_stdout_line_lst[3]))

#                             if (sent_bytes == "0"):
#                                 # pass
#                                 print()
#                                 print(f'iftop_traffic,interface={interface},sender={sender},receiver={receiver} receiveRate={float(received_bytes)}{1}')
#                             elif(received_bytes == "0"):
#                                 # pass
#                                 print(f'iftop_traffic,interface={interface},sender={sender},receiver={receiver} sendRate={float(sent_bytes)}')
#                             else:
#                                 # pass
#                                 print(f'iftop_traffic,interface={interface},sender={sender},receiver={receiver} sendRate={float(sent_bytes)},receiveRate={float(received_bytes)}')

#                     else:
#                         pass

#             except Exception as e:
#                 raise e

# ------------------------------------------------------------- exec


def size(val):
    """
    Parsing the value in Bytes for a given value.
    """
    __logger.info("size initialized")
    val = val.lower()
    if (val[-1] == "b"):
        val = val[:-1]

        if ("g" in val):
            return val.lower().replace("g", "0"*9)
        elif ("m" in val):
            return val.lower().replace("m", "0"*6)
        elif ("k" in val):
            return val.lower().replace("k", "0"*3)
        else:
            return val
    else:
        return "0"


def get_iftop(interface, sudo_password=None, debug=0):
    """
    Getting the iftop values and parsing it as per line protocol.
    """
    __logger.info("get iftop initialized")
    # iftop command for each interface
   # command = f'iftop -bBP -i {interface} -s 1s -o 10s -L 100 -t'
    command = f'iftop -nNb -i {interface} -s 1s -o 10s -L 100 -t'

    # For inserting password in cmd line
    #cmd1 = subprocess.Popen(['echo',sudo_password], stdout=subprocess.PIPE)
    # Getting iftop command output
    cmd2 = subprocess.Popen(command.split(), stdout=subprocess.PIPE)

    # decoding output from cmd
    lines = cmd2.stdout.read().decode()
    lines_lst = lines.split("\n")
#    print(lines)
    # Parsing each line and getting the output in line protocol.
    for i, line in enumerate(lines_lst):
        lst = line.split()
        try:
            sender, sent, receiver, received = 0, 0, 0, 0

            if (len(lst) > 1):
                if (lst[0].isdigit()):

                    if (len(lst) == 7):
                        sender, sent = (lst[1], size(val=lst[4]))

                    nxt_line_lst = lines_lst[i+1].split()

                    if (len(nxt_line_lst) == 6):

                        receiver, received = (
                            nxt_line_lst[0], size(val=nxt_line_lst[3]))

                        if (sent == "0"):
                            print()
                            print(
                                f'iftop_traffic,interface={interface},sender={sender}{ip_locator(sender)},receiver={receiver}{ip_locator(receiver)} receiveRate={float(received)}')
                        elif (received == "0"):
                            print(
                                f'iftop_traffic,interface={interface},sender={sender}{ip_locator(sender)},receiver={receiver}{ip_locator(receiver)} sendRate={float(sent)}')
                        else:
                            print(
                                f'iftop_traffic,interface={interface},sender={sender}{ip_locator(sender)},receiver={receiver}{ip_locator(receiver)} sendRate={float(sent)},receiveRate={float(received)}')

                else:
                    # Skipping unwanted lines.
                    pass
                    # append_new_line("here")

        # Handling exception and storing the output in a log file.
        except Exception as e:
            print(e)
            if debug:
                raise e
            else:
                pass

# ------------------------------------------------------------- exec


def get_active_interface_list():
    __logger.info("active interface initialized")
    device_interface_info_list = []
    active_interface_info = []

    execution_status, execution_output = execute_command("ip -json add show")

    try:
        if execution_status == 0:
            device_interface_info_list = json.loads(execution_output)

            for device_interface_info in device_interface_info_list:
                if (device_interface_info["operstate"] == "UP") or (device_interface_info["operstate"] == "UNKNOWN"):
                    active_interface_info.append(
                        device_interface_info["ifname"])

    except Exception as exceptions:
        return []

    return active_interface_info


def get_system_configuration_interface_list():
    __logger.info("system coinfiguration initialized initialized")
    wan_interface_list = []
    lan_interface_list = []

    telegraf_system_configuration_location = CUSTOM_SCRIPT_LOCATION + \
        "SystemConfiguration.json"

    try:
        with open(telegraf_system_configuration_location, "r+") as conf_file:
            system_configuration = json.load(conf_file)
            wan_interface_list = system_configuration["system_information"]["wan_interfaces"]
            lan_interface_list = system_configuration["system_information"]["lan_interfaces"]

    except Exception as exceptions:
        wan_interface_list = []
        lan_interface_list = []

    return wan_interface_list, lan_interface_list


# --------------------- main -------------------------------------
if __name__ == "__main__":
    wan_interface_list, lan_interface_list = get_system_configuration_interface_list()

    active_interface_list = get_active_interface_list()

    active_wan_interface_list = []
    active_lan_interface_list = []

    for active_interface in active_interface_list:
        if active_interface in wan_interface_list:
            active_wan_interface_list.append(active_interface)

        if active_interface in lan_interface_list:
            active_lan_interface_list.append(active_interface)

    for wan_interface in active_wan_interface_list:
        #    get_iftop_output(wan_interface)
        get_iftop(wan_interface)

    for lan_interface in active_lan_interface_list:
        #    get_iftop_output(lan_interface)
        get_iftop(lan_interface)
