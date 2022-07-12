import subprocess
import json
import os

dnsmasq_contents = []
ip_neigh = "ip -json neigh show"
reachable = ["REACHABLE"]


def get_hostname(file_path):
    result = subprocess.Popen(ip_neigh, shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, universal_newlines=True)

    json_out, json_err = result.communicate()
    if os.path.exists(file_path) is True:
        with open(file=file_path, mode="r") as dnsmasq_data:
            dnsmasq_contents = dnsmasq_data.readlines()
        for lines in dnsmasq_contents[0:]:
            dnsmasq_contents.append(lines.split())
    else:
      print(file_path+"File path is not exist")
    try:
        ipneig_json = json.loads(json_out)
        for ipneig_data in ipneig_json:
            if ipneig_data['state'] == reachable:
                for dnsmasq_data in dnsmasq_contents:
                    if dnsmasq_data[2] == ipneig_data['dst']:
                        if dnsmasq_data[3] != '*':
                            print("active_hosts,interface=" +
                                  ipneig_data['dev']+",ip_address="+dnsmasq_data[2]+" active_host="+'"'+dnsmasq_data[3]+'"')
                        else:
                            print("active_hosts,interface=" +
                                  ipneig_data['dev']+",ip_address="+dnsmasq_data[2]+" active_host=-")
    except Exception as exceptions:
        print(exceptions)


if __name__ == "__main__":
    get_hostname("/var/lib/misc/dnsmasq.leases")
