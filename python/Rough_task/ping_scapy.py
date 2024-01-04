from scapy.all import sr1, IP, ICMP, conf
from datetime import datetime
import json
import time

def ping_destination(destination, interface, packet_count=10):
    # Set the sending interface
    conf.iface = interface

    # Initialize variables to store response details
    total_receive = 0
    total_rtt = 0
    min_rtt = float('inf')
    max_rtt = 0

    for _ in range(packet_count):
        # Craft ICMP Echo Request packet
        packet = IP(dst=destination) / ICMP()

        # Send and receive packets
        response = sr1(packet, timeout=2, verbose=False, iface=interface)

        if response:
            # Update variables with response information
            total_receive += 1
            sent_time = packet.sent_time  # Extract the sent time from the packet
            received_time = response.time  # Extract the received time from the response
            rtt = (received_time - sent_time) * 1000
            total_rtt += rtt
            min_rtt = min(min_rtt, rtt) # Keep track of the minimum value in a sequence
            max_rtt = max(max_rtt, rtt) # Keep track of the maximum value in a sequence
            time.sleep(0.1)
    # Calculate average RTT only if there were responses
    avg_rtt = total_rtt / total_receive if total_receive > 0 else 0.0

    # Create a dictionary with the final results
    result = {
        "destination": destination,
        "packet_transmit": packet_count,
        "packet_receive": total_receive,
        "packet_loss_count": packet_count - total_receive,
        "packet_loss_rate": (packet_count - total_receive) / packet_count * 100,
        "rtt_min": float("{:.3f}".format(min_rtt if total_receive > 0 else 0.0)),
        "rtt_avg": float("{:.3f}".format(avg_rtt)),
        "rtt_max": float("{:.3f}".format(max_rtt if total_receive > 0 else 0.0)),
        "rtt_mdev": float("{:.3f}".format((max_rtt - min_rtt) / 2 if total_receive > 0 else 0.0)),
        "packet_duplicate_count": 0,
        "packet_duplicate_rate": 0.0,
        "interface": interface,
        "interface_state": "UP",  # You may need to check the interface state
    }

    return result

def main():
    destinations = ["8.8.8.8"]  # Add more destinations if needed
    # interfaces = ["enp1s0", "enp2s0"]  # Specify the interfaces to use
    ping_destination = "8.8.8.8"
    results = []
    tun_interfaces = ["tun0", "tun1", "tun2", "tun3", "tun4", "tap0", "tap1", "tap2", "tap3", "tap4"]
    systemconfiguration_json = {}
    
    with open("/etc/telegraf/custom_scripts/SystemConfiguration.json", "r") as conf_file:
        data = conf_file.read()
        systemconfiguration_json = json.loads(data)  
    
    for interface in systemconfiguration_json["system_information"]["wan_interfaces"]:
        if interface not in tun_interfaces:
                for destination in destinations:
                  result = ping_destination(destination, interface, packet_count=10)
                  results.append(result)
   
    # for interface in interfaces:
    #     for destination in destinations:
    #         result = ping_destination(destination, interface, packet_count=10)
    #         results.append(result)

    # Print the results in JSON format
    json_output = json.dumps(results, indent=2)
    print(json_output)

if __name__ == "__main__":
    main()
