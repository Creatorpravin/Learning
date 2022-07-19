from re import sub
import subprocess
import json
import os

DEFAULT_SYSTEM_CONFIGURATION_FILE = "/home/chiefnet/ChiefNet/ConfigurationFiles/SystemConfiguration.json"


def get_hostname():

    LAN_INTERFACES = lan_interface_list()

    for lan_data in LAN_INTERFACES:
        ip_neigh = "ip -json neigh show dev " + lan_data + " nud reachable"
        result = subprocess.Popen(ip_neigh, shell=True, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE, universal_newlines=True)
        json_out, json_err = result.communicate()
        ipneig_json = json.loads(json_out)
#        print(ipneig_json)
        # for ipneigh_data in ipneig_json:
        # print(ipneigh_data['dst'])

        for ipneigh_data in ipneig_json:
            #          print(ipneigh_data)
            get_nslookup = nslookup(ipneigh_data['dst']) 
            # print(get_nbtscan)

            if get_nslookup == False:
                get_nbtscan = nbtscan(ipneigh_data['dst'])
                # print(get_nslookup)
                if get_nbtscan == False :
                    
                    # print(get_nslookup)
                    print("active_hosts,interface=" +
                          lan_data+",ip_address="+ipneigh_data['dst']+' host_name=\"-\",status="REACHABLE"')

                elif get_nbtscan == "<unknown>":
                    
                    # print(get_nslookup)
                    print("active_hosts,interface=" +
                          lan_data+",ip_address="+ipneigh_data['dst']+' host_name=\"-\",status="REACHABLE"')
                else:
                    print(get_nbtscan)
                    print("active_hosts,interface=" +
                          lan_data+",ip_address="+ipneigh_data['dst']+" host_name="+'"'+get_nbtscan+'",status="REACHABLE"')
            else:
                print("active_hosts,interface=" +
                      lan_data+",ip_address="+ipneigh_data['dst']+" host_name="+'"'+get_nslookup+'",status="REACHABLE"')


def lan_interface_list():
    try:
        if os.path.exists(DEFAULT_SYSTEM_CONFIGURATION_FILE) is True:
            with open(file=DEFAULT_SYSTEM_CONFIGURATION_FILE, mode="r") as system_config:
                system_config_json = json.loads(system_config.read())
                lan_interfaces = system_config_json["system_information"]["lan_interfaces"]
                return lan_interfaces
    except Exception as exceptions:
        lan_interfaces = []
        print(exceptions)


def nbtscan(ip):

    nbtscan_command = "sudo nbtscan -r "+ip
    #print('_____________inside nbtscan__________')
    nbtscan_communication = subprocess.Popen(nbtscan_command, shell=True, stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE, universal_newlines=True)

    nbtscan_out, nbtscan_err = nbtscan_communication.communicate()
    nbtscan_list = nbtscan_out.split()
    if len(nbtscan_list) > 18:
        #        print(nbtscan_list)
        return(nbtscan_list[18])
    else:
        # print(nbtscan_list)
        return False


def nslookup(ip):

    nslookup_command = "sudo nslookup "+ip+" 127.0.0.1"
    #print('_____________inside nslookup__________')
    nslookup_communication = subprocess.Popen(
        nslookup_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    nslookup_out, nslookup_err = nslookup_communication.communicate()
    nslookup_list = nslookup_out.split()
    # print(nslookup_err)
    if nslookup_communication.returncode == 0:
        result = nslookup_list[len(nslookup_list) - 1]
        return result
    else:
        return False


if __name__ == "__main__":
    get_hostname()
