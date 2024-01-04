#!/usr/bin/env python3
import subprocess
import json

ping_destination = "8.8.8.8"

tun_interfaces = ["tun0", "tun1", "tun2", "tun3", "tun4", "tap0", "tap1", "tap2", "tap3", "tap4"]
systemconfiguration_json = {}
output_list = []

with open("/etc/telegraf/custom_scripts/SystemConfiguration.json", "r") as conf_file:
    data = conf_file.read()
    systemconfiguration_json = json.loads(data)    

try:
    for interface in systemconfiguration_json["system_information"]["wan_interfaces"]:
        if interface not in tun_interfaces:
            latency_measurements = []
            packet_transmit = 10
            packet_receive = 0
            packet_loss_count = 0
            packet_duplicate_count = 0

            for _ in range(packet_transmit):
                ping_command = f"ping {ping_destination} -c 1 -i .290 -w 3 -I {interface} | pingparsing"
        
                ping_result = subprocess.run(ping_command, shell=True, capture_output=True)

                if ping_result.returncode != 0:
                    raise Exception("Failed to run ping command")

                ping_output = json.loads(ping_result.stdout.decode("utf-8"))
                latency_measurements.append(ping_output["rtt_avg"])

                if "packet_receive" in ping_output and ping_output["packet_receive"] == 1:
                    packet_receive += 1
                else:
                    packet_loss_count += 1

                if "packet_duplicate_count" in ping_output:
                    packet_duplicate_count += ping_output["packet_duplicate_count"]

            avg_latency = sum(latency_measurements) / len(latency_measurements)
            rtt_mdev = max(latency_measurements) - min(latency_measurements)

            packet_loss_rate = (packet_loss_count / packet_transmit) * 100 if packet_transmit > 0 else 0
            packet_duplicate_rate = (packet_duplicate_count / packet_transmit) * 100 if packet_transmit > 0 else 0

            output_dict = {
                "destination": ping_destination,
                "packet_transmit": packet_transmit,
                "packet_receive": packet_receive,
                "packet_loss_count": packet_loss_count,
                "packet_loss_rate": packet_loss_rate,
                "packet_duplicate_count": packet_duplicate_count,
                "packet_duplicate_rate": packet_duplicate_rate,
                "rtt_min": min(latency_measurements),
                "rtt_avg": avg_latency,
                "rtt_max": max(latency_measurements),
                "rtt_mdev": rtt_mdev,
                "interface": interface,
                "interface_state": "UP",  # Placeholder, replace with actual interface state
            }

            output_list.append(output_dict)
except Exception as exceptions:
    raise exceptions

print(json.dumps(output_list))