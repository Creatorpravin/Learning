from scapy.all import srp1, Ether, IP, ICMP
import json
import time

def ping_destination(destination, source_ip, interface, packet_count=10):
    # Initialize variables to store response details
    total_receive = 0
    total_rtt = 0
    min_rtt = float('inf')
    max_rtt = 0

    for _ in range(packet_count):
        # Craft Ethernet, IP, and ICMP packets
        packet = Ether() / IP(src=source_ip, dst=destination) / ICMP()

        # Send and receive packets
        response = srp1(packet, iface=interface, timeout=2, verbose=False)
        if response:
            # Update variables with response information
            total_receive += 1
            sent_time = packet.time  # Extract the sent time from the packet
            received_time = response.time  # Extract the received time from the response
            rtt = (received_time - sent_time) * 1000
            total_rtt += rtt
            min_rtt = min(min_rtt, rtt)  # Keep track of the minimum value in a sequence
            max_rtt = max(max_rtt, rtt)  # Keep track of the maximum value in a sequence
            time.sleep(0.1)

    # Calculate average RTT only if there were responses
    avg_rtt = total_rtt / total_receive if total_receive > 0 else 0.0
    packet_loss = (packet_count - total_receive) / packet_count * 100
    # Create a dictionary with the final results
    result = {
        "destination": destination,
        "packet_transmit": packet_count,
        "packet_receive": total_receive,
        "packet_loss_count": packet_count - total_receive,
        "packet_loss_rate": packet_loss,
        "rtt_min": float("{:.3f}".format(min_rtt if total_receive > 0 else 0.0)),
        "rtt_avg": float("{:.3f}".format(avg_rtt)),
        "rtt_max": float("{:.3f}".format(max_rtt if total_receive > 0 else 0.0)),
        "rtt_mdev": float("{:.3f}".format((max_rtt - min_rtt) / 2 if total_receive > 0 else 0.0)),
        "packet_duplicate_count": 0,
        "packet_duplicate_rate": 0.0,
        "interface": interface,
        "interface_state": "DOWN" if packet_loss == 100 else "UP",  # You may need to check the interface state
    }

    return result

def main():
    destinations = ["1.1.1.1"]  # Add more destinations if needed
    interfaces = {
        "enp0s3": "10.0.2.15",  # Replace with the actual IP of interface1
        "enp0s8": "10.0.3.15",  # Replace with the actual IP of interface2
    }

    results = []

    for interface, source_ip in interfaces.items():
        for destination in destinations:
            result = ping_destination(destination, source_ip, interface, packet_count=10)
            results.append(result)

    # Print the results in JSON format
    json_output = json.dumps(results, indent=2)
    print(json_output)

if __name__ == "__main__":
    main()
