# Linux Networking commands

* pwd - File path
* touch filename - create file
* nano filename - edit the file
* cat filename - view the file
* sudo mv 01.ethernet-configuration.yaml 01-ethernet-configuration.yaml - change the filename
* sudo ip link set up dev eno1 - Set the link up on that interface
* sudo ip link set down dev eno1 - Set the link down on that link
* ip a - get the ip of interfaces
* ip r - get the server gateway or ip 
* sudo traceroute 8.8.8.8 - Trace the route of packets 
* ping 192.128.10.1 - Check the pinging 
* sudo apt-get install netplan.io - install netplan 
* sudo netplan generate - Generte the netplan 
* sudo netplan apply - Apply netplan 
* sudo iptables -t nat -A POSTROUTING -j MASQUERADE - enable routing 
* ssh hostname@domain(or)ip - Make SSH connection
* scp origin_file_path hostname@ip:remote_filepath - Trafer file in secure copy 
* scp hostname@ip:remote_filePath origin_filePath - download the file through secure copy
* sudo tcpdump -i eno1 - Check the data packets flow
* ls -lh - Check the file permission
* chmod +x script-name-here.sh - Give execution permission to the files
* nmcli connection - Check the interface connection
* nmcli device status - Check all interface status
* ip a s eno1 - Status of particular link
* sudo ethtool wlp2s0 | grep -i 'Link det' - Link detected status
* ip -json route show - view command output in JSON format
* sudo su - change to root user
* hostnamectl - get os and version details
