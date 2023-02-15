#!/bin/bash

# Restarting dnsmasq.service to make sure the DHCP server
systemctl restart dnsmasq.service

# Make sure the service stopped before tun and tap configuration
systemctl stop openvpn.service

# Configuring black hole rule
ip rule add fwmark 0x00010000/0x000F0000 blackhole priority 256

# Make tunnel interface as persistent
openvpn --mktun --dev tun0
openvpn --mktun --dev tun1
openvpn --mktun --dev tun2
openvpn --mktun --dev tun3
openvpn --mktun --dev tun4

openvpn --mktun --dev tap0
openvpn --mktun --dev tap1
openvpn --mktun --dev tap2
openvpn --mktun --dev tap3
openvpn --mktun --dev tap4

openvpn --mktun --dev taps0
openvpn --mktun --dev taps1
openvpn --mktun --dev taps2
openvpn --mktun --dev taps3
openvpn --mktun --dev taps4

# Start OpenVPN service
systemctl start openvpn.service

# Deactivate the virtual environment
deactivate

# Set root directory to the CPE application
cd /home/chiefnet/ChiefNet/CPE

# Kill the current instance of CPE application
kill $(cat CPE-application.pid)

# Activate the virtual environment
activate()
{ source ../VirtualEnvironment/bin/activate; }
activate

# Run CPE application
python main.py

# Set to default directory
cd /home/chiefnet/ChiefNet
