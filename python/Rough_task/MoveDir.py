import shutil

source = "/home/praveen/test/yes"
destination = "/home/praveen/test/telegraf"

resu = shutil.move( source , destination )
print(resu)

import os
import psutil
import subprocess
import threading
from CoreCode.service_manager import ServiceManager
import Definitions.message_code_definitions as MessageCodeDefinitions
import Definitions.message_definitions as MessageDefinitions
import CoreCode.logger as Logger

RECEIVED_PACKET_CAPTURE_REQUEST = "Packet capture request has been received."
STARTED_PACKET_CAPTURING = "Packet capturing is started."
PACKET_CAPTURE_IS_DONE = "Packet capturing is completed."
RECEIVED_PACKET_CAPTURE_STOP_REQUEST = "Packet capture stop request is received."
STARTED_STOP_PACKET_CAPTURE = "Stopping the packet capture process."
STOPPED_PACKET_CAPTURE = "Packet cpature is stopped."
# Errors
EXISTING_REQUEST_IS_NOT_COMPLETED = "Packet capture is already in-prgress"
INTERFACE_NOT_PROVIDED = "No interface found in the tcpdump command."
FILE_NOT_FOUND = "No file found in the tcpdump command."
INTERFACE_NOT_FOUND = "Requested interface not found in the device."
INTERFACE_DOWN_STATE = "Packet capture requested interface is in down state."
DIRECTORY_OR_FILE_ERROR = "Error on creating provided file/dirctory."
FAILED_TO_CAPTURE_PACKETS = "Failed to capture the packets."
PACKET_CAPTURE_PROCESS_NOT_FOUND = "No in-progress packet capture process"


class PacketCaptureManager(ServiceManager):
    """
    PacketCaptureManager Class
    This class extends ServiceManager and is responsible for managing packet capture functionality.
    Attributes:
        __logger (Logger): An instance of the logger for logging information and errors.
        __interface (str): Stores the network interface specified for packet capture.
        __tcpdump_command (str): Stores the tcpdump command provided for packet capture.
        __output_file (str): Stores the output file path specified for storing captured packets.
        __output_file_path (str): Full path of the output file after decoding and validation.
    Methods:
        __init__(self, data_manager, response_manager):
            Constructor method for initializing the PacketCaptureManager.
        __capture_packets(self):
            Method responsible for initiating the packet capture process.
        __decode_tcpdump_command(self):
            Decodes the tcpdump command to extract the network interface and output file.
        __is_interface_exists_and_up(self):
            Checks if the specified network interface is both existing and up.
        __create_directory_and_file(self):
            Creates the directory and file specified for storing captured packets.
        __capture_packets_thread(self):
            Threaded method for executing the tcpdump command and capturing packets.
        __start_capturing_packets_on_interface(self):
            Starts a thread to capture packets on the specified network interface and send to the server.
        __stop_capturing_packets(self):
            Stops the packet capture process.
        __stop_capturing(self):
            Stops the packet capture process execution.
        __handle_packet_capture_success(self):
            Handles the success of packet capture process.
    """

    def __init__(self, data_manager, response_manager):
        """
        Constructor method for initializing the PacketCaptureManager.
        Args:
            data_manager: An instance of the data manager class.
            response_manager: An instance of the response manager class.
        """
        self.__logger = Logger.get_logger(__name__)
        self.__logger.info("PacketCaptureManager initializer starts")
        event_dict = {}
        event_dict[MessageCodeDefinitions.CAPTURE_PACKETS] = self.__capture_packets
        event_dict[
            MessageCodeDefinitions.STOP_CAPTURE_PACKETS
        ] = self.__stop_capturing_packets
        super().__init__(
            data_manager,
            response_manager,
            event_dict,
        )
        self.__in_progress = False
        self.__interface = None
        self.__tcpdump_command = None
        self.__output_file = None
        self.__output_file_path = None
        self.__process = None
        self.__logger.info("PacketCaptureManager initializer ends")

    def __capture_packets(self):
        """
        Method responsible for initiating the packet capture process.
        Returns:
            bool: True if packet capture is successful, False otherwise.
        """
        try:
            if not self.__in_progress:
                self.__in_progress = True
                self._response_manager.send_response(
                    message=self._message_dictionary,
                    status_code=MessageCodeDefinitions.RECEIVED_PACKET_CAPTURE_REQUEST,
                    status_message=RECEIVED_PACKET_CAPTURE_REQUEST,
                )
                if (
                    self.__decode_tcpdump_command()
                    and self.__is_interface_exists_and_up()
                    and self.__create_directory_and_file()
                    and self.__start_capturing_packets_on_interface()
                ):
                    return True
                else:
                    self.__in_progress = False
                    self._response_manager.send_response(
                        message=self._message_dictionary,
                        status_code=MessageCodeDefinitions.ERRORS_IN_PACKET_CAPTURE,
                        status_message=FAILED_TO_CAPTURE_PACKETS,
                    )

            else:
                self.__logger.error("Packet capturing is already in progress")
                self._response_manager.send_response(
                    message=self._message_dictionary,
                    status_code=MessageCodeDefinitions.STARTED_PACKET_CAPTURING,
                    status_message=EXISTING_REQUEST_IS_NOT_COMPLETED,
                )

        except KeyError as key_error:
            self.__logger.error(f"KeyError in capturing packets: {key_error}")
        except Exception as exception:
            self.__logger.error(f"Exception in capturing packets: {exception}")

        return False

    def __decode_tcpdump_command(self):
        """
        Decodes the tcpdump command to extract the network interface and output file.
        Returns:
            bool: True if decoding is successful, False otherwise.
        """
        try:
            self.__tcpdump_command = self._message_dictionary[
                MessageDefinitions.CONTENT_KEY
            ][MessageDefinitions.COMMAND_KEY]

            for index, command in enumerate(self.__tcpdump_command):
                if command == "-i":
                    self.__interface = self.__tcpdump_command[index + 1]
                elif command == "-w":
                    self.__output_file = self.__tcpdump_command[index + 1]

            if not self.__interface:
                self.__logger.error(
                    f"No interface found in the tcpdump command: {self.__tcpdump_command}"
                )
                self._response_manager.send_response(
                    message=self._message_dictionary,
                    status_code=MessageCodeDefinitions.ERRORS_IN_PACKET_CAPTURE,
                    status_message=INTERFACE_NOT_PROVIDED,
                )

            if not self.__output_file:
                self.__logger.error(
                    f"No file found in the tcpdump command: {self.__tcpdump_command}"
                )
                self._response_manager.send_response(
                    message=self._message_dictionary,
                    status_code=MessageCodeDefinitions.ERRORS_IN_PACKET_CAPTURE,
                    status_message=FILE_NOT_FOUND,
                )
                return False

            return True
        except KeyError as key_error:
            self.__logger.error(f"KeyError while decoding tcpdump command: {key_error}")
        except Exception as exception:
            self.__logger.error(f"Error while decoding tcpdump command: {exception}")
        return False

    def __is_interface_exists_and_up(self):
        """
        Checks if the specified network interface is both existing and up.
        Returns:
            bool: True if the interface is existing and up, False otherwise.
        """
        try:
            network_interfaces = psutil.net_if_stats()

            if self.__interface not in network_interfaces:
                self.__logger.error(f"Interface {self.__interface} does not exist.")
                self._response_manager.send_response(
                    message=self._message_dictionary,
                    status_code=MessageCodeDefinitions.ERRORS_IN_PACKET_CAPTURE,
                    status_message=INTERFACE_NOT_FOUND,
                )
                return False

            if not network_interfaces[self.__interface].isup:
                self.__logger.error(
                    f"Interface {self.__interface} is down. Unable to capture packets."
                )
                self._response_manager.send_response(
                    message=self._message_dictionary,
                    status_code=MessageCodeDefinitions.ERRORS_IN_PACKET_CAPTURE,
                    status_message=INTERFACE_DOWN_STATE,
                )
                return False

            return True
        except Exception as exception:
            self.__logger.error(f"An unexpected error occurred: {exception}")

        return False

    def __create_directory_and_file(self):
        """
        Creates the directory and file specified for storing captured packets.
        Returns:
            bool: True if directory and file creation is successful, False otherwise.
        """
        try:
            directory_path = os.path.dirname(self.__output_file)
            file_name = os.path.basename(self.__output_file)

            if not file_name:
                self.__logger.error(
                    f"Filename is not provided in the command: {self.__tcpdump_command}"
                )
                return False

            if not os.path.exists(directory_path):
                os.makedirs(directory_path)

            self.__output_file_path = os.path.join(directory_path, file_name)

            if not os.path.exists(self.__output_file_path):
                open(self.__output_file_path, "w").close()

            return True

        except (FileNotFoundError, IsADirectoryError, PermissionError) as error:
            self.__logger.error(f"Error while creating directory/file: {error}")
        except Exception as exception:
            self.__logger.error(f"An unexpected error occurred: {exception}")

        self._response_manager.send_response(
            message=self._message_dictionary,
            status_code=MessageCodeDefinitions.ERRORS_IN_PACKET_CAPTURE,
            status_message=DIRECTORY_OR_FILE_ERROR,
        )
        return False

    def __capture_packets_thread(self):
        """
        Threaded method for executing the tcpdump command and capturing packets.
        Raises:
            subprocess.CalledProcessError: If there is an error in the subprocess while capturing packets.
            Exception: For other unexpected errors during packet capturing.
        """
        try:
            self._response_manager.send_response(
                message=self._message_dictionary,
                status_code=MessageCodeDefinitions.STARTED_PACKET_CAPTURING,
                status_message=STARTED_PACKET_CAPTURING,
            )
            self.__process = subprocess.Popen(
                self.__tcpdump_command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            stdout, stderr = self.__process.communicate()
            self.__handle_packet_capture_success()

        except (subprocess.CalledProcessError, Exception) as error:
            self.__logger.error(f"Error while capturing packets. {error}")
            self._response_manager.send_response(
                message=self._message_dictionary,
                status_code=MessageCodeDefinitions.ERRORS_IN_PACKET_CAPTURE,
                status_message=FAILED_TO_CAPTURE_PACKETS,
            )

    def __start_capturing_packets_on_interface(self):
        """
        Starts a thread to capture packets on the specified network interface.
        Returns:
            bool: True if the thread starts successfully, False otherwise.
        """
        try:
            capture_thread = threading.Thread(target=self.__capture_packets_thread)
            capture_thread.start()
            return True

        except Exception as exception:
            self.__logger.error(f"Error while capturing packets: {exception}")

        self._response_manager.send_response(
            message=self._message_dictionary,
            status_code=MessageCodeDefinitions.ERRORS_IN_PACKET_CAPTURE,
            status_message=FAILED_TO_CAPTURE_PACKETS,
        )
        return False

    def __stop_capturing_packets(self):
        """
        Stops the packet capture process.
        Returns:
            bool: True if the packet capture process is stopped successfully, False otherwise.
        """
        try:
            if self.__in_progress:
                self._response_manager.send_response(
                    message=self._message_dictionary,
                    status_code=MessageCodeDefinitions.RECEIVED_PACKET_CAPTURE_STOP_REQUEST,
                    status_message=RECEIVED_PACKET_CAPTURE_STOP_REQUEST,
                )
                return self.__stop_capturing()
            else:
                self.__logger.error("No packet capture request is in progress.")
                self._response_manager.send_response(
                    message=self._message_dictionary,
                    status_code=MessageCodeDefinitions.ERRORS_IN_PACKET_CAPTURE,
                    status_message=PACKET_CAPTURE_PROCESS_NOT_FOUND,
                )
            return True
        except Exception as exception:
            self.__logger.error(f"Error while stopping packets capture: {exception}")
            self._response_manager.send_response(
                message=self._message_dictionary,
                status_code=MessageCodeDefinitions.ERRORS_IN_PACKET_CAPTURE,
                status_message=FAILED_TO_CAPTURE_PACKETS,
            )
        return False

    def __stop_capturing(self):
        """
        Stops the packet capture process execution.
        Returns:
            bool: True if the packet capture process is stopped successfully, False otherwise.
        """
        try:
            if self.__process.poll() is None:
                self._response_manager.send_response(
                    message=self._message_dictionary,
                    status_code=MessageCodeDefinitions.STARTED_STOP_PACKET_CAPTURE,
                    status_message=STARTED_STOP_PACKET_CAPTURE,
                )
                self.__process.kill()
                self.__process.wait()
                self._response_manager.send_response(
                    message=self._message_dictionary,
                    status_code=MessageCodeDefinitions.STOPPED_PACKET_CAPTURE,
                    status_message=STOPPED_PACKET_CAPTURE,
                )
                return self.__handle_packet_capture_success()
            else:
                self.__logger.error(
                    f"No packet capture request is in progress. Return code : {self.__process.returncode}"
                )
                self._response_manager.send_response(
                    message=self._message_dictionary,
                    status_code=MessageCodeDefinitions.ERRORS_IN_PACKET_CAPTURE,
                    status_message=PACKET_CAPTURE_PROCESS_NOT_FOUND,
                )
                return False

        except Exception as exception:
            self.__logger.error(f"Error while stopping packets capture: {exception}")
            self._response_manager.send_response(
                message=self._message_dictionary,
                status_code=MessageCodeDefinitions.ERRORS_IN_PACKET_CAPTURE,
                status_message=FAILED_TO_CAPTURE_PACKETS,
            )
        return False

    def __handle_packet_capture_success(self):
        """
        Handles the success of the packet capture process.
        Returns:
            bool: True if handling success is completed, False otherwise.
        """
        try:
            if self.__process.returncode == 0 or self.__process.returncode == -9:
                self.__logger.info("Packet capture completed successfully.")
                self._response_manager.send_response(
                    message=self._message_dictionary,
                    status_code=MessageCodeDefinitions.PACKET_CAPTURE_IS_DONE,
                    status_message=PACKET_CAPTURE_IS_DONE,
                )
                self._data_manager.post_file(
                    message=self._message_dictionary, file_url=self.__output_file_path
                )
            else:
                self.__logger.error(
                    f"Error while capturing packets.{self.__process.returncode}"
                )
                self._response_manager.send_response(
                    message=self._message_dictionary,
                    status_code=MessageCodeDefinitions.ERRORS_IN_PACKET_CAPTURE,
                    status_message=FAILED_TO_CAPTURE_PACKETS,
                )
                return False
            return True
        except Exception as exception:
            self.__logger.error(f"Error while stopping packets capture: {exception}")
            self._response_manager.send_response(
                message=self._message_dictionary,
                status_code=MessageCodeDefinitions.ERRORS_IN_PACKET_CAPTURE,
                status_message=FAILED_TO_CAPTURE_PACKETS,
            )
        finally:
            self.__in_progress = False
        return False