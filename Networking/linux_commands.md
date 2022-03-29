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

# Traffic steering
* sudo iptables -t mangle -A PREROUTING -i enp0s10 -d 8.8.8.8 -j MARK –set-mark 0x00010001 => Set fwmark value for incoming packets from LAN interface in Mangle table.
* ip rule add fwmark 0x00000001/0x000000ff tables wan_table_5 => Create and add fwmark in ip rule  table
* ip route add default via 10.0.2.2 dev enp0s3 table wable_5 => Add route to respective WAN interface by ip rule table
* ip route show table wan_table_5 => To view the table 
* ip route add 102.102.166.224 via 192.168.10.10 dev enps03 => send particular ip to one interface

# ipset 
 
* ipset -N myset-ip iphash => create a myset-ip hash table
* ipset add myset-ip 1.1.1.1 => add ip to hash table
* ipset add myset-ip 2.2.2.2=> add ip to hash table
* iptables -I INPUT -m set --match-set myset-ip src -j DROP=> Finally, configure iptables to block any address in that set.
* ipset -L => to view hash table of ipset
* ipset -N myset nethash =>  create a myset hash table block a network
* ipset add myset 14.144.0.0/12 => add network to hash table
* ipset add myset 27.8.0.0/13 => add network to hash table
* iptables -I INPUT -m set --match-set myset src -j DROP => drop the network
* ipset destroy myset => delete particular table
* ipset -F => delete all hash tables
