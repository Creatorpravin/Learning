import json

system_configuration = open('SystemConfiguration.json')
data = json.load(system_configuration)

system_information=data['system_information']
lan_interfaces = system_information['lan_interfaces']

for i in range(len(lan_interfaces)):
   print(lan_interfaces[i])
