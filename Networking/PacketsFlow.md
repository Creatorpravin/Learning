# Packet flow in different Network

* To deliver the packet to the destination host, the source IP, destination IP, source MAC address and destination MAC address should be known. Some basic rules for the packet flow: 

1. If the destination host is present in the same network, then the packet is delivered directly to the destination host.
2. If the destination host is present in a different network then the packet is delivered to the default gateway first which in turn delivers the packet to the destination host.
3. If ARP is not resolved then ARP will be resolved first.
4. MAC address never crosses its broadcast domain.