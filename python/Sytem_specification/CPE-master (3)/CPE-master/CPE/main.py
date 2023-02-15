import signal
import sys
import os

from CoreCode.websocket_manager import WebSocketManager
from CoreCode.http_communication_manager import HttpCommunicationManager

from CoreCode.data_manager import DataManager
from CoreCode.system_configuration_manager import SystemConfigurationManager
from CoreCode.action_handler import ActionHandler
from CoreCode.response_manager import ResponseManager

from CoreCode.service_manager import ServiceManager
from CoreCode.traffic_steering_manager import TrafficSteeringManager
from CoreCode.qos_manager import QoSManager
from CoreCode.network_interface_manager import NetworkInterfaceManager
from CoreCode.dhcp_manager import DHCPManager
from CoreCode.split_dns_manager import SplitDNSManager
from CoreCode.vpn_manager import VPNManager
from CoreCode.delete_device_manager import DeleteDeviceManager
from CoreCode.reset_manager import ResetManager
from CoreCode.route_manager import RouteManager
from CoreCode.remote_ssh_manger import RemoteSSHManager
from CoreCode.settings_manager import SettingsManager

import Definitions.system_definitions as SystemDefinitions
import Definitions.message_code_definitions as MessageCodeDefinitions

from CoreCode.provision_manager import ProvisionManager
from CoreCode.system_preparation_manager import SystemPrepartionManager

import CoreCode.logger as Logger

PROCESS_ID_FILEPATH = "CPE-application.pid"

QUERY_SYMBOL = "?"
DEVICE_ID_QUERY_KEY = "device_id"
EQUALTO_SYMBOL = "="


def sigterm_handler(_signo, _stack_frame):
    print("SIGTERM/SIGINT received. Exiting system")
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, sigterm_handler)
    signal.signal(signal.SIGTERM, sigterm_handler)

    # Get the current CPE Process id and log it to a file
    cpe_application_process_id = os.getpid()
    with open(PROCESS_ID_FILEPATH, SystemDefinitions.FILE_WRITE_MODE) as pid_file:
        pid_file.write(str(cpe_application_process_id))

    system_preparation_manager = SystemPrepartionManager()

    system_configuration_manager = SystemConfigurationManager()

    provision_server_http_communication_manager = HttpCommunicationManager(system_configuration_manager=system_configuration_manager, authorization_request_header="")
    provisionManager = ProvisionManager(system_configuration_manager=system_configuration_manager, communication_manager=provision_server_http_communication_manager)

    websocket_server_uri = provisionManager.get_websocket_server_uri() + QUERY_SYMBOL + DEVICE_ID_QUERY_KEY + EQUALTO_SYMBOL + system_configuration_manager.get_device_id()
    websocket_manager = WebSocketManager(websocket_server_uri=websocket_server_uri)

    reset_manager = ResetManager()

    response_manager = ResponseManager(communication_manager=websocket_manager, system_configuration_manager=system_configuration_manager)

    action_handler = ActionHandler(system_configuration_manager=system_configuration_manager, response_manager=response_manager)
    websocket_manager.register_receive_data_callback(receive_data_callback=action_handler.message_receive_callback)

    http_communication_manager = HttpCommunicationManager(system_configuration_manager=system_configuration_manager, authorization_request_header=system_configuration_manager.get_device_id())
    data_manager = DataManager(communication_manager=http_communication_manager)

    traffic_steering_manager = TrafficSteeringManager(data_manager=data_manager, response_manager=response_manager)
    qos_manager = QoSManager(data_manager=data_manager, response_manager=response_manager)
    network_interface_manager = NetworkInterfaceManager(data_manager=data_manager, response_manager=response_manager)
    dhcp_manager = DHCPManager(data_manager=data_manager, response_manager=response_manager)
    split_dns_manager = SplitDNSManager(data_manager=data_manager, response_manager=response_manager)
    vpn_manager = VPNManager(data_manager=data_manager, response_manager=response_manager)
    delete_device_manager = DeleteDeviceManager(data_manager=data_manager,response_manager=response_manager)
    route_manager = RouteManager(data_manager=data_manager,response_manager=response_manager)
    remote_ssh_manager = RemoteSSHManager(data_manager=data_manager, response_manager=response_manager)
    settings_manager = SettingsManager(data_manager=data_manager, response_manager=response_manager)

    action_handler.register_service_manager_callback(service_code=MessageCodeDefinitions.TRAFFIC_STEERING_MANAGER, service_manager=traffic_steering_manager)
    action_handler.register_service_manager_callback(service_code=MessageCodeDefinitions.QOS_MANAGER, service_manager=qos_manager)
    action_handler.register_service_manager_callback(service_code=MessageCodeDefinitions.NETWORK_INTERFACE_MANAGER, service_manager=network_interface_manager)
    action_handler.register_service_manager_callback(service_code=MessageCodeDefinitions.DHCP_MANAGER, service_manager=dhcp_manager)
    action_handler.register_service_manager_callback(service_code=MessageCodeDefinitions.SPLIT_DNS_MANAGER, service_manager=split_dns_manager)
    action_handler.register_service_manager_callback(service_code=MessageCodeDefinitions.VPN_MANAGER, service_manager=vpn_manager)
    action_handler.register_service_manager_callback(service_code=MessageCodeDefinitions.DELETE_DEVICE_MANAGER, service_manager=delete_device_manager)
    action_handler.register_service_manager_callback(service_code=MessageCodeDefinitions.ROUTE_MANAGER, service_manager=route_manager)
    action_handler.register_service_manager_callback(service_code=MessageCodeDefinitions.REMOTE_SSH_MANAGER, service_manager=remote_ssh_manager)
    action_handler.register_service_manager_callback(service_code=MessageCodeDefinitions.SETTINGS_MANAGER, service_manager=settings_manager)

    signal.pause()