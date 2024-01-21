import subprocess
def __ping_destination_via_wan_interface():
        
        wan_interface_state_dict = dict()
        
        packet_loss_list = []
        latency_list = []
        jitter_list = []
        
        for i in range(3):
            ping_process = subprocess.run(["ping", "-c", "4", "8.8.8.8"], stdout=subprocess.PIPE, text=True)
                                        
            stdout = ping_process.stdout

            if ping_process.returncode != 0:
                packet_loss_percentage = 100
                rtt_avg = 100
                jitter = 100

            else:
                packet_loss_percentage = str(stdout).split(',')[2].split('%')[0].strip()
                if "duplicates" in packet_loss_percentage:
                    packet_loss_percentage = str(stdout).split(',')[3].split('%')[0].strip() 
                rtt_min = str(stdout).split("mdev =")[1].split("/")[0]
                rtt_avg = str(stdout).split("mdev =")[1].split("/")[1]
                rtt_max = str(stdout).split("mdev =")[1].split("/")[2]
                jitter = float(rtt_max) - float(rtt_min)
            packet_loss_list.append(float(packet_loss_percentage))
            latency_list.append(float(rtt_avg))
            jitter_list.append(float(jitter))


        average_packet_loss_percentage = sum(packet_loss_list) / len(packet_loss_list)
        calculated_packet_loss_percentage = round(average_packet_loss_percentage)
    
        average_latency_ms = sum(latency_list) / len(latency_list)
        calculated_packet_latency = round(average_latency_ms)

        average_jitter_ms = sum(jitter_list) / len(jitter_list)
        calculated_packet_jitter = round(average_jitter_ms)

        print(average_jitter_ms)
        print(average_latency_ms)
        print(average_packet_loss_percentage)         

        
        return wan_interface_state_dict

__ping_destination_via_wan_interface()