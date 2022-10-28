#!/usr/bin/env python
import subprocess
import json
import os

DEFAULT_SYSTEM_CONFIGURATION_FILE = "/etc/telegraf/custom_scripts/SystemConfiguration.json"


def get_hostname():
    LAN_INTERFACES = lan_interface_list()
    if len(LAN_INTERFACES):
        try:
            for lan_data in LAN_INTERFACES:
                ip_neigh = "ip -json neigh show dev " + lan_data + " nud reachable"
                result = subprocess.Popen(ip_neigh, shell=True, stdout=subprocess.PIPE,
                                          stderr=subprocess.PIPE, universal_newlines=True)
                json_out, json_err = result.communicate()
                if result.returncode == 0:
                    ipneig_json = json.loads(json_out)
                    if len(ipneig_json) == 0:
                        pass
                    else:
                        for ipneigh_data in ipneig_json:
                            get_nslookup = nslookup(ipneigh_data['dst'])
                            if get_nslookup == False:
                                get_nbtscan = nbtscan(ipneigh_data['dst'])
                                if get_nbtscan == False:
                                    print("active_hosts,interface=" +
                                          lan_data+",ip_address="+ipneigh_data['dst']+' host_name=\"-\",status="REACHABLE"')
                                elif get_nbtscan == "<unknown>":
                                    print("active_hosts,interface=" +
                                          lan_data+",ip_address="+ipneigh_data['dst']+' host_name=\"-\",status="REACHABLE"')
                                else:
                                    print("active_hosts,interface=" +
                                          lan_data+",ip_address="+ipneigh_data['dst']+" host_name="+'"'+get_nbtscan+'",status="REACHABLE"')
                            else:
                                print("active_hosts,interface=" +
                                      lan_data+",ip_address="+ipneigh_data['dst']+" host_name="+'"'+get_nslookup.replace(".", "")+'",status="REACHABLE"')
                else:
                    pass
        except Exception as exception:
            pass
    else:
        pass


def lan_interface_list():
    try:
        if os.path.exists(DEFAULT_SYSTEM_CONFIGURATION_FILE) is True:
            with open(file=DEFAULT_SYSTEM_CONFIGURATION_FILE, mode="r") as system_config:
                system_config_json = json.loads(system_config.read())
                lan_interfaces = system_config_json["system_information"]["lan_interfaces"]
                return lan_interfaces
        else:
            lan_interfaces = []
            return []
    except Exception as exceptions:
        lan_interfaces = []
    return []


def nbtscan(ip):
    nbtscan_command = "nbtscan -r "+ip
    try:
        nbtscan_communication = subprocess.Popen(nbtscan_command, shell=True, stdout=subprocess.PIPE,
                                                 stderr=subprocess.PIPE, universal_newlines=True)
        nbtscan_out, nbtscan_err = nbtscan_communication.communicate()
        nbtscan_list = nbtscan_out.split()
        if nbtscan_communication.returncode == 0:
            if len(nbtscan_list) > 18:
                return (nbtscan_list[18])
            else:
                return False
        else:
            return False
    except Exception as exception:
        return False


def nslookup(ip):
    nslookup_command = "nslookup " + ip + " 127.0.0.1"
    try:
        nslookup_communication = subprocess.Popen(
            nslookup_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        nslookup_out, nslookup_err = nslookup_communication.communicate()
        nslookup_list = nslookup_out.split()
        if nslookup_communication.returncode == 0:
            result = nslookup_list[len(nslookup_list) - 1]
            return result
        else:
            return False
    except Exception as exception:
        return False


if __name__ == "__main__":
    get_hostname()
