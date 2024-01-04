import subprocess
import json
# WAN_INTERFACE_PACKET_LOSS_PERCENTAGE_THRESHOLD = 100

# def __ping_destination_via_wan_interface():
#     ping_command = "ping 8.8.8.8 -c 3 -w 3"

#     packet_loss_list = []

#     for i in range(2):
#         ping_process = subprocess.run(ping_command, shell=True, capture_output=True, text=True)

#         stdout = ping_process.stdout

#         if ping_process.returncode != 0:
#             packet_loss_percentage = 100
#         else:
#             packet_loss_percentage = str(stdout).split(',')[
#                 2].split('%')[0].strip()
            
#         packet_loss_list.append(float(packet_loss_percentage))
#     print(packet_loss_list)
#     average_packet_loss_percentage = sum(
#         packet_loss_list) / len(packet_loss_list)
#     calculated_packet_loss_percentage = round(average_packet_loss_percentage)

#     wan_interface_state = True
    
#     if calculated_packet_loss_percentage == WAN_INTERFACE_PACKET_LOSS_PERCENTAGE_THRESHOLD:
#         wan_interface_state = False

#     return  wan_interface_state


# print(__ping_destination_via_wan_interface())

with open("wan-failover-threshold.json", 'r') as threshold_value:
    data = json.load(threshold_value)

print(type(data[0]))
print(data[0]["latency"])