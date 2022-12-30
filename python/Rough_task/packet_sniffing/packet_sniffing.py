import socket 
import struct
import binascii

#s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.htons(0x0800))
interface = socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.IPPROTO_IP)
interface.bind(("enp4s0",0x0800))
print(interface)
#s.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
#interface.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)
#print(interface.recvfrom)


while True:

    packet=interface.recvfrom(65565)
#    print(binascii.hexlify)    
    print("|----- Ethernet Header -----|")
    eth_header = struct.unpack("!6s6s2s", (packet[0][0:14]))
    print ("Destination mac-address ", binascii.hexlify(eth_header[0]))
    print ("Source mac-address ", binascii.hexlify(eth_header[1]))
    print ("Type ", binascii.hexlify(eth_header[2]))
#    print(socket.inet_ntoa)

    print("|----- IP Header -----|")
    ip_header = struct.unpack("!12s4s4s", (packet[0][14:34]))
    print ("Source IP ", socket.inet_ntoa(ip_header[1]))
    print ("Destination IP ", socket.inet_ntoa(ip_header[2]))
