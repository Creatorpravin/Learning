import subprocess
import json

# Run the ping command and capture the output
ping_output = subprocess.Popen(["ping", "-c", "3", "8.8.8.8"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, std_err = ping_output.communicate()

# Convert the output to a string
ping_output_str = stdout.decode("utf-8")
print(ping_output_str)

# Split the output into lines
# lines = ping_output_str.split('\n')
# rtt_lines = str(lines[7]).split('=')
# rtt_values = str(rtt_lines[1]).split('/')
# print(float(rtt_values[0]))
# print(float(rtt_values[1]))
# print(float(rtt_values[2]))

# print(float(rtt_values[2])-float(rtt_values[0]))

rtt_min = str(ping_output_str).split("mdev =")[1].split("/")[0]
rtt_avg = str(ping_output_str).split("mdev =")[1].split("/")[1]
rtt_max = str(ping_output_str).split("mdev =")[1].split("/")[2]
jitter = float(rtt_max) - float(rtt_min)

print("Average latency is :",rtt_avg)
print("Jitter value is : ", jitter)


# with open("wan-failover-threshold.json", 'r') as threshold_value:
#     data = json.load(threshold_value)

# print(data)
  