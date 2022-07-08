import subprocess
import json
import os

cwd = os.getcwd()
# print(cwd)

ping_destination = "8.8.8.8"

tun_interfaces = ["tun0", "tun1", "tun2", "tun3", "tun4", "tap0", "tap1", "tap2", "tap3", "tap4"]
systemconfiguration_json = {}
output_json = {}
output_list = []

with open("/etc/telegraf/custom_scripts/SystemConfiguration.json", "r") as conf_file:
    data = conf_file.read()
    systemconfiguration_json = json.loads(data)    

for interface in systemconfiguration_json["system_information"]["wan_interfaces"]:
    if interface not in tun_interfaces:
        ping_command = "ping " + ping_destination + " -c 10 -i .200 -w 3 -I " + interface + " | pingparsing" 
        
        ping_result = subprocess.run(ping_command, shell=True, capture_output=True)

        if ping_result.returncode != 0:
            print("Error")

        output_json = json.loads((ping_result.stdout).decode("utf-8"))
        output_json["interface"] = interface

        output_list.append(output_json)


print(output_list)
