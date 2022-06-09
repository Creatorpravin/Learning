from asyncio import subprocess
import os
import subprocess
import json

# interface = open('SystemConfiguration.json')
# data = json.load(interface)resd

system_configuration = open('SystemConfiguration.json')
data = json.load(system_configuration)

system_information=data['system_information']
lan_interfaces = system_information['lan_interfaces']

for i in range(len(lan_interfaces)):
   interface = lan_interfaces[i]

   #interface = 'wlp0s20f3'
   cmd = "ip addr show "+interface



   status = os.popen(cmd).read().split("state ")[1].split(" group")[0]

   #print(status)

   if status=="DOWN":
     print("Interface is",status,ip)
   else:
     ip = os.popen(cmd).read().split("inet ")[1].split("brd")[0]
     print(ip)

