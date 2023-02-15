import signal
import sys
import os
import threading
import json
import time

from CoreCode.websocket_manager import WebSocketManager
from CoreCode.system_upgrade_action_handler import SystemUgradeActionHandler
from CoreCode.response_manager import ResponseManager
from CoreCode.system_configuration_manager import SystemConfigurationManager
from CoreCode.system_upgrade import SystemUpgrade
from CoreCode.uri_manager import URIManager

import CoreCode.logger as Logger
import Definitions.system_definitions as SystemDefinitions
import Definitions.message_code_definitions as MessageCodeDefinitions


def usersignal_handler(_signo, _stack_frame):
    device_provisioned_event.set()


def sigterm_handler(_signo, _stack_frame):
    print("SIGTERM/SIGINT received. Exiting system")
    system_upgrade_exit_event.set()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, sigterm_handler)
    signal.signal(signal.SIGTERM, sigterm_handler)
    signal.signal(signal.SIGUSR1, usersignal_handler)

    system_upgrade_application_process_id = os.getpid()
    with open(SystemDefinitions.SYSTEM_UPGRADE_PID, SystemDefinitions.FILE_WRITE_MODE) as pid_file:
        pid_file.write(str(system_upgrade_application_process_id))

    device_provisioned_event = threading.Event()
    system_upgrade_exit_event = threading.Event()
    
    logger = Logger.get_logger(__name__)
    
    system_upgrade_server_uri = str()

    # The below section will be modified by IPC mechanism.
    if ((os.path.exists(SystemDefinitions.SYSTEM_PROVISION_PATH_NAME) == False) or 
        (os.path.exists(SystemDefinitions.SYSTEMUPGRADE_SERVER_URI_PATH_NAME) == False)) == True:
        device_provisioned_event.wait()

    if os.path.exists(SystemDefinitions.SYSTEMUPGRADE_SERVER_URI_PATH_NAME) == True:
        with open(SystemDefinitions.SYSTEMUPGRADE_SERVER_URI_PATH_NAME, SystemDefinitions.FILE_READ_MODE) as system_upgrade_server_uri_file:
            system_upgrade_server_uri = json.load(system_upgrade_server_uri_file)[SystemDefinitions.SYSTEMUPGRADE_SERVER_URI_KEY]
    else:
        logger.error("SystemUpgrade uri not found")

    system_configuration_manager = SystemConfigurationManager()

    uri_manager = URIManager(websocket_server_base_uri=system_upgrade_server_uri, cpe_version_file_path=SystemDefinitions.CPE_VERSION_FILE_PATH, system_configuration_manager=system_configuration_manager)
    websocket_manager = WebSocketManager(uri_manager=uri_manager)
    
    response_manager = ResponseManager(communication_manager=websocket_manager, system_configuration_manager=system_configuration_manager)

    system_upgrade_action_handler = SystemUgradeActionHandler(system_configuration_manager=system_configuration_manager, response_manager=response_manager)
    websocket_manager.register_receive_data_callback(receive_data_callback=system_upgrade_action_handler.message_receive_callback)

    system_upgrade = SystemUpgrade(response_manager=response_manager)
    
    system_upgrade_action_handler.register_message_received_callback(MessageCodeDefinitions.SYSTEM_UPGRADE, system_upgrade.system_upgrade_request_callback)

    system_upgrade_exit_event.wait()
