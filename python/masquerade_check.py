import subprocess
import os
import logging
import logging.handlers
import json

LOG_DIRECTORY = '/var/SDWAN/Monitoring/'

DEFAULT_LOG_FILE = 'masquerade_check.log'
DEFAULT_FILE_OPEN_MODE = 'a'   # Append mode
DEFAULT_LOG_LEVEL = logging.DEBUG  # Debug Log level
SYSLOG_ADDRESS_DIR = "/dev/log"


configuration_location = " /var/SDWAN/ConfigurationFiles/traffic-steering-configuration/"


def get_wan_list():
    sysconf_filepath = "/home/chiefnet/ChiefNet/ConfigurationFiles/SystemConfiguration.json"
    data = {}
    wan_list = []

    with open(sysconf_filepath, "r+") as fd:
        data = json.load(fd)

    wan_list = [x for x in data["system_information"]["wan_interfaces"] if "en" in x]

    return wan_list


def get_logger(logger_name,
               log_filename=DEFAULT_LOG_FILE,
               file_open_mode=DEFAULT_FILE_OPEN_MODE,
               logger_level=DEFAULT_LOG_LEVEL):

    file_and_stdout_formatter = logging.Formatter('%(asctime)s | MASQUERADE | %(message)s')

    logger = logging.getLogger(logger_name)
    logger.setLevel(logger_level)

    if not os.path.exists(LOG_DIRECTORY):
        os.makedirs(LOG_DIRECTORY + os.path.sep)

    log_file_path = LOG_DIRECTORY + os.path.sep + log_filename

    file_handler = logging.FileHandler(log_file_path, mode=file_open_mode)
    file_handler.setFormatter(file_and_stdout_formatter)
    logger.addHandler(file_handler)

    return logger


def get_iptables_details():
    iptables_cmd = "iptables -t nat -nvL"

    cmd_rslt = subprocess.run(iptables_cmd, shell=True, capture_output=True)

    if cmd_rslt.returncode == 0:
        return cmd_rslt.stdout.decode("utf-8")

    return ""


def apply_masquerade_if_not_exist(data, printy):
    try:
        if data != "":

            if "MASQUERADE" in data:
                return True
            else:
                printy.info("MASQUERADE rule not found")
                ipset_location = configuration_location + "ipset-configuration.sh"

                cmd1_rslt = subprocess.run(ipset_location, shell=True, capture_output=True)

                if cmd1_rslt.returncode == 0:
                    printy.info("Ipset Executed successfully")
                    iptables_location = configuration_location + "initial-configuration.txt"

                    iptables_cmd = "iptables-restore < " + iptables_location

                    cmd2_rslt = subprocess.run(iptables_cmd, shell=True, capture_output=True)

                    if cmd2_rslt.returncode == 0:
                        printy.info("Chiefnet IPtables applied successfully")
                        return True
                else:
                    return False

    except Exception as e:
        print(e)
        return False


def masquerade(wan_list, printy):
    for wan in wan_list:
        iptables_cmd = "iptables -t nat -A POSTROUTING -o " + wan + " -j MASQUERADE"

        cmd_rslt = subprocess.run(iptables_cmd, shell=True, capture_output=True)

        if cmd_rslt.returncode == 0:
            printy.info(f"Updated Manual Masquerade to {wan}")


printy = get_logger("masquerade")
wan_list = get_wan_list()

if apply_masquerade_if_not_exist(get_iptables_details(), printy) != True:
    printy.info(wan_list)
    masquerade(wan_list, printy)
