import json
import os

try:
    if os.path.exists("test.json") is True:
        with open(file="test.json", mode="r") as nmap_read:
            nmap_json = json.loads(nmap_read.read())
            eno1_total_host_range = nmap_json[0]["eno1"]["nmaprun"]["runstats"]["hosts"]["@up"]
            enp4s0_total_host_range = nmap_json[1]["enp4s0"]["nmaprun"]["runstats"]["hosts"]["@up"]

            if int(enp4s0_total_host_range) <= 1:
                with open("json_out.json", "w") as json_file:
                    json_file.write('[')
                    for eno1_host_count in range(int(eno1_total_host_range)):
                        eno1_nmap_dict = {}
                        eno1_data_json = nmap_json[0]["eno1"]["nmaprun"]["host"][eno1_host_count]
                        status_json = eno1_data_json['status']['@state']
                        address_json = eno1_data_json['address']['@addr']
                        eno1_nmap_dict["dev"] = "eno1"
                        eno1_nmap_dict["address"] = address_json
                        eno1_nmap_dict["status"] = status_json
                      #   if (host_count==int(total_range)-1):
                      #       json_file.write(json.dumps(nmap_dict))
                      #   else:
                        json_file.write(json.dumps(eno1_nmap_dict)+',')

                    for enp4s0_host_count in range(int(enp4s0_total_host_range)):
                        enp4s0_nmap_dict = {}
                        # [enp4s0_host_count]
                        enp4s0_data_json = nmap_json[1]["enp4s0"]["nmaprun"]["host"]
                        status_json = enp4s0_data_json['status']['@state']
                        address_json = enp4s0_data_json['address']['@addr']
                        enp4s0_nmap_dict["dev"] = "enp4s0"
                        enp4s0_nmap_dict["address"] = address_json
                        enp4s0_nmap_dict["status"] = status_json
                        # if (enp4s0_host_count == int(enp4s0_total_host_range)-1):
                        #     json_file.write(json.dumps(enp4s0_nmap_dict))
                        # else:
                        json_file.write(json.dumps(enp4s0_nmap_dict))
                    json_file.write(']')
            else:
                with open("json_out.json", "w") as json_file:
                    json_file.write('[')
                    for eno1_host_count in range(int(eno1_total_host_range)):
                        eno1_nmap_dict = {}
                        eno1_data_json = nmap_json[0]["eno1"]["nmaprun"]["host"][eno1_host_count]
                        status_json = eno1_data_json['status']['@state']
                        address_json = eno1_data_json['address']['@addr']
                        eno1_nmap_dict["dev"] = "eno1"
                        eno1_nmap_dict["address"] = address_json
                        eno1_nmap_dict["status"] = status_json
                      #   if (host_count==int(total_range)-1):
                      #       json_file.write(json.dumps(nmap_dict))
                      #   else:
                        json_file.write(json.dumps(eno1_nmap_dict)+',')

                    for enp4s0_host_count in range(int(enp4s0_total_host_range)):
                        enp4s0_nmap_dict = {}
                        # [enp4s0_host_count]
                        enp4s0_data_json = nmap_json[1]["enp4s0"]["nmaprun"]["host"][enp4s0_host_count]
                        status_json = enp4s0_data_json['status']['@state']
                        address_json = enp4s0_data_json['address']['@addr']
                        enp4s0_nmap_dict["dev"] = "enp4s0"
                        enp4s0_nmap_dict["address"] = address_json
                        enp4s0_nmap_dict["status"] = status_json
                        if (enp4s0_host_count == int(enp4s0_total_host_range)-1):
                            json_file.write(json.dumps(enp4s0_nmap_dict))
                        else:
                            json_file.write(json.dumps(enp4s0_nmap_dict)+',')
                    json_file.write(']')
except Exception as exceptions:
    print(exceptions)
