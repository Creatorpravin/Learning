from dataclasses import dataclass
import subprocess
import json
import os


ip_neigh = "ip -json neigh show"
reachable = ["REACHABLE"]
 
result = subprocess.Popen(ip_neigh, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

json_out, json_err = result.communicate()

ipneig_json=json.loads(json_out)
if ipneig_json[0]['state'] == reachable:
   print(ipneig_json[0]['dst'])
   print(ipneig_json[0]['state'] )

for date in ipneig_json:
  if date['state'] == reachable:
    print(date)
  
