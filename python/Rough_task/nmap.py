from os import popen
import subprocess
import xmltodict
import json
import get_interface_ip
import time

"""Used to run shell command in python and get the output"""

ip = format(get_interface_ip.ip)
cmd = "nmap -sn -PR "+ip+" -oX data.xml"

p1 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
out, err = p1.communicate()



if p1.returncode == 0: #used to get return value in shell 'echo $?' if == 0 means success if == other than 0 means fail 
    print("out: {0}". format(out))
    print("command : success")
else:
    print("error: {0}". format(err))
    print("command : failure")

with open("data.xml") as xml_file:
    data_dict_0 = xmltodict.parse(xml_file.read())
    xml_file.close()

with open("data.xml") as xml_file:
    data_dict_1 = xmltodict.parse(xml_file.read())
    xml_file.close()

json_data_0 = json.dumps(data_dict_0)
json_data_1 = json.dumps(data_dict_1)

#print(json_data)

with open("nmap.json", "w") as json_file:
    json_file.write('[{wlp0s20f3:')
    json_file.write(json_data_0)
    json_file.write('},')
    json_file.write('{enp4s0:')
    json_file.write(json_data_1)
    json_file.write('}]')
    json_file.close()

p1 = subprocess.Popen('cat nmap.json', shell=True,     stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
json_out, json_err = p1.communicate()

time.sleep(5)
if p1.returncode == 0: #used to get return value in shell 'echo $?' if == 0 means success if == other than 0 means fail 
    print("out: {0}". format(json_out))
    print("command : success")
else:
    print("error: {0}". format(json_err))
    print("command : failure")
