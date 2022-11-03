# #!/usr/bin/env python
# # coding: utf-8

# # In[1]:


# import os
# import json
# import subprocess
# import asyncio
# from time import sleep
# import threading
# #import datetime

# # In[2]:


# debug = 1
# sudo_password = None


# # In[3]:


# def get_physical_interfaces(
#     file_loc="/home/chiefnet/ChiefNet/ConfigurationFiles",
#     debug=0
# ):
#     try:
#         with open("SystemConfiguration.json", "r") as f:
#             system_config = json.load(f)
#         # Get list from json file
#         wan_interfaces_list = system_config["system_information"]["wan_interfaces"]
#         lan_interfaces_list = system_config["system_information"]["lan_interfaces"]

#         wifi_interfaces = []
#         lan_interfaces = []
#         wan_interfaces = []

#         for interface in lan_interfaces_list:
#             if(interface.lower().startswith("wl")):
#                 wifi_interfaces.append(interface)
#             else:
#                 lan_interfaces.append(interface)

#         wan_interfaces = [interface for interface in wan_interfaces_list
#                           if not (interface.startswith("tun"))
#                           ]

#         return wan_interfaces, lan_interfaces, wifi_interfaces
#     except Exception as e:
#         if debug:
#             raise e
#         else:
#             pass


# # In[4]:


# def get_active_interfaces(interfaces, debug=0):
#     """
#     Function to retrieve active interfaces that are currently in UP state.
#     """
#     str_out = ""
#     out = {}
#     # Variable to store active interfaces.
#     actives_interfaces = set()
#     # cmd to get all the interfaces.
#     command = f'ip -j address'

#     # Executing the cmd
#     cmd1 = subprocess.Popen(command.split(), stdout=subprocess.PIPE)

#     # Parsing the json to get desired "interfaces" only if its "operstate" is "UP".
#     try:
#         # Decoding cmd output
#         str_out = cmd1.stdout.read().decode()

#         # Decoding to dict format
#         out = json.loads(str_out)

#         # Looping through all the interfaces.
#         for i in out:
#             # Checking if the interface is in desired set of interfaces.
#             if ((i.get("ifname")) != None):
#                 if (i["ifname"] in interfaces):
#                     # Add to active interfaces set if state is UP.
#                     if(i["operstate"].lower() == "up"):
#                         actives_interfaces.add(i["ifname"])
#                     # Add to active interfaces set if state is UNKNOWN.
#                     elif(i["operstate"].lower() == "unknown"):
#                         actives_interfaces.add(i["ifname"])
#                     # Add to logs if state is neither UP nor DOWN.
#                     elif(i["operstate"].lower() != 'down'):
#                         pass

#     except Exception as e:
#         if debug:
#             raise e
#         else:
#             pass
#    # print(actives_interfaces)
#     return actives_interfaces, str(str_out)


# # In[5]:


# def size(val):
#     """
#     Parsing the value in Bytes for a given value.
#     """
#     val = val.lower()
#     if(val[-1] == "b"):
#         val = val[:-1]

#         if("g" in val):
#             return val.lower().replace("g", "0"*9)
#         elif("m" in val):
#             return val.lower().replace("m", "0"*6)
#         elif("k" in val):
#             return val.lower().replace("k", "0"*3)
#         else:
#             return val
#     else:
#         return "0"


# async def get_iftop(interface, sudo_password=None, debug=0):

#     """
#     Getting the iftop values and parsing it as per line protocol.
#     """

#     # iftop command for each interface
#     command = f'iftop -bBP -i {interface} -s 1s -o 10s -L 100 -t'
#    # print("----------------"+interface+"-------------------")
#     # For inserting password in cmd line
#     #cmd1 = subprocess.Popen(['echo',sudo_password], stdout=subprocess.PIPE)
#     # Getting iftop command output
#     cmd2 = subprocess.Popen(command.split(), stdout=subprocess.PIPE)

#     # decoding output from cmd
#     lines = cmd2.stdout.read().decode()
#     lines_lst = lines.split("\n")

#     # await asyncio.sleep(10)
#     # Parsing each line and getting the output in line protocol.
#     for i, line in enumerate(lines_lst):
#         # Getting list values of each line
#         lst = line.split()
#         try:
#             # initializing fields
#             sender, sent, receiver, received = 0, 0, 0, 0

#             # Checking for valid lines in the output
#             if(len(lst) > 1):
#                 if (lst[0].isdigit()):
#                     # print(lst[0])

#                     # Validity check with length for sent
#                     if(len(lst) == 7):
#                         # Getting sender and send rate
#                         sender, sent = (lst[1], size(val=lst[4]))
#                         # print(lst)
#                     nxt_line_lst = lines_lst[i+1].split()
#                     # Validity check with length for received
#                     if(len(nxt_line_lst) == 6):
#                         # Getting receiver and received rate
#                         receiver, received = (
#                             nxt_line_lst[0], size(val=nxt_line_lst[3]))
#                         # print(nxt_line_lst)

#                         # printing values in line protocol format
#                         # Validity check to prevent unnecessary values.
#                         if (sent == "0"):
#                             # printing values in line protocol format
#                             temp_data = f'iftop_traffic,interface={interface},sender={sender},receiver={receiver} receiveRate={float(received)}'
#                             print(temp_data)
#                             return temp_data
#                         elif(received == "0"):
#                             temp_data = f'iftop_traffic,interface={interface},sender={sender},receiver={receiver} sendRate={float(sent)}'
#                             print(temp_data)
#                             return temp_data
#                         else:
#                             temp_data = f'iftop_traffic,interface={interface},sender={sender},receiver={receiver} sendRate={float(sent)},receiveRate={float(received)}'
#                             print(temp_data)
#                             return temp_data
#                 else:
#                     # Skipping unwanted lines.
#                     pass
#                     # append_new_line("here")

#         # Handling exception and storing the output in a log file.
#         except Exception as e:
#             if debug:
#                 raise e
#             else:
#                 pass


# async def asyn():
#     try:
#         result = get_physical_interfaces(
#             r"/etc/telegraf/iftop",
#             debug
#         )
#         if(result == None):
#             raise Exception("No interfaces found.")
#         wan_interfaces, lan_interfaces, wifi_interfaces = result

#         #interfaces = set(list(wan_interface_dict) + list(lan_interface_dict))
#         interfaces = set(wan_interfaces + lan_interfaces + wifi_interfaces)
#         #interfaces = {"enp1s0","enp2s0","enp3s0","enp4s0"}
#         inactives_interfaces = set()

#         # Getting active interfaces.
#         actives_interfaces, out = get_active_interfaces(interfaces=interfaces,
#                                                         debug=debug
#                                                         )
#         # getting inactive interfaces
#         inactives_interfaces = interfaces - actives_interfaces

#         # Printing line protocol for interfaces present.
#         actives_interfaces_list = []
#         for interface in actives_interfaces:
#             # Iftop data for active interfaces.
#             # actives_interfaces_list.append(get_iftop(sudo_password=sudo_password,
#             #                                          interface=interface,
#             #                                          debug=debug
#             #                                          ))
#             await get_iftop(sudo_password=sudo_password,
#                        interface=interface,
#                        debug=debug
#                        )
#             # get_iftop(sudo_password=sudo_password,
#             #           interface=interface,
#             #           debug=debug
#             #           )
# #        await asyncio.sleep(0.2)
#         # print(actives_interfaces_list)
#         #await asyncio.gather(*actives_interfaces_list)

#     except Exception as e:
#         if debug:
#             pass
#         else:
#             pass


# # In[ ]:
# def async_thread():
#     asyncio.run(asyn())


# if __name__ == "__main__":
#  #   print(datetime.datetime.now())
#    # thread1 = threading.Thread(target=async_thread, args=())
#    # thread1.start()
#    # thread1.join()
#     async_thread()
# #    print("-------------------------------------- {}".format(datetime.datetime.now()))

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import json
import subprocess
#import datetime

# In[2]:


debug = 1
sudo_password = None


# In[3]:


def get_physical_interfaces(
    file_loc = "/home/chiefnet/ChiefNet/ConfigurationFiles",
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
                          if not (interface.startswith("tun"))
                         ]

        return wan_interfaces, lan_interfaces, wifi_interfaces
    except Exception as e:
        if debug: 
            raise e
        else:
            pass


# In[4]:


def get_active_interfaces(interfaces,debug=0):
    """
    Function to retrieve active interfaces that are currently in UP state.
    """
    str_out = ""
    out ={}
    # Variable to store active interfaces.
    actives_interfaces =set()
    # cmd to get all the interfaces.
    command = 'ip -j address'

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
#    print(actives_interfaces)
    return actives_interfaces,str(str_out)


# In[5]:


def size(val):
    """
    Parsing the value in Bytes for a given value.
    """
    val = val.lower()
    if(val[-1] == "b"):
        val = val[:-1]

        if("g" in val):
            return val.lower().replace("g","0"*9)
        elif("m" in val):
            return val.lower().replace("m","0"*6)
        elif("k" in val):
            return val.lower().replace("k","0"*3)
        else:
            return val
    else:
        return "0"
    
def get_iftop(interface,sudo_password=None,debug=0):
    
    """
    Getting the iftop values and parsing it as per line protocol.
    """

    # iftop command for each interface 
    command = 'iftop -bBP -i ' + interface + ' -s 1s -o 10s -L 100 -t'
    
    # For inserting password in cmd line
    #cmd1 = subprocess.Popen(['echo',sudo_password], stdout=subprocess.PIPE)
    # Getting iftop command output
    cmd2 = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    
    # decoding output from cmd
    lines = cmd2.stdout.read().decode()
    lines_lst = lines.split("\n")
    
    # Parsing each line and getting the output in line protocol.
    for i,line in enumerate(lines_lst):
        # Getting list values of each line
        lst = line.split()
        try :
            # initializing fields
            sender,sent,receiver,received = 0,0,0,0
            
            # Checking for valid lines in the output
            if(len(lst)>1):
                if (lst[0].isdigit()):
                    #print(lst[0])

                    # Validity check with length for sent
                    if(len(lst) == 7):
                        # Getting sender and send rate
                        sender,sent = (lst[1],size(val =lst[4]))
                        #print(lst)
                    nxt_line_lst = lines_lst[i+1].split()
                    # Validity check with length for received
                    if(len(nxt_line_lst) == 6):
                        # Getting receiver and received rate
                        receiver,received =(nxt_line_lst[0],size(val =nxt_line_lst[3]))
                        #print(nxt_line_lst)

                        # printing values in line protocol format
                        # Validity check to prevent unnecessary values.
#                        print("--------------------------------------")
                        if (sent == "0"):
                            # printing values in line protocol format
                            print('iftop_traffic,interface=' + interface + ',sender='+ sender + ',receiver=' +receiver + 'receiveRate=' + float(received))
                        elif(received == "0"):
                            print('iftop_traffic,interface='+interface + ',sender=' + sender + ',receiver=' +  receiver + ' sendRate= ' + {float(sent)})
                        else:
                            print('iftop_traffic,interface='+ interface + ',sender=' + sender + ',receiver=' + receiver +' sendRate=' + float(sent) + ' ,receiveRate=' + float(received))
                            
                else:
                    # Skipping unwanted lines.
                    pass
                    #append_new_line("here")

        # Handling exception and storing the output in a log file.
        except Exception as e:
            if debug: 
                raise e
            else:
                pass


# In[ ]:


if __name__ == "__main__":
    
    try:
       # print(datetime.datetime.now())

        result = get_physical_interfaces(
                r"/etc/telegraf/custom_scripts",
                debug
                )
        if(result == None):
            raise Exception("No interfaces found.")
        wan_interfaces, lan_interfaces, wifi_interfaces = result
        
        #interfaces = set(list(wan_interface_dict) + list(lan_interface_dict))
        interfaces = set(wan_interfaces + lan_interfaces + wifi_interfaces)
        #interfaces = {"enp1s0","enp2s0","enp3s0","enp4s0"}
        inactives_interfaces = set()
        
        # Getting active interfaces.
        actives_interfaces,out = get_active_interfaces(interfaces=interfaces,
                                                          debug=debug
                                                         )
        # getting inactive interfaces
        inactives_interfaces = interfaces - actives_interfaces
#        print(actives_interfaces)       
        # Printing line protocol for interfaces present.
        for interface in actives_interfaces:
            # Iftop data for active interfaces.
            get_iftop(sudo_password=sudo_password,
                       interface=interface,
                       debug=debug
                      )
       # print(datetime.datetime.now())

    except Exception as e:
        if debug:
            raise e
        else:
            pass
