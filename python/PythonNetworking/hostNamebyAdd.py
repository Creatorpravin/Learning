
import socket

 

ipAddress = "3.96.23.237"

hostName = socket.gethostbyaddr(ipAddress)

print("Host Name for the IP address {} is {}".format(ipAddress, hostName))