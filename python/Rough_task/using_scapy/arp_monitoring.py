from scapy.all import *

def arp_display(pkt):
    if pkt[ARP].op == 1: #who-has (request)
        return "Request: " + pkt[ARP].psrc + " is asking about " + pkt[ARP].pdst
    if pkt[ARP].op == 2: #is-at   (response)
        return "*Response: " + pkt[ARP].hwsrc + " has address " + pkt[ARP].psrc

print sniff(prn=arp_display, filter="arp", store=0, count=10)