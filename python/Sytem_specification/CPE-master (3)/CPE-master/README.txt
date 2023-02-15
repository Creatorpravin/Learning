##################################################################################################################################################

1. This section in README.txt explains where to place the folders in CPE device.
NOTE:- To prepare CPE device to functional state, please take a look at SystemPreparation section in Wiki.
(https://dev.azure.com/NetconProducts/ChiefNet/_wiki/wikis/ChiefNet.wiki/128/SystemPreparation)

##################################################################################################################################################

***************************************
* ConfigurationFiles *
***************************************
    -----------------
    | Description |
    -----------------
        This folder contains all the CPE application related configuration files.

    -------------------------
    | Steps to be follow |
    -------------------------
        --> Should copy ConfigurationFiles directory in CPE device to /home/chiefnet/ChiefNet/

***************************************
* CPE *
***************************************
    -----------------
    | Description |
    -----------------
        This folder contains core python scripts for CPE application

    -------------------------
    | Steps to be follow |
    -------------------------
        --> Should copy CPE directory in CPE device to /home/chiefnet/ChiefNet/

***************************************
* FactoryReset *
***************************************
    -----------------
    | Description |
    -----------------
        This folder contains all the default configuration fiiles for the system.

    -------------------------
    | Steps to be follow |
    -------------------------
        --> Should copy FactoryReset directory in CPE device to /home/chiefnet/ChiefNet/

***************************************
* StartupScripts *
***************************************
    -----------------
    | Description |
    -----------------
        This folder contains the startup scripts for CPE application and for systemupgrade application

    -------------------------
    | Steps to be follow |
    -------------------------
        --> Should copy StartupScripts directory in CPE device to /home/chiefnet/ChiefNet/

***************************************
* SystemUpgrade *
***************************************
    -----------------
    | Description |
    -----------------
        This folder contains all the python scripts for system upgrade application

    -------------------------
    | Steps to be follow |
    -------------------------
        --> Should copy SystemUpgrade directory in CPE device to /home/chiefnet/ChiefNet/

***************************************
* SystemSetup *
***************************************
    -----------------
    | Description |
    -----------------
        This folder contains all the system configuration files for CPE application to function.
        A README.txt is created in the SystemSetup folder which will give the information about placing the files in specific directory

    -------------------------
    | Steps to follow|
    -------------------------
        Place the files in SystemSetup directory as mentioned in README.txt under SystemSetup folder


##################################################################################################################################################

2. This section in README.txt explains where to place default configuration files inorder for CPE to start in expected configuration. 
FactoryReset directory contains all the default configuration. Please place the system configuration files in specifed directory 
as shown below.

##################################################################################################################################################
***************************************
* FactoryReset/dnsmasq_configuration/constants-dnsmasq.conf *
***************************************
    -----------------
    | Description |
    -----------------
        Default configuration for dnsmasq.

    -------------------------
    | Steps to follow|
    -------------------------
        --> Should be present in the /etc/dnsmasq.d directory

***************************************
* FactoryReset/frr_configuration *
***************************************
    -----------------
    | Description |
    -----------------
        Default configuration for frr(Routing tool).

    -------------------------
    | Steps to follow|
    -------------------------
        --> All the configuation files in the FactoryReset/frr_configuration should be present in the /etc/frr/ directory

***************************************
* FactoryReset/network_configuration *
***************************************
    -----------------
    | Description |
    -----------------
        Default configuration for network interface.

    -------------------------
    | Steps to follow|
    -------------------------
        --> Should be present in the /etc/netplan/ directory

***************************************
* FactoryReset/qos_configuration *
***************************************
    -----------------
    | Description |
    -----------------
        Default configuration for qos.

    -------------------------
    | Steps to follow|
    -------------------------
        --> Should be present in the /var/SDWAN/ConfigurationFiles directory

***************************************
* FactoryReset/traffic_steering_configuration *
***************************************
    -----------------
    | Description |
    -----------------
        Default configuration for traffic steering.

    -------------------------
    | Steps to follow|
    -------------------------
        --> Should be present in the /var/SDWAN/ConfigurationFiles/traffic-steering-configuration directory

    
    




