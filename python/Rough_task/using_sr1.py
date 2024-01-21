from scapy.all import srp1, Ether, IP, ICMP
import json
import time
#import psutil
import netifaces

def get_ip_address(interface):
    try:
        addresses = netifaces.ifaddresses(interface)
        ipv4_address = addresses[netifaces.AF_INET][0]['addr']
        return ipv4_address
    except (KeyError, IndexError):
        return None

def ping_destination(destination, interface, packet_count=10):
    # Get the IP address of the specified interface
    source_ip = get_ip_address(interface)
    if source_ip is None:
        result = {
        "destination": "null",
        "packet_transmit": "null",
        "packet_receive": "null",
        "packet_loss_count": "null",
        "packet_loss_rate": "null",
        "rtt_min": "null",
        "rtt_avg": "null",
        "rtt_max": "null",
        "rtt_mdev": "null",
        "packet_duplicate_count": "null",
        "packet_duplicate_rate": "null",
        "interface": interface,
        "interface_state": "DOWN",
         }

        return result

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
            time.sleep(0.5)

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
    destinations = ["8.8.8.8"]  # Add more destinations if needed
#    interfaces = [iface.name for iface in psutil.net_if_stats().values() if iface.isup]
    interfaces = ["enp0s3", "enp0s8"]
    results = []

    for interface in interfaces:
        for destination in destinations:
            result = ping_destination(destination, interface, packet_count=5)
            if result is not None:
                results.append(result)

    # Print the results in JSON format
    json_output = json.dumps(results, indent=2)
    print(json_output)

if __name__ == "__main__":
    main()
