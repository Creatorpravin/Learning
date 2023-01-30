import socket

def find_service_name():
    protocolName = "tcp"
    for port in [80, 25, 22]:
        print ("Port: %s => service name: %s" %(port, socket.getservbyport(port, protocolName)))
    print ("Port: %s => service name: %s" %(53, socket.getservbyport(53, 'udp')))

find_service_name()