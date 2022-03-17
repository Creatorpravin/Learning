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
* ping 192.128.10.1 - Check the pinging
* sudo watch -n 1 ("commends") - continuesoly run the command 
* sudo vtysh - to check the version  

# **Netplan**
* sudo apt-get install netplan.io - install netplan 
* sudo netplan generate - Generte the netplan 
* sudo netplan apply - Apply netplan 

# **SSH**
* ssh hostname@domain(or)ip - Make SSH connection
* scp origin_file_path hostname@ip:remote_filepath - Trafer file in secure copy 
* scp hostname@ip:remote_filePath origin_filePath - download the file through secure copy
* sudo traceroute 8.8.8.8 - Trace the route of packets 
* sudo tcpdump -i eno1 - Check the data packets flow

# **File permission**
* ls -lh - Check the file permission
* chmod +x script-name-here.sh - Give execution permission to the files
* nmcli connection - Check the interface connection
* nmcli device status - Check all interface status
* ip a s eno1 - Status of particular link
* sudo ethtool wlp2s0 | grep -i 'Link det' - Link detected status
* ip -json route show - view command output in JSON format
* sudo su - change to root user
* hostnamectl - get os and version details
* journalctl -u chiefnet-sdwan -f - monitering the chiefne t running 

# **IP Table**
* ip rule - to check the iptable rule
* sudo iptables -t nat -A POSTROUTING -j MASQUERADE - enable routing
* sudo iptables -F - Delete all table (flush)
* sudo iptables-save>test.txt - get the current iptable
* sudo iptables-restore<test.txt - set and run the iptable
* sudo iptables -A INPUT -s 192.168.1.198 -j DROP - to block particular ip
* iptables -A OUTPUT -p tcp -m string --string "amazon.com" --algo kmp -j REJECT - To block a site
* sudo iptables -F - to delete all iptables (flush)
* sudo iptables -t "table_name" -L -n -v - view particular table by table name.
* sudo iptables -L -n -v - check the iptables packs hits
* host -t a main.com - get the ip of domain
* sudo ip route add 157.240.23.35 via 192.168.10.10 dev enp0s8 - (Traffic steering) add route to particular ip 