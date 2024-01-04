import time
import os
from scapy.all import *

# Define the target IP address to ping (e.g., a public DNS server)
target_ip = "8.8.8.8"

# Define the network interface to capture packets from
interface_to_capture = "wlp0s20f3"  # Change this to your specific interface name

# Define the maximum consecutive failures before considering it a failure
max_consecutive_failures = 3

# Initialize failure counter
consecutive_failures = 0

# Initialize latency and jitter variables
latency = None
jitter = None

# Define the number of packets in each burst
burst_size = 5  # Adjust the burst size as needed

# Initialize a list to store latency measurements within the burst
latency_measurements = []

# Define the function to send a burst of ICMP echo requests and check for replies
def send_icmp_burst(target_ip, burst_size):
    global latency, jitter, latency_measurements, consecutive_failures
    try:
        for _ in range(burst_size):
            # Construct an ICMP packet
            icmp = IP(dst=target_ip) / ICMP()
            sent_time = time.time()  # Record the time when the request was sent

            # Send the ICMP packet using the specified network interface
            response = sr1(icmp, iface=interface_to_capture, timeout=5)

            if response and response.haslayer(ICMP) and response[ICMP].type == 0:
                # Ping was successful, reset the failure counter
                consecutive_failures = 0
                received_time = time.time()  # Record the time when the response was received
                latency = (received_time - sent_time) * 1000  # Calculate latency in milliseconds
                latency_measurements.append(latency)
            else:
                # Ping failed, increment the failure counter
                consecutive_failures += 1
                print(f"Ping to {target_ip} failed (Consecutive Failures: {consecutive_failures}).")

                if consecutive_failures >= max_consecutive_failures:
                    print("WAN link failure detected. Taking action...")
                    # Add your code to handle the link failure here

    except KeyboardInterrupt:
        print("Monitoring script terminated.")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

while True:
    send_icmp_burst(target_ip, burst_size)

    if latency_measurements:
        avg_latency = sum(latency_measurements) / len(latency_measurements)
        jitter = sum(abs(latency - avg_latency) for latency in latency_measurements) / len(latency_measurements)
        print(f"Average Latency: {avg_latency:.2f} ms")
        print(f"Average Jitter: {jitter:.2f} ms")

    time.sleep(5)  # Adjust the interval as needed