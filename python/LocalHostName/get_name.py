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
        ipneig_json = json.loads(json_out)
        for ipneig_data in ipneig_json:
            
            get_nbtscan = nbtscan(ipneig_data('dst'))

            if get_nbtscan == False:
                print("active_hosts,interface=" +
                      ipneig_data['dev']+",ip_address="+dnsmasq_data[2]+' host_name=\"-\",status="REACHABLE"')
            elif get_nbtscan == "<unknown>":
                print("active_hosts,interface=" +
                      ipneig_data['dev']+",ip_address="+dnsmasq_data[2]+' host_name=\"-\",status="REACHABLE"')
            else:
                print("active_hosts,interface=" +
                      ipneig_data['dev']+",ip_address="+dnsmasq_data[2]+" host_name="+'"'+get_nbtscan+'",status="REACHABLE"')
        return
    try:
        ipneig_json_0 = json.loads(json_out)
        for ipneig_data_0 in ipneig_json_0:
            if ipneig_data_0['state'] == reachable:
                for dnsmasq_data in dnsmasq_contents:
                    if dnsmasq_data[2] == ipneig_data['dst']:
                        status = str(ipneig_data['state'])
                        if dnsmasq_data[3] != '*':
                            print("active_hosts,interface=" +
                                  ipneig_data_0['dev']+",ip_address="+dnsmasq_data[2]+" host_name="+'"'+dnsmasq_data[3]+'",status= "REACHABLE"')
                        else:
                            print("active_hosts,interface=" +
                                  ipneig_data_0['dev']+",ip_address="+dnsmasq_data[2]+' host_name=\"-\",status="REACHABLE"')
    except Exception as exceptions:
        print(exceptions)


def nbtscan(ip):

    nbtscan_command = "sudo nbtscan -r "+ip

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


if __name__ == "__main__":
    get_hostname("/var/lib/misc/dnsmasq.leases")
