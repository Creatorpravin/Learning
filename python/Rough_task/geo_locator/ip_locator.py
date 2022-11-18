# import geocoder as geo

# ip_addr = "1.1.1.1"

# ip = geo.ip(ip_addr)

# print(type(ip.city))
# if ip.city == None:
#     print("None")
# else:
#     print(ip.city)
import subprocess
import re

cmd = "geoiplookup 15.207.189.46"

ip_add_location = subprocess.Popen(
    cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

location, location_err = ip_add_location.communicate()
if ip_add_location.returncode == 0:
    if "IP Address not found" in location:
        print("IP Address not found")
    else:
        location_li = re.sub(r'[^\w]', ' ', location).split(" ")
        print("country = ", location_li[4])
