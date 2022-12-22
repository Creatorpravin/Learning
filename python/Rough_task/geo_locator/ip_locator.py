import geocoder as geo

ip_addr = "164.92.143.142"

ip = geo.ip(ip_addr)

print(type(ip.city))
print(ip.country)
if ip.city == None:
    print("None")
else:
    print(ip.city)
    
# import subprocess
# import re
# import json 

# cmd = "geoiplookup 15.207.189.46"

# ip_add_location = subprocess.Popen(
#     cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

# location, location_err = ip_add_location.communicate()

# if ip_add_location.returncode == 0:
#     if "IP Address not found" in location:
#         print("IP Address not found")
#     else:
#         location_li = re.sub(r'[^\w]', ' ', location).split(" ")
#         print("country = ", location_li[4])
#         with open(file="country_code.json", mode="r") as  country_code:
#             country_json = json.load(country_code)
#             for country in country_json:
#                 if country['code'] == location_li[4]:
#                     print(country['flag'])
            