import subprocess
import os
import json
import xmltodict

DEFAULT_SYSTEM_CONFIGURATION_FILE = "/home/chiefnet/ChiefNet/ConfigurationFiles/SystemConfiguration.json"


def get_lan_interface_list() -> list:
    """
    This Function is used to get the LAN interface list from the SystemConfiguration.json
    """

    lan_interface_key = "lan_interfaces"
    system_configuration_json = {}
    lan_interface_list = []

    try:
        if os.path.exists(DEFAULT_SYSTEM_CONFIGURATION_FILE) is True:
            with open(file=DEFAULT_SYSTEM_CONFIGURATION_FILE, mode="r") as sys_config_file:
                system_configuration_json = json.loads(sys_config_file.read())
                lan_interface_list = system_configuration_json["system_information"][lan_interface_key]
    except Exception as exceptions:
        lan_interface_list = []
        print(exceptions)

    return lan_interface_list


def get_interfaces_network(interfaces_list: list) -> dict:
    """
    This function get the interface list as the argument and return the interface and its network as dictionary
    """
    interface_ip_dict = {}

    for interface in interfaces_list:
        ip_command = "ip --json address show dev " + str(interface)

        result = subprocess.run(ip_command, shell=True, capture_output=True)

        if result.returncode == 0:
            temp = (result.stdout).decode("utf-8")
            temp_dic = (json.loads(temp))[0]

            ip_address = temp_dic["addr_info"][0]["local"] + \
                "/" + str(temp_dic["addr_info"][0]["prefixlen"])
            interface_ip_dict[interface] = ip_address

    return interface_ip_dict


def nmap(interface, network):

    nmap_command = "nmap " + network + " -sn -PR -oX  " + interface + ".xml"
    try:
        result = subprocess.run(nmap_command, shell=True, capture_output=True)

        if result.returncode != 0:
            print(result.stdout)

    except Exception as exceptions:
        print(exceptions)


interface_lists = get_lan_interface_list()
# print(interface_lists)

network_dict = get_interfaces_network(interface_lists)
# print(network_dict)

for key, value in network_dict.items():
    nmap(key, value)


def convert_xml_to_json(interface_list):
    
   # This function get the interface list as the argument and append .xml to get xml file
   # return output in json format
    

    with open(interface_list[0]+".xml") as xml_file:
        data_dict_0 = xmltodict.parse(xml_file.read())
        xml_file.close()

    with open(interface_list[1]+".xml") as xml_file:
        data_dict_1 = xmltodict.parse(xml_file.read())
        xml_file.close()

    json_data_0 = json.dumps(data_dict_0)
    json_data_1 = json.dumps(data_dict_1)

    with open("nmap.json", "w") as json_file:
        json_file.write('[{'+'"{}":'.format(interface_list[0])) 
        json_file.write(json_data_0)
        json_file.write('},')
        json_file.write('{'+'"{}":'.format(interface_list[1])) 
        json_file.write(json_data_1)
        json_file.write('}]')
        json_file.close()


convert_xml_to_json(interface_list=interface_lists)


def format_json_file(interface_list, json_file):

   # This function get the interface list as the argument and get json file to read
   # and create new formated json output

    try:
        if os.path.exists(json_file) is True:
            with open(file=json_file, mode="r") as nmap_read:
                nmap_json = json.loads(nmap_read.read())
                interface1_total_host_range = nmap_json[0][interface_list[0]
                                                     ]["nmaprun"]["runstats"]["hosts"]["@up"]
                interface2_total_host_range = nmap_json[1][interface_list[1]
                                                       ]["nmaprun"]["runstats"]["hosts"]["@up"]
                if int(interface1_total_host_range) <= 1 and int(interface2_total_host_range) <= 1:
                    with open("json_out.json", "w") as json_file:
                        json_file.write('[')
                        print('[')
                        for interface1_host_count in range(int(interface1_total_host_range)):
                            interface1_nmap_dict = {}
                            interface1_data_json = nmap_json[0][interface_list[0]
                                                          ]["nmaprun"]["host"]
                            status_json = interface1_data_json['status']['@state']
                            address_json = interface1_data_json['address']['@addr']
                            interface1_nmap_dict["dev"] = interface_list[0]
                            interface1_nmap_dict["address"] = address_json
                            interface1_nmap_dict["status"] = status_json
                            json_file.write(json.dumps(interface1_nmap_dict)+',')
                            print(json.dumps(interface1_nmap_dict)+',')

                        for interface2_host_count in range(int(interface2_total_host_range)):
                            interface2_nmap_dict = {}
                            # [enp4s0_host_count]
                            enp4s0_data_json = nmap_json[1][interface_list[1]
                                                            ]["nmaprun"]["host"]
                            status_json = interface2_data_json['status']['@state']
                            address_json = interface2_data_json['address']['@addr']
                            interface2_nmap_dict["dev"] = interface_list[1]
                            interface2_nmap_dict["address"] = address_json
                            interface2_nmap_dict["status"] = status_json
                            json_file.write(json.dumps(interface2_nmap_dict))
                            print(json.dumps(interface2_nmap_dict))
                        json_file.write(']')
                elif int(interface2_total_host_range) <= 1:
                    with open("json_out.json", "w") as json_file:
                        json_file.write('[')
                        print('[')
                        for interface1_host_count in range(int(interface1_total_host_range)):
                            interface1_nmap_dict = {}
                            interface1_data_json = nmap_json[0][interface_list[0]
                                                          ]["nmaprun"]["host"][interface1_host_count]
                            status_json = interface1_data_json['status']['@state']
                            address_json = interface1_data_json['address']['@addr']
                            interface1_nmap_dict["dev"] = interface_list[0]
                            interface1_nmap_dict["address"] = address_json
                            interface1_nmap_dict["status"] = status_json
                            json_file.write(json.dumps(interface1_nmap_dict)+',')
                            print(json.dumps(interface1_nmap_dict)+',')

                        for interface2_host_count in range(int(interface2_total_host_range)):
                            interface2_nmap_dict = {}
                            # [enp4s0_host_count]
                            interface2_data_json = nmap_json[1][interface_list[1]
                                                            ]["nmaprun"]["host"]
                            status_json = interface2_data_json['status']['@state']
                            address_json = interface2_data_json['address']['@addr']
                            interface2_nmap_dict["dev"] = interface_list[1]
                            interface2_nmap_dict["address"] = address_json
                            interface2_nmap_dict["status"] = status_json
                            json_file.write(json.dumps(interface2_nmap_dict))
                            print(json.dumps(interface2_nmap_dict))
                        json_file.write(']')
                        print(']')
                elif int(interface1_total_host_range) <= 1:
                    with open("json_out.json", "w") as json_file:
                        json_file.write('[')
                        print('[')
                        for interface1_host_count in range(int(interface1_total_host_range)):
                            interface1_nmap_dict = {}
                            interface1_data_json = nmap_json[0][interface_list[0]
                                                          ]["nmaprun"]["host"]
                            status_json = interface1_data_json['status']['@state']
                            address_json = interface1_data_json['address']['@addr']
                            interface1_nmap_dict["dev"] = interface_list[0]
                            interface1_nmap_dict["address"] = address_json
                            interface1_nmap_dict["status"] = status_json
                            json_file.write(json.dumps(interface1_nmap_dict)+',')
                            print(json.dumps(interface1_nmap_dict)+',')

                        for interface2_host_count in range(int(interface2_total_host_range)):
                            interface2_nmap_dict = {}
                            interface2_data_json = nmap_json[1][interface_list[1]
                                                            ]["nmaprun"]["host"][interface2_host_count]
                            status_json = interface2_data_json['status']['@state']
                            address_json = interface2_data_json['address']['@addr']
                            interface2_nmap_dict["dev"] = interface_list[1]
                            interface2_nmap_dict["address"] = address_json
                            interface2_nmap_dict["status"] = status_json
                            if (interface2_host_count == int(interface2_total_host_range)-1):
                                json_file.write(json.dumps(interface2_nmap_dict))
                                print(json.dumps(interface2_nmap_dict))
                            else:
                                json_file.write(
                                    json.dumps(interface2_nmap_dict)+',')
                                print(json.dumps(interface2_nmap_dict)+',')
                        json_file.write(']')
                        print(']')
                else:
                    with open("json_out.json", "w") as json_file:
                        json_file.write('[')
                        print('[')
                        for interface1_host_count in range(int(interface1_total_host_range)):
                            interface1_nmap_dict = {}
                            interface1_data_json = nmap_json[0][interface_list[0]
                                                          ]["nmaprun"]["host"][interface1_host_count]
                            status_json = interface1_data_json['status']['@state']
                            address_json = interface1_data_json['address']['@addr']
                            interface1_nmap_dict["dev"] = interface_list[0]
                            interface1_nmap_dict["address"] = address_json
                            interface1_nmap_dict["status"] = status_json
                            json_file.write(json.dumps(interface1_nmap_dict)+',')
                            print(json.dumps(interface1_nmap_dict)+',')

                        for interface2_host_count in range(int(interface2_total_host_range)):
                            interface2_nmap_dict = {}
                            interface2_data_json = nmap_json[1][interface_list[1]
                                                            ]["nmaprun"]["host"][interface2_host_count]
                            status_json = interface2_data_json['status']['@state']
                            address_json = interface2_data_json['address']['@addr']
                            interface2_nmap_dict["dev"] = interface_list[1]
                            interface2_nmap_dict["address"] = address_json
                            interface2_nmap_dict["status"] = status_json
                            if (interface2_host_count == int(interface2_total_host_range)-1):
                                json_file.write(json.dumps(interface2_nmap_dict))
                                print(json.dumps(interface2_nmap_dict))
                            else:
                                json_file.write(
                                    json.dumps(interface2_nmap_dict)+',')
                                print(json.dumps(interface2_nmap_dict)+',')
                        json_file.write(']')
                        print(']')
    except Exception as exceptions:
        print(exceptions)


format_json_file(interface_list=interface_lists, json_file="nmap.json")
