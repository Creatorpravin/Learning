import os
import subprocess

APT_GET_PREFIX = "apt-get"
APT_GET_UPDATE_SUFFIX = "update"
APT_GET_INSTALL_SUFFIX = "install"
APT_GET_OPTION = "-y"
APT_GET_INSTALL_ALLOW_DOWNGRADE = "--allow-downgrades"
DEBIAN_FRONTEND_KEY = "DEBIAN_FRONTEND"
DEBIAN_FRONTEND_VALUE = "noninteractive"

SYSTEMCTL_COMMAND_PREFIX = "systemctl"
SYSTEMCTL_STOP_OPTION = "stop"
SYSTEMCTL_START_OPTION = "start"
SYSTEMCTL_DISABLE_OPTION = "disable"
SYSTEMCTL_ENABLE_OPTION = "enable"
SYSTEMCTL_RESTART_OPTION = "restart"

COLON_CHARACTER = ":"

CHOWN_COMMAND_PREFIX = "chown"
CHOWN_RECURSIVE_OPTION = "-R"

PATH_SEPERATOR_CHARACTER = os.path.sep
SPACE_CHARACTER = " "
EQUAL_CHARACTER = "="


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

            if result.returncode != 0:
                return False

        except Exception as exception:
            logger_object.error(exception)
            return False

        return True
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


def update_package_list(logger_object):
    """
    This funtion will update the package information for specified repositories under
    /etc/apt/source.list and /etc/apt/source.list.d/*
    Args:
        logger_object - object of type Logger which is used by this function to log messages
    """

    # Apt update command format = apt-get update
    apt_get_update_command = APT_GET_PREFIX + SPACE_CHARACTER + APT_GET_OPTION + SPACE_CHARACTER + APT_GET_UPDATE_SUFFIX

    if execute_linux_command(command=apt_get_update_command, logger_object=logger_object) != True:
        return False

    return True


def install_package(package_name, target_version, logger_object):
    """
    This funtion  will install the package specified by package name
    Args:
        package_name - package to be installed
        target_version - package version to be installed
        logger_object - object of type Logger which is used by this function to log messages
    """

    # Apt install command format = DEBIAN_FRONTEND=noninteractive apt-get install -y <packagename>
    apt_get_install_command = DEBIAN_FRONTEND_KEY + EQUAL_CHARACTER + DEBIAN_FRONTEND_VALUE + SPACE_CHARACTER + APT_GET_PREFIX \
                                        + SPACE_CHARACTER + APT_GET_INSTALL_SUFFIX + SPACE_CHARACTER + APT_GET_OPTION \
                                        + SPACE_CHARACTER + APT_GET_INSTALL_ALLOW_DOWNGRADE+ SPACE_CHARACTER + package_name
    if target_version != "":
        apt_get_install_command = apt_get_install_command + EQUAL_CHARACTER + target_version

    if execute_linux_command(command=apt_get_install_command, logger_object=logger_object) != True:
        return False

    return True
