#!/bin/bash

# Stop the script if any error occurs
set -e

# Check for root privileges
if [ $(id -u) -ne 0 ]; then
    echo "This script must be run as root or with sudo."
    exit 1
fi

# Check if the file "chiefnetimg_latest.tar" exists
if [ -e "chiefnetaug.tar" ]; then
    echo "The file chiefnetaug.tar already exists in the current directory. Proceeding with 20 GB disk space requirement."
    threshold_gb=5
else
    echo "The file chiefnetaug.tar does not exist in the current directory. Proceeding with 30 GB disk space requirement."
    threshold_gb=30
fi

# Get available disk space in GB
available_gb=$(df -BG / | awk 'NR==2 {print $4}' | sed 's/G//')

# Check if available space is less than the threshold
if [ "$available_gb" -lt "$threshold_gb" ]; then
  echo "Error: Available disk space is less than $threshold_gb GB."
  exit 1
else
  echo "Disk space is sufficient ($available_gb GB available). Proceeding with the script."
fi

# Prompt for machine count
echo "Enter the machine count"
read input_count

if [ $input_count -eq 0 ]; then
  echo "Usage: $0 <count>"
  exit 1
fi

# Check if Podman is installed
if ! command -v podman
then
    echo "Podman is not installed. Installing Podman..."

    # Update package repositories
    sudo apt update -y || exit 1

    # Install curl
    sudo apt install curl -y || exit 1

    # Add Podman repository
    echo "deb https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/xUbuntu_20.04/ /" | sudo tee /etc/apt/sources.list.d/podman.list
    curl -L "https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/xUbuntu_20.04/Release.key" | sudo apt-key add -

    # Install Podman
    sudo apt update -y || exit 1
    sudo apt install podman -y || exit 1

    echo "Podman has been installed."
else
    echo "Podman is already installed."
fi

# Download chiefNET image from s3
if [ -e "chiefnetaug.tar" ]; then
    echo "The file chiefnetaug.tar already exists in the current directory. Skipping download."
else
    # Download the file if it doesn't exist
    curl -O "https://chiefnet-custom-os.s3.ap-south-1.amazonaws.com/chiefnet_docker/chiefnetimg_latest.tar"
fi

# Load chiefNET image
if podman images --format "{{.Repository}}" | grep -q "chiefnetaug"; then
    echo "The chiefnetaug image already exists. Skipping image loading."
else
    # Load the image if it doesn't exist
    sudo podman load -i chiefnetaug.tar
fi

# Run the chiefnetaug image
# Check if the chiefnet_main container is already running
if ! sudo podman ps | grep -q chiefnet_main; then
  # Start the container only if it's not already running
  sudo podman run -dit --network=podman --name=chiefnet_main chiefnetaug bash
else
  echo "chiefnet_main container is already running."
fi

# Build the ubuntu slave Podman image
if podman images --format "{{.Repository}}" | grep -q "ubuntu-slave"; then
    echo "The ubuntu-slave image already exists. Skipping image build."
else
     # Create Dockerfile content for ubuntu slave image
    DOCKERFILE_CONTENT=$(cat <<EOL
    FROM docker.io/library/ubuntu:20.04

    RUN apt update && apt install -y iproute2 iputils-ping

    CMD sleep infinity
EOL
)
    echo "$DOCKERFILE_CONTENT" > Dockerfile

    # Build the ubuntu-slave image if it doesn't exist
    sudo podman build -t ubuntu-slave .
fi


# Find the file path for container root directory
chiefnet_container=$(sudo podman ps -a --format "{{.ID}} {{.CreatedAt}}" | sort -k 2 | head -n 1 | awk '{print $1}')
MergedDir=$(sudo podman inspect -f "{{.GraphDriver.Data.MergedDir}}" $chiefnet_container)

# host_nic_name
host_nic_name=$(ip -o link show | awk -F': ' 'NR==2{print $2}')
echo "___________________"
sudo podman network create wan_network
echo "___________________2"
create_chiefnet_container() {

    sudo podman run --network=wan_network,lan_network$1 --name=chiefnet_container$1 --device=/dev/net --dns=8.8.8.8 \
    --systemd=true -v /sys/fs/cgroup:/sys/fs/cgroup:rw \
    -v $MergedDir:/srv/container_root --tmpfs /tmp --tmpfs /run -itd chiefnetaug /usr/lib/systemd/systemd --system-unit=basic.target
    # Return the sum
    echo sudo podman ps -a | grep $2 | awk '{print $7}'
}



machine_exit_status="Exited"

for i in $(seq 1 $input_count); do
        lan_network_name="lan_network${i}"
#        wan_network_name="wan_network"

        # Create WAN network
#        sudo podman network create $wan_network_name
        echo "inside for"
        # Create LAN network
        sudo podman network create --driver=macvlan --subnet=172.16.$((20 + i)).0/24 --gateway=172.16.$((20 + i)).2 \
        -o parent=$host_nic_name $lan_network_name

        echo "LAN network created"

        # chiefNET container

        # sudo podman run --rm --network=$wan_network_name,$lan_network_name --name=chiefnet_container${i} --device=/dev/net --dns=8.8.8.8 \
        # --systemd=true -v /sys/fs/cgroup:/sys/fs/cgroup:rw \
        # -v $MergedDir:/srv/container_root --tmpfs /tmp --tmpfs /run -itd chiefnetaug /usr/lib/systemd/systemd --system-unit=basic.target
        
        result="Exited"
        count=1

        while [ $count -le 5 ]
        do
            echo "inside while loop"
            if [ "$result" == "Exited" ]; then
                echo "inside if"
                result=$(create_chiefnet_container ${i})       
                echo $result 

            else
                echo "$i machine created"
                break
            fi

            count=$((count + 1))
            
        done
        
	# Add SystemConfiguration.json file
	num_addresses=$i
        echo sudo podman ps -a | grep chiefnet_container${i} | awk '{print $7}'
	for ((mac_id = 0; mac_id < num_addresses; mac_id++)); do
	    if [ "$mac_id" -eq $((num_addresses - 1)) ]; then
	        new_uuid=$(printf "1E:FE:67:AF:%02X:%02X\n" $((mac_id / 256)) $((mac_id % 256)))
	    else
	        # Generate the MAC addresses but don't print them
	        new_uuid=$(printf "1E:FE:67:AF:%02X:%02X\n" $((mac_id / 256)) $((mac_id % 256))) > /dev/null
	    fi
	done

	#printf "%02X\n" $i
	#hexa=$(printf "%02X" $i)
	#new_uuid="1E:FE:67:AF:50:$hexa"
	echo $new_uuid
	json_data='{"system_information": {"uuid": "1E:FE:67:AF:50:BA", "os_version": "20.04", "mac_address": "1e:fe:67:af:50:ba", "model": "Virtual CPE", "lan_interfaces": ["eth0"], "wan_interfaces": ["eth1", "tun0", "tun1", "tun2", "tun3", "tun4", "tap0", "tap1", "tap2", "tap3", "tap4", "taps0", "taps1", "taps2", "taps3", "taps4", "prisma1", "prisma2", "prisma3", "prisma4", "prisma5", "prisma6", "prisma7", "prisma8", "prisma9", "prisma10", "ipsec1", "ipsec2", "ipsec3", "ipsec4", "ipsec5", "ipsec6", "ipsec7", "ipsec8", "ipsec9", "ipsec10", "ipsec11", "ipsec12", "ipsec13", "ipsec14", "ipsec15", "ipsec16", "ipsec17", "ipsec18", "ipsec19", "ipsec20", "ipsec21", "ipsec22", "ipsec23", "ipsec24", "ipsec25", "ipsec26", "ipsec27", "ipsec28", "ipsec29", "ipsec30", "ipsec31", "ipsec32", "ipsec33", "ipsec34", "ipsec35", "ipsec36", "ipsec37", "ipsec38", "ipsec39", "ipsec40"], "cpu_info": [{"id": "cpu:0", "class": "processor", "claimed": true, "product": "Intel(R) Xeon(R) CPU E5-2670 v2 @ 2.50GHz", "vendor": "Intel Corp.", "physid": "1", "businfo": "cpu@0", "width": 64, "capabilities": {"fpu": "mathematical co-processor", "fpu_exception": "FPU exceptions reporting", "wp": true, "vme": "virtual mode extensions", "de": "debugging extensions", "pse": "page size extensions", "tsc": "time stamp counter", "msr": "model-specific registers", "pae": "4GB+ memory addressing (Physical Address Extension)", "mce": "machine check exceptions", "cx8": "compare and exchange 8-byte", "apic": "on-chip advanced programmable interrupt controller (APIC)", "sep": "fast system calls", "mtrr": "memory type range registers", "pge": "page global enable", "mca": "machine check architecture", "cmov": "conditional move instruction", "pat": "page attribute table", "pse36": "36-bit page size extensions", "clflush": true, "dts": "debug trace and EMON store MSRs", "mmx": "multimedia extensions (MMX)", "fxsr": "fast floating point save/restore", "sse": "streaming SIMD extensions (SSE)", "sse2": "streaming SIMD extensions (SSE2)", "ss": "self-snoop", "syscall": "fast system calls", "nx": "no-execute bit (NX)", "rdtscp": true, "x86-64": "64bits extensions (x86-64)", "constant_tsc": true, "arch_perfmon": true, "pebs": true, "bts": true, "nopl": true, "xtopology": true, "tsc_reliable": true, "nonstop_tsc": true, "cpuid": true, "aperfmperf": true, "pni": true, "pclmulqdq": true, "ssse3": true, "cx16": true, "pcid": true, "sse4_1": true, "sse4_2": true, "x2apic": true, "popcnt": true, "tsc_deadline_timer": true, "aes": true, "xsave": true, "avx": true, "f16c": true, "rdrand": true, "hypervisor": true, "lahf_lm": true, "cpuid_fault": true, "pti": true, "fsgsbase": true, "tsc_adjust": true, "smep": true, "dtherm": true, "ida": true, "arat": true, "pln": true, "pts": true}}, {"id": "cpu:1", "class": "processor", "claimed": true, "product": "Intel(R) Xeon(R) CPU E5-2670 v2 @ 2.50GHz", "vendor": "Intel Corp.", "physid": "2", "businfo": "cpu@1", "width": 64, "capabilities": {"fpu": "mathematical co-processor", "fpu_exception": "FPU exceptions reporting", "wp": true, "vme": "virtual mode extensions", "de": "debugging extensions", "pse": "page size extensions", "tsc": "time stamp counter", "msr": "model-specific registers", "pae": "4GB+ memory addressing (Physical Address Extension)", "mce": "machine check exceptions", "cx8": "compare and exchange 8-byte", "apic": "on-chip advanced programmable interrupt controller (APIC)", "sep": "fast system calls", "mtrr": "memory type range registers", "pge": "page global enable", "mca": "machine check architecture", "cmov": "conditional move instruction", "pat": "page attribute table", "pse36": "36-bit page size extensions", "clflush": true, "dts": "debug trace and EMON store MSRs", "mmx": "multimedia extensions (MMX)", "fxsr": "fast floating point save/restore", "sse": "streaming SIMD extensions (SSE)", "sse2": "streaming SIMD extensions (SSE2)", "ss": "self-snoop", "syscall": "fast system calls", "nx": "no-execute bit (NX)", "rdtscp": true, "x86-64": "64bits extensions (x86-64)", "constant_tsc": true, "arch_perfmon": true, "pebs": true, "bts": true, "nopl": true, "xtopology": true, "tsc_reliable": true, "nonstop_tsc": true, "cpuid": true, "aperfmperf": true, "pni": true, "pclmulqdq": true, "ssse3": true, "cx16": true, "pcid": true, "sse4_1": true, "sse4_2": true, "x2apic": true, "popcnt": true, "tsc_deadline_timer": true, "aes": true, "xsave": true, "avx": true, "f16c": true, "rdrand": true, "hypervisor": true, "lahf_lm": true, "cpuid_fault": true, "pti": true, "fsgsbase": true, "tsc_adjust": true, "smep": true, "dtherm": true, "ida": true, "arat": true, "pln": true, "pts": true}}, {"id": "cpu:2", "class": "processor", "claimed": true, "product": "Intel(R) Xeon(R) CPU E5-2670 v2 @ 2.50GHz", "vendor": "Intel Corp.", "physid": "3", "businfo": "cpu@2", "width": 64, "capabilities": {"fpu": "mathematical co-processor", "fpu_exception": "FPU exceptions reporting", "wp": true, "vme": "virtual mode extensions", "de": "debugging extensions", "pse": "page size extensions", "tsc": "time stamp counter", "msr": "model-specific registers", "pae": "4GB+ memory addressing (Physical Address Extension)", "mce": "machine check exceptions", "cx8": "compare and exchange 8-byte", "apic": "on-chip advanced programmable interrupt controller (APIC)", "sep": "fast system calls", "mtrr": "memory type range registers", "pge": "page global enable", "mca": "machine check architecture", "cmov": "conditional move instruction", "pat": "page attribute table", "pse36": "36-bit page size extensions", "clflush": true, "dts": "debug trace and EMON store MSRs", "mmx": "multimedia extensions (MMX)", "fxsr": "fast floating point save/restore", "sse": "streaming SIMD extensions (SSE)", "sse2": "streaming SIMD extensions (SSE2)", "ss": "self-snoop", "syscall": "fast system calls", "nx": "no-execute bit (NX)", "rdtscp": true, "x86-64": "64bits extensions (x86-64)", "constant_tsc": true, "arch_perfmon": true, "pebs": true, "bts": true, "nopl": true, "xtopology": true, "tsc_reliable": true, "nonstop_tsc": true, "cpuid": true, "aperfmperf": true, "pni": true, "pclmulqdq": true, "ssse3": true, "cx16": true, "pcid": true, "sse4_1": true, "sse4_2": true, "x2apic": true, "popcnt": true, "tsc_deadline_timer": true, "aes": true, "xsave": true, "avx": true, "f16c": true, "rdrand": true, "hypervisor": true, "lahf_lm": true, "cpuid_fault": true, "pti": true, "fsgsbase": true, "tsc_adjust": true, "smep": true, "dtherm": true, "ida": true, "arat": true, "pln": true, "pts": true}}, {"id": "cpu:3", "class": "processor", "claimed": true, "product": "Intel(R) Xeon(R) CPU E5-2670 v2 @ 2.50GHz", "vendor": "Intel Corp.", "physid": "4", "businfo": "cpu@3", "width": 64, "capabilities": {"fpu": "mathematical co-processor", "fpu_exception": "FPU exceptions reporting", "wp": true, "vme": "virtual mode extensions", "de": "debugging extensions", "pse": "page size extensions", "tsc": "time stamp counter", "msr": "model-specific registers", "pae": "4GB+ memory addressing (Physical Address Extension)", "mce": "machine check exceptions", "cx8": "compare and exchange 8-byte", "apic": "on-chip advanced programmable interrupt controller (APIC)", "sep": "fast system calls", "mtrr": "memory type range registers", "pge": "page global enable", "mca": "machine check architecture", "cmov": "conditional move instruction", "pat": "page attribute table", "pse36": "36-bit page size extensions", "clflush": true, "dts": "debug trace and EMON store MSRs", "mmx": "multimedia extensions (MMX)", "fxsr": "fast floating point save/restore", "sse": "streaming SIMD extensions (SSE)", "sse2": "streaming SIMD extensions (SSE2)", "ss": "self-snoop", "syscall": "fast system calls", "nx": "no-execute bit (NX)", "rdtscp": true, "x86-64": "64bits extensions (x86-64)", "constant_tsc": true, "arch_perfmon": true, "pebs": true, "bts": true, "nopl": true, "xtopology": true, "tsc_reliable": true, "nonstop_tsc": true, "cpuid": true, "aperfmperf": true, "pni": true, "pclmulqdq": true, "ssse3": true, "cx16": true, "pcid": true, "sse4_1": true, "sse4_2": true, "x2apic": true, "popcnt": true, "tsc_deadline_timer": true, "aes": true, "xsave": true, "avx": true, "f16c": true, "rdrand": true, "hypervisor": true, "lahf_lm": true, "cpuid_fault": true, "pti": true, "fsgsbase": true, "tsc_adjust": true, "smep": true, "dtherm": true, "ida": true, "arat": true, "pln": true, "pts": true}}], "ip_info": [{"ifindex": 1, "ifname": "lo", "flags": ["LOOPBACK", "UP", "LOWER_UP"], "mtu": 65536, "qdisc": "noqueue", "operstate": "UNKNOWN", "group": "default", "txqlen": 1000, "link_type": "loopback", "address": "00:00:00:00:00:00", "broadcast": "00:00:00:00:00:00", "addr_info": [{"family": "inet", "local": "127.0.0.1", "prefixlen": 8, "scope": "host", "label": "lo", "valid_life_time": 4294967295, "preferred_life_time": 4294967295}, {"family": "inet6", "local": "::1", "prefixlen": 128, "scope": "host", "valid_life_time": 4294967295, "preferred_life_time": 4294967295}]}, {"ifindex": 2, "link_index": 2, "ifname": "eth0", "flags": ["BROADCAST", "MULTICAST", "UP", "LOWER_UP"], "mtu": 1500, "qdisc": "noqueue", "operstate": "UP", "group": "default", "link_type": "ether", "address": "1e:fe:67:af:50:ba", "broadcast": "ff:ff:ff:ff:ff:ff", "link_netnsid": 0, "addr_info": [{"family": "inet", "local": "172.16.21.1", "prefixlen": 24, "broadcast": "172.16.21.255", "scope": "global", "label": "eth0", "valid_life_time": 4294967295, "preferred_life_time": 4294967295}, {"family": "inet6", "local": "fe80::1cfe:67ff:feaf:50ba", "prefixlen": 64, "scope": "link", "valid_life_time": 4294967295, "preferred_life_time": 4294967295}]}, {"ifindex": 3, "link_index": 6, "ifname": "eth1", "flags": ["BROADCAST", "MULTICAST", "UP", "LOWER_UP"], "mtu": 1500, "qdisc": "noqueue", "operstate": "UP", "group": "default", "link_type": "ether", "address": "86:a4:9e:fb:f6:a6", "broadcast": "ff:ff:ff:ff:ff:ff", "link_netnsid": 0, "addr_info": [{"family": "inet", "local": "10.89.0.2", "prefixlen": 24, "broadcast": "10.89.0.255", "scope": "global", "label": "eth1", "valid_life_time": 4294967295, "preferred_life_time": 4294967295}, {"family": "inet6", "local": "fe80::84a4:9eff:fefb:f6a6", "prefixlen": 64, "scope": "link", "valid_life_time": 4294967295, "preferred_life_time": 4294967295}]}, {"ifindex": 4, "ifname": "tun0", "flags": ["POINTOPOINT", "MULTICAST", "NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 100, "link_type": "none", "addr_info": []}, {"ifindex": 5, "ifname": "tun1", "flags": ["POINTOPOINT", "MULTICAST", "NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 100, "link_type": "none", "addr_info": []}, {"ifindex": 6, "ifname": "tun2", "flags": ["POINTOPOINT", "MULTICAST", "NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 100, "link_type": "none", "addr_info": []}, {"ifindex": 7, "ifname": "tun3", "flags": ["POINTOPOINT", "MULTICAST", "NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 100, "link_type": "none", "addr_info": []}, {"ifindex": 8, "ifname": "tun4", "flags": ["POINTOPOINT", "MULTICAST", "NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 100, "link_type": "none", "addr_info": []}, {"ifindex": 9, "ifname": "tap0", "flags": ["BROADCAST", "MULTICAST"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 100, "link_type": "ether", "address": "7e:ac:71:0c:9d:c5", "broadcast": "ff:ff:ff:ff:ff:ff", "addr_info": []}, {"ifindex": 10, "ifname": "tap1", "flags": ["BROADCAST", "MULTICAST"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 100, "link_type": "ether", "address": "46:18:21:98:b3:d2", "broadcast": "ff:ff:ff:ff:ff:ff", "addr_info": []}, {"ifindex": 11, "ifname": "tap2", "flags": ["BROADCAST", "MULTICAST"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 100, "link_type": "ether", "address": "fe:e6:52:3b:fc:0c", "broadcast": "ff:ff:ff:ff:ff:ff", "addr_info": []}, {"ifindex": 12, "ifname": "tap3", "flags": ["BROADCAST", "MULTICAST"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 100, "link_type": "ether", "address": "12:14:58:79:19:87", "broadcast": "ff:ff:ff:ff:ff:ff", "addr_info": []}, {"ifindex": 13, "ifname": "tap4", "flags": ["BROADCAST", "MULTICAST"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 100, "link_type": "ether", "address": "da:1b:8a:60:52:5f", "broadcast": "ff:ff:ff:ff:ff:ff", "addr_info": []}, {"ifindex": 14, "ifname": "taps0", "flags": ["BROADCAST", "MULTICAST"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 100, "link_type": "ether", "address": "56:0a:41:de:80:3b", "broadcast": "ff:ff:ff:ff:ff:ff", "addr_info": []}, {"ifindex": 15, "ifname": "taps1", "flags": ["BROADCAST", "MULTICAST"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 100, "link_type": "ether", "address": "8a:e1:50:61:2b:28", "broadcast": "ff:ff:ff:ff:ff:ff", "addr_info": []}, {"ifindex": 16, "ifname": "taps2", "flags": ["BROADCAST", "MULTICAST"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 100, "link_type": "ether", "address": "a2:ca:60:6c:1a:65", "broadcast": "ff:ff:ff:ff:ff:ff", "addr_info": []}, {"ifindex": 17, "ifname": "taps3", "flags": ["BROADCAST", "MULTICAST"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 100, "link_type": "ether", "address": "7a:9e:d5:09:7b:18", "broadcast": "ff:ff:ff:ff:ff:ff", "addr_info": []}, {"ifindex": 18, "ifname": "taps4", "flags": ["BROADCAST", "MULTICAST"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 100, "link_type": "ether", "address": "66:19:25:45:2c:dc", "broadcast": "ff:ff:ff:ff:ff:ff", "addr_info": []}, {"ifindex": 19, "link": "lo", "ifname": "ipsec1", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 20, "link": "lo", "ifname": "ipsec2", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 21, "link": "lo", "ifname": "ipsec3", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 22, "link": "lo", "ifname": "ipsec4", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 23, "link": "lo", "ifname": "ipsec5", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 24, "link": "lo", "ifname": "ipsec6", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 25, "link": "lo", "ifname": "ipsec7", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 26, "link": "lo", "ifname": "ipsec8", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 27, "link": "lo", "ifname": "ipsec9", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 28, "link": "lo", "ifname": "ipsec10", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 29, "link": "lo", "ifname": "ipsec11", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 30, "link": "lo", "ifname": "ipsec12", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 31, "link": "lo", "ifname": "ipsec13", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 32, "link": "lo", "ifname": "ipsec14", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 33, "link": "lo", "ifname": "ipsec15", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 34, "link": "lo", "ifname": "ipsec16", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 35, "link": "lo", "ifname": "ipsec17", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 36, "link": "lo", "ifname": "ipsec18", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 37, "link": "lo", "ifname": "ipsec19", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 38, "link": "lo", "ifname": "ipsec20", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 39, "link": "lo", "ifname": "ipsec21", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 40, "link": "lo", "ifname": "ipsec22", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 41, "link": "lo", "ifname": "ipsec23", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 42, "link": "lo", "ifname": "ipsec24", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 43, "link": "lo", "ifname": "ipsec25", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 44, "link": "lo", "ifname": "ipsec26", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 45, "link": "lo", "ifname": "ipsec27", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 46, "link": "lo", "ifname": "ipsec28", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 47, "link": "lo", "ifname": "ipsec29", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 48, "link": "lo", "ifname": "ipsec30", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 49, "link": "lo", "ifname": "ipsec31", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 50, "link": "lo", "ifname": "ipsec32", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 51, "link": "lo", "ifname": "ipsec33", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 52, "link": "lo", "ifname": "ipsec34", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 53, "link": "lo", "ifname": "ipsec35", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 54, "link": "lo", "ifname": "ipsec36", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 55, "link": "lo", "ifname": "ipsec37", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 56, "link": "lo", "ifname": "ipsec38", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 57, "link": "lo", "ifname": "ipsec39", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 58, "link": "lo", "ifname": "ipsec40", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 59, "link": "lo", "ifname": "prisma1", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 60, "link": "lo", "ifname": "prisma2", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 61, "link": "lo", "ifname": "prisma3", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 62, "link": "lo", "ifname": "prisma4", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 63, "link": "lo", "ifname": "prisma5", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 64, "link": "lo", "ifname": "prisma6", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 65, "link": "lo", "ifname": "prisma7", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 66, "link": "lo", "ifname": "prisma8", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 67, "link": "lo", "ifname": "prisma9", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}, {"ifindex": 68, "link": "lo", "ifname": "prisma10", "flags": ["NOARP"], "mtu": 1500, "qdisc": "noop", "operstate": "DOWN", "group": "default", "txqlen": 1000, "link_type": "none", "addr_info": []}]}, "provisioning_server_uri": "https://chiefnet-stg-api.yavar.in/v1/devices/provision"}'
	updated_json=$(echo "$json_data" | jq --arg new_uuid "$new_uuid" '.system_information.uuid = $new_uuid')
	echo "$updated_json" > SystemConfiguration.json

	sudo podman cp SystemConfiguration.json chiefnet_container${i}:/home/chiefnet/ChiefNet/ConfigurationFiles/SystemConfiguration.json


        # Grep IP for adding in ubuntu container
        chiefnetip=$(sudo podman exec --privileged -it chiefnet_container${i} /bin/bash \
        -c "hostname -I | awk '{print \$1}' | tr -d '\n'")

        sudo podman exec --privileged -it chiefnet_container${i} /bin/bash \
        -c "iptables -t nat -A POSTROUTING -j MASQUERADE"

        # cpe-start-script
        sudo podman exec --privileged -dit chiefnet_container${i} /bin/bash -c "bash /home/chiefnet/ChiefNet/StartupScripts/cpe-start-script.sh"

        # Ubuntu container
        sudo podman run --privileged -d --network=$lan_network_name --name ubuntu-container${i} ubuntu-slave

        # Delete old route
        # sudo podman exec --privileged -it ubuntu-container${i} /bin/bash -c "ip route del default via 172.16.$((20 + i)).2 dev eth0"
        sudo podman exec --privileged -it ubuntu-container${i} /bin/bash -c "ip route del default"

        # Add new route
        sudo podman exec --privileged -it ubuntu-container${i} /bin/bash \
        -c "ip route add default via $chiefnetip dev eth0"
        sleep 2
done
