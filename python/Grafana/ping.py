#!/usr/bin/env python
# coding: utf-8

# In[10]:


import os
import json
import subprocess


# In[11]:


debug = 0


# In[12]:


def get_physical_interfaces(
    file_loc = r"/home/chiefnet/ChiefNet/ConfigurationFiles",
    debug = 0
    ): 
    try:        
        with open(file_loc+"/SystemConfiguration.json", "r") as f:
            system_config = json.load(f)

        # Get list from json file
        wan_interfaces_list = system_config["system_information"]["wan_interfaces"]
        lan_interfaces_list = system_config["system_information"]["lan_interfaces"]

        wifi_interfaces = []
        lan_interfaces = []
        wan_interfaces = []
        
        for interface in lan_interfaces_list:
            if(interface.lower().startswith("wl")):
                wifi_interfaces.append(interface)
            else:
                lan_interfaces.append(interface)

        wan_interfaces = [interface for interface in wan_interfaces_list 
                          if not (interface.startswith("tun") or interface.startswith("tap"))
                         ]

        return wan_interfaces, lan_interfaces, wifi_interfaces
    except Exception as e:
        if debug: 
            raise e
        else:
            pass


# In[13]:


def get_active_interfaces(interfaces,debug=0):
    """
    Function to retrieve active interfaces that are currently in UP state.
    """
    str_out = ""
    out ={}
    # Variable to store active interfaces.
    actives_interfaces =set()
    # cmd to get all the interfaces.
    command = f'ip -j address'

    # Executing the cmd
    cmd1 = subprocess.Popen(command.split(), stdout=subprocess.PIPE)

    # Parsing the json to get desired "interfaces" only if its "operstate" is "UP".
    try:
        # Decoding cmd output
        str_out = cmd1.stdout.read().decode()
        
        # Decoding to dict format
        out = json.loads(str_out)
        
        # Looping through all the interfaces.
        for i in out:
            # Checking if the interface is in desired set of interfaces.
            if ((i.get("ifname")) != None):
                if (i["ifname"] in interfaces):
                    # Add to active interfaces set if state is UP.
                    if(i["operstate"].lower() == "up"):
                        actives_interfaces.add(i["ifname"])
                    # Add to active interfaces set if state is UNKNOWN.
                    elif(i["operstate"].lower() == "unknown"):
                        actives_interfaces.add(i["ifname"])
                    # Add to logs if state is neither UP nor DOWN.    
                    elif(i["operstate"].lower() !='down'):
                        pass
                    
    except Exception as e:
        if debug: 
            raise e
        else:
            pass
    return actives_interfaces,str(str_out)


# In[14]:


def ping_data(ping_cmd,interface):   
    """
    Function prints ping values for interfaces that are in UP/UNKNOWN state.
    """
    global debug
    
    ping_data_req = ("packets transmitted","received","% packet loss")
    interface_state = "active"
    
    # Getting ping command output
    cmd2 = subprocess.run(ping_cmd.split(), stdout=subprocess.PIPE)
    # decoding output from cmd
    lines = cmd2.stdout.decode()
    lines_lst = lines.split("\n")
    # processing each lines
    ping_data_packets,ping_data_received,ping_data_loss = 0.0,0.0,0.0
    ping_min_avg_max = [0.0,0.0,0.0]
    
    for i,line in enumerate(lines_lst):
        try:
            # Getting data from packets line
            if("packets transmitted" in line or "received" in line or "% packet loss" in line):
                # Replace unwanted characters  and covert to float.
                for wrd in line.split(","):
                    if(ping_data_req[0] in wrd):
                        ping_data_packets = float(wrd.replace(ping_data_req[0],""))
                    if(ping_data_req[1] in wrd):
                        ping_data_received = float(wrd.replace(ping_data_req[1],""))
                    if(ping_data_req[2] in wrd):
                        ping_data_loss = float(wrd.replace(ping_data_req[2],""))
                
            # Getting min/avg/max data 
            elif("min/avg/max/mdev" in line):
                ping_min_avg_max = list(map(lambda x:float(x),line.split("=")[-1].split("/")[:-1]))
                
        # Skipping unwanted lines
        except Exception as e:
            if debug: 
                raise e
            else:
                pass
    # printing in line protocol
    print(f'exec_ping_status,interface={interface} minimum_response_ms={ping_min_avg_max[0]},average_response_ms={ping_min_avg_max[1]},maximum_response_ms={ping_min_avg_max[2]},loss_percentage={ping_data_loss},packet_received={ping_data_received},packet_transmited={ping_data_packets},state="{interface_state}"'
         )


# In[15]:


if __name__ == "__main__":
    
    try:
        result = get_physical_interfaces(
                r"/etc/telegraf/iftop",
                debug
                )
        
        if(result == None):
            raise Exception("No interfaces found.")
        wan_interfaces, lan_interfaces, wifi_interfaces = result
        
        interfaces = set(wan_interfaces)
        inactives_interfaces = set()
        
        # Getting active interfaces.
        actives_interfaces,out = get_active_interfaces(interfaces=interfaces,
                                                       debug=debug
                                                      )
        # getting inactive interfaces
        inactives_interfaces = interfaces - actives_interfaces
        
        # Ping data for inactive interfaces.
        for interface in inactives_interfaces:
            temp = f'exec_ping_status,interface={interface} minimum_response_ms=0.0,average_response_ms=0.0,maximum_response_ms=0.0,loss_percentage=100,packet_received=0,packet_transmited=0,state="inactive"'
            print(temp)
                
        # Printing line protocol for interfaces present.
        for interface in actives_interfaces:
            ping = f'ping 8.8.8.8 -c 1 -w 1 -I {interface}'
            # Ping data for active interfaces.
            ping_data(ping_cmd = ping,
                      interface = interface
                     )

    except Exception as e:
        if debug: 
            raise e
        else:
            pass


# In[ ]:




