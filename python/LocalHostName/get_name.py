file = open("dnsmasq.leases","r")
content = []
file_content = file.readlines()


for lines in file_content[0: ]:
     content.append(lines.split())

#print(content[12][3])
for data in content:
    if data[2] == "192.168.10.162": 
      print(data[3])