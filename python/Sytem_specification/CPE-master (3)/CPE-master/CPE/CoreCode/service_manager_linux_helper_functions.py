import os
import subprocess

SYSTEMCTL_COMMAND_PREFIX = "systemctl"
SYSTEMCTL_STOP_OPTION = "stop"
SYSTEMCTL_START_OPTION = "start"
SYSTEMCTL_DISABLE_OPTION = "disable"
SYSTEMCTL_ENABLE_OPTION = "enable"
SYSTEMCTL_RESTART_OPTION = "restart"

COLON_CHARACTER = ":"

CHOWN_COMMAND_PREFIX = "chown"
CHOWN_RECURSIVE_OPTION = "-R"

REBOOT_COMMAND = "reboot"

PATH_SEPERATOR_CHARACTER = os.path.sep
SPACE_CHARACTER = " "

PID_OF_COMMAND = "pidof"

def execute_linux_command(command, logger_object):
    """
    This funtion gets and executes the linux commands
    Args:
        command - an object of type string which is command need to execute on linux
        logger_object - an object of type Logger which is used by this function to log messages
    """
    try:
        execution_status = subprocess.run(command, shell=True, capture_output=True, text=True)
        logger_object.info(execution_status.stdout)
        logger_object.debug(execution_status.stderr)

        if execution_status.returncode != 0:
            return False

    except Exception as exception:
        logger_object.error(exception)
        return False

    return True


def execute_script(filepath, logger_object):
    """
    This funtion gets and executes the linux shell script
    Args:
        filepath - file path of linux shell script to be executed
        logger_object - an object of type Logger which is used by this function to log messages
    """
    if os.path.exists(filepath):
        try:
            result = subprocess.run(filepath, capture_output=True)

            logger_object.info(result.stdout)
            logger_object.debug(result.stderr)

            logger_object.info("{} file executed successfully".format(filepath))
            return True
        except Exception as exception:
            logger_object.error(exception)
            return False

    else:
        logger_object.error("{} file does not exist".format(filepath))
        return False


def start_system_service(service_name, logger_object):
    """
    This funtion get the name of system service and starts the system service
    Args:
        service_name - object of type string, it represent the name of the system service
        logger_object - an object of type Logger which is used by this function to log messages
    """
    start_system_service_command = SYSTEMCTL_COMMAND_PREFIX + SPACE_CHARACTER \
                                        + SYSTEMCTL_START_OPTION + SPACE_CHARACTER + service_name

    if execute_linux_command(command=start_system_service_command, logger_object=logger_object) != True:
        return False

    return True


def stop_system_service(service_name, logger_object):
    """
    This funtion get the name of system service and stops the system service
    Args:
        service_name - object of type string, it represent the name of the system service
        logger_object - an object of type Logger which is used by this function to log messages
    """
    stop_system_service_command = SYSTEMCTL_COMMAND_PREFIX + SPACE_CHARACTER \
                                        + SYSTEMCTL_STOP_OPTION + SPACE_CHARACTER + service_name

    if execute_linux_command(command=stop_system_service_command, logger_object=logger_object) != True:
        return False

    return True


def enable_system_service(service_name, logger_object):
    """
    This funtion get the name of system service and enables the system service
    Args:
        service_name - object of type string, it represent the name of the system service
        logger_object - an object of type Logger which is used by this function to log messages
    """
    enable_system_service_command = SYSTEMCTL_COMMAND_PREFIX + SPACE_CHARACTER \
                                        + SYSTEMCTL_ENABLE_OPTION + SPACE_CHARACTER + service_name

    if execute_linux_command(command=enable_system_service_command, logger_object=logger_object) != True:
        return False

    return True


def disable_system_service(service_name, logger_object):
    """
    This funtion get the name of system service and disables the system service
    Args:
        service_name - object of type string, it represent the name of the system service
        logger_object - an object of type Logger which is used by this function to log messages
    """
    disable_system_service_command = SYSTEMCTL_COMMAND_PREFIX + SPACE_CHARACTER \
                                        + SYSTEMCTL_DISABLE_OPTION + SPACE_CHARACTER + service_name

    if execute_linux_command(command=disable_system_service_command, logger_object=logger_object) != True:
        return False

    return True


def restart_system_service(service_name, logger_object):
    """
    This funtion get the name of system service and restarts the system service
    Args:
        service_name - object of type string, it represent the name of the system service
        logger_object - object of type Logger which is used by this function to log messages
    """
    restart_system_service_command = SYSTEMCTL_COMMAND_PREFIX + SPACE_CHARACTER \
                                        + SYSTEMCTL_RESTART_OPTION + SPACE_CHARACTER + service_name

    if execute_linux_command(command=restart_system_service_command, logger_object=logger_object) != True:
        return False

    return True

def change_directory_and_its_files_ownership(user_name, group_name, directory_path, logger_object):
    """
    This funtion get the user name, group name and destination path of directory and changes the ownership of the directory and its files
    Args:
        user_name - object of type string, it represent the user name
        group_name - object of type string, it represent the group name
        directory_path - bject of type string, it represent the directory to which we want to change ownership
        logger_object - object of type Logger which is used by this function to log messages
    """

    change_directory_ownership_command = CHOWN_COMMAND_PREFIX+ SPACE_CHARACTER + CHOWN_RECURSIVE_OPTION + \
                                              SPACE_CHARACTER + user_name + COLON_CHARACTER + group_name + \
                                              SPACE_CHARACTER + directory_path

    if execute_linux_command(command=change_directory_ownership_command, logger_object=logger_object) != True:
        return False

    return True

def change_file_ownership(user_name, group_name, file_path, logger_object):
    """
    This funtion get the user name, group name and destination file path and changes the ownership of the file
    Args:
        user_name - object of type string, it represent the user name
        group_name - object of type string, it represent the group name
        file_path - object of type string, it represent the file to which we want to change ownership
        logger_object - object of type Logger which is used by this function to log messages
    """

    change_file_ownership_command = CHOWN_COMMAND_PREFIX+ SPACE_CHARACTER + \
                                        user_name + COLON_CHARACTER + group_name + \
                                        SPACE_CHARACTER + file_path

    if execute_linux_command(command=change_file_ownership_command, logger_object=logger_object) != True:
        return False

    return True


def get_pid(process_name, logger_object):
    """
    This funtion get the process name and return the PID number based on the process name
    Args:
        process_name - object of type string, it represent the process name
        logger_object - object of type Logger which is used by this function to log messages
    Return:
        Returns PID values
        type - list of integer values
    """
    pid_list = []

    try:
        process_id_string = subprocess.check_output(args=[PID_OF_COMMAND, process_name])
        process_id_string_list = process_id_string.split()

        for process_id in process_id_string_list:
            process_id_integer = int(process_id.decode("utf-8"))
            pid_list.append(process_id_integer)
    except Exception as exceptions:
        return []

    return pid_list


def reboot_system(logger_object):
    """
    This funtion initiates the reboot sequence of the system
    Args:
        logger_object - an object of type Logger which is used by this function to log messages
    """

    logger_object.info("ChiefNET - Reboot Sequence Initiated")

    if execute_linux_command(command=REBOOT_COMMAND, logger_object=logger_object) is False:
        return False

    return True