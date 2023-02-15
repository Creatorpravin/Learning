***************************************
* chiefnet-connectivity-check.conf *
***************************************
    -----------------
    | Description |
    -----------------
        This section controls NetworkManager's optional connectivity checking functionality.
        This allows NetworkManager to detect whether or not the system can actually access the internet

        In chiefnet-connectivity-check.conf, we check the connectivity using the custom URL for interval of 5 seconds

    -------------------------
    | Steps to be follow |
    -------------------------
        --> Should be created as root user
        --> Should be present in the /etc/NetworkManager/conf.d directory

****************************
* chiefnet-custom-route *
****************************
    -----------------
    | Description |
    -----------------
        chiefnet-custom-route script is used to add/remove a custom routing table whenever WAN interface is physically plugged in / plugged off.
        This custom routing table is helpfull to configure and achieve the traffic steering functionality using Chiefnet CPE Application

        NetworkManager will execute scripts in the /etc/NetworkManager/dispatcher.d directory or subdirectories in 
        alphabetical order in response to network events. Each script should be a regular executable file owned by root. 

    -------------------------
    | Steps to be follow |
    -------------------------
        --> Should be created as root user
        --> Should have execution permission (command: sudo chmod 755 chiefnet-custom-route)
        --> Should be present in the /etc/NetworkManager/dispatcher.d directory

*****************************
* chiefnet-sdwan.service *
*****************************
    -----------------
    | Description |
    -----------------
        Services are essential background processes that are usually run while booting up and shut down with the OS.
        chiefnet-sdwan.service file is used to start and run the Chiefnet-CPE Application in background while boot up.

    -------------------------
    | Steps to be follow |
    -------------------------
        --> Should be created as root user
        --> Should be present in the /etc/systemd/system directory
        --> Should enable the service (command: sudo systemctl enable chiefnet-sdwan.service)

****************************
* NetworkManager.conf *
****************************
    -----------------
    | Description |
    -----------------
        NetworkManager.conf is the configuration file for NetworkManager. It is used to set up various aspects of NetworkManager's behaviour.

        The changes done in NetworkManager.conf are listed below
            1. dns=resolvconf 
                    Description: NetworkManager will run resolvconf to update the DNS configuration in /etc/resolv.conf
            
            2. carrier-wait-timeout=0
                    Description: Configure NetworkManager to set the ignore timeout second as 0 to avoid default 5 seconds delay 

            3. [device-interface-enp3s0]
               match-device=interface-name:enp3s0
               ignore-carrier=yes

               [device-interface-enp4s0]
               match-device=interface-name:enp4s0
               ignore-carrier=yes

                    Description: Configure the NetworkManager to ignore the carrier flag for the enp3s0 and enp4s0 interfaces

    -------------------------
    | Steps to be follow |
    -------------------------
        --> Replace this file content in /etc/NetworkManager/NetworkManager.conf file

*****************************
* sdwan-systemupgrade.service *
*****************************
    -----------------
    | Description |
    -----------------
        Services are essential background processes that are usually run while booting up and shut down with the OS.
        sdwan-systemupgrade.service file is used to start and run the SystemUpgrade Application in background while boot up.

    -------------------------
    | Steps to be follow |
    -------------------------
        --> Should be created as root user
        --> Should be present in the /etc/systemd/system directory
        --> Should enable the service (command: sudo systemctl enable sdwan-systemupgrade.service)

*****************************
* telegraf.service *
*****************************
    -----------------
    | Description |
    -----------------
        Services are essential background processes that are usually run while booting up and shut down with the OS.
        telegraf.service file is used to start and run the telegraf application in background while boot up with the 
        configuration specified in the telegraf.conf.

    -------------------------
    | Steps to be follow |
    -------------------------
        --> Should be created as root user
        --> Should be present in the /etc/systemd/system directory
        --> Should enable the service (command: sudo systemctl enable telegraf.service)

*****************************
* telegraf.conf *
*****************************
    -----------------
    | Description |
    -----------------
        telegraf.conf file is used to configure the telegraf application.

    -------------------------
    | Steps to be follow |
    -------------------------
        --> Should be created as root user
        --> Should be present in the /etc/telegraf/ directory

*****************************
* rt_tables *
*****************************
    -----------------
    | Description |
    -----------------
        rt_tables file is used to initialize the custom routing table name.

    -------------------------
    | Steps to be follow |
    -------------------------
        --> Should be created as root user
        --> Should be present in the /etc/iproute2/rt_tables directory

Note: Reboot system once to see all the above configuration change get reflected
