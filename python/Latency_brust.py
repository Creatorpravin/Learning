#!/usr/bin/env python3
 
from scapy.all import *
import time
 
# Define the target IP address to ping (e.g., a public DNS server)
target_ip = "8.8.8.8"
 
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
    global latency, jitter, latency_measurements
    try:
        for _ in range(burst_size):
            icmp = IP(dst=target_ip)/ICMP()
            sent_time = time.time()  # Record the time when the request was sent
            response = sr1(icmp, timeout=5)  # Send ICMP echo request and wait for a response
            received_time = time.time()  # Record the time when the response was received
 
            if response and response.haslayer(ICMP) and response[ICMP].type == 0:
                # Ping was successful, reset the failure counter
                consecutive_failures = 0
                latency = (received_time - sent_time) * 1000  # Calculate latency in milliseconds
                latency_measurements.append(latency)
 
            else:
                # Ping failed, increment the failure counter
                consecutive_failures += 1
                print(f"Ping to {target_ip} failed (Consecutive Failures: {consecutive_failures}).")
 
                # If consecutive failures exceed the threshold, consider it a link failure
                if consecutive_failures >= max_consecutive_failures:
                    print("WAN link failure detected. Taking action...")
                    # Add your code to handle the link failure here, e.g., send alerts or switch to a backup link
 
    except KeyboardInterrupt:
        print("Monitoring script terminated.")
        sys.exit(0)
    except Exception as e:
        # Handle any other exceptions (e.g., network issues)
        print(f"An error occurred: {str(e)}")
 
while True:
    send_icmp_burst(target_ip, burst_size)
    
    if latency_measurements:
        avg_latency = sum(latency_measurements) / len(latency_measurements)
        a=((latency - avg_latency) for latency in latency_measurements)
        print("---------------",sum(abs(a)))
        jitter = sum(abs(latency - avg_latency) for latency in latency_measurements) / len(latency_measurements)
        print(f"Average Latency: {avg_latency:.2f} ms")
        print(f"Average Jitter: {jitter:.2f} ms")
    
    time.sleep(3)  # Adjust the interval as needed