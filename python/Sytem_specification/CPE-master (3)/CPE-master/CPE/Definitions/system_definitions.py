#Base directory
BASE_DIRECTORY = "/home/chiefnet/ChiefNet/"

# SystemConfigurationManager
SYS_CONFIG_FILE_PATH_NAME = BASE_DIRECTORY + "ConfigurationFiles/SystemConfiguration.json"
DEVICE_UUID_KEY = "uuid"
PROVISIONINS_DETAILS_KEY = "provisioning_details"
SYSTEM_INFORMATION_KEY = "system_information"
PROVISIONING_SERVER_URI_KEY= "provisioning_server_uri"
PACKAGE_VERSION_KEY = "package_version"

# ProvisionManager
SYSTEM_PROVISION_PATH_NAME = BASE_DIRECTORY + "ConfigurationFiles/SystemProvision.json"
WEBSOCKET_SERVER_URI_PATH_NAME = BASE_DIRECTORY + "ConfigurationFiles/WebsocketServerUri.json"
SYSTEMUPGRADE_SERVER_URI_PATH_NAME = BASE_DIRECTORY + "ConfigurationFiles/SystemUpgradeServerUri.json"
PROVISIONING_STATUS_KEY = "provision_status"
SYSTEMUPGRADE_SERVER_URI_KEY = "system_upgrade_websocket_server_url"
WEBSOCKET_SERVER_URI_KEY = "configuration_websocket_server_url"
PROVISIONING_RETRY_TIMEOUT = 10 # Unit in seconds

# File operation constants
FILE_READ_MODE = "r"
FILE_WRITE_MODE = "w"
FILE_APPEND_MODE = "a"
FILE_WRITE_BINARY_MODE = "wb"

MAX_DATA_QUEUE_SIZE = 1000

# Time interval at which the ping frame is sent, value in seconds
PING_INTERVAL = 3
# If the corresponding pong frame isn’t received within PING_TIMEOUT seconds, the connection is considered unusable, value in seconds
PING_TIMEOUT = 3
# Maximum wait time in seconds for completing the closing handshake and terminating the TCP connection, value in seconds
CLOSE_TIMEOUT = 3

# ServiceManager
USER_CONFIG_FILE_PATH = "/var/SDWAN/ConfigurationFiles"
TEMP_USER_CONFIG_FILE_PATH = "/tmp/SDWAN/ConfigurationFiles"
AUTHORIZATION_HTTP_HEADER_KEY = "Authorization"

# Factory reset configuration path
FACTORY_RESET_FOLDER_PATH = BASE_DIRECTORY + "FactoryReset/"
USER_CONFIG_FOLDER_PATH = "ConfigurationFiles"

# Qos configuration
QOS_CONFIG_FILE_NAME = "qos-configuration.sh"
QOS_FACTORY_RESERT_FOLDER_PATH = FACTORY_RESET_FOLDER_PATH + "qos_configuration"

#Traffic steering configuration
IPTABLES_CONFIG_FILE_NAME = "initial-configuration.txt"
TRAFFIC_STEERING_FACTORY_RESET_FOLDER_PATH = FACTORY_RESET_FOLDER_PATH + "traffic_steering_configuration"

# Dhcp and Split dns configuration
DNSMASQ_CONFIG_FOLDER_PATH = "/etc/dnsmasq.d"
DNSMASQ_FACTORY_RESET_FOLDER_PATH = FACTORY_RESET_FOLDER_PATH + "dnsmasq_configuration"
DNSMASQ_CONFIG_FILE_NAME = "constants-dnsmasq.conf"

# Network interface configuration
NETWORK_INTERFACE_CONFIG_FOLDER_PATH = "/etc/netplan/"
NETWORK_INTERFACE_CONFIG_YAML_FILE_NAME = "01-ethernet-configuration.yaml"
NETWORK_INTERFACE_FACTORY_RESET_FOLDER_PATH = FACTORY_RESET_FOLDER_PATH + "network_configuration"

# OPENVPN configuration
OPENVPN_CONFIG_FOLDER_PATH = "/etc/openvpn"
OPENVPN_FACTORY_RESET_FOLDER_PATH = FACTORY_RESET_FOLDER_PATH + "openvpn_configuration"
OPENVPN_FILE_EXTENSION = "ovpn.conf"
VPN_UP_FILE_NAME = "vpn-up.sh"
VPN_DOWN_FILE_NAME = "vpn-down.sh"

#ROUTING configuration
ROUTING_CONFIG_FOLDER_PATH = "/etc/frr"
ROUTING_FACTORY_RESET_FOLDER_PATH = FACTORY_RESET_FOLDER_PATH + "frr_configuration"

# HttpCommunicationManager
HTTP_TIMEOUT = 4    # Unit in seconds

# SystemUpgrade
SYSTEM_UPGRADE_PID = BASE_DIRECTORY + "SystemUpgrade/SystemUpgrade-application.pid"
SYSTEM_UPGRADE_SERVICE = "sdwan-systemupgrade.service"

# Version
CPE_VERSION_FILE_PATH = BASE_DIRECTORY + "CPE/version.txt"

# RemoteSSH configuration
REMOTE_SSH_CONFGURATION_FILE_NAME = "remote-ssh-configuration.sh"

# System Preparation configuration
HOSTNAME_PREFIX = "chiefnet-"

DEVELOPMENT_PROVISIONING_URL = "https://chiefnet-dev-api.yavar.in/v1/devices/provision"
PRODUCTION_PROVISIONING_URL = "https://chiefnetapi.yavar.in/v1/devices/provision"

DEVELOPMENT_SYSTEM_OPERATION_MODE = "DEVELOPMENT"
PRODUCTION_SYSTEM_OPERATION_MODE = "PRODUCTION"

DEVICE_MODEL = "G1"
OPERATION_MODE = DEVELOPMENT_SYSTEM_OPERATION_MODE

WAN_INTERFACE_COUNT = 2