from os import popen
import subprocess
import xmltodict
import json
import get_interface_ip
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
    data_dict = xmltodict.parse(xml_file.read())
    xml_file.close()

#data_dict = xmltodict.parse(out)

json_data = json.dumps(data_dict)

#print(json_data)

with open("nmap.json", "w") as json_file:
    json_file.write(json_data)
    json_file.close()