import os
import tarfile
import time
import shutil
import threading

import CoreCode.logger as Logger

SUCCESS = 0
FAILURE = 1

CUSTOM_SYSLOGFILE_DIRECTORY = '/var/log/UserLog'
USER_SYSLOG_PATH = os.getcwd()   # Custom user syslog path

CUSTOM_COMPRESSED_SYSLOGFILE_PATH = USER_SYSLOG_PATH + os.path.sep + 'Syslog/CompressedSyslogFile'
USER_CONFIGFILE = USER_SYSLOG_PATH + os.path.sep + 'Syslog/UserConfigFile/rsyslog.conf'

SYSTEM_SYSLOG_CONFIGFILE = '/etc/rsyslog.conf'
RSYSLOG_STOP_COMMAND = 'systemctl stop rsyslog syslog.socket'
RSYSLOG_START_COMMAND = 'systemctl start rsyslog syslog.socket'

WRITE_COMPRESS_OPTION = 'w:gz'
TARFILE_EXTENSION_STRING = '.tar.gz'
LOG_EXTENSION_STRING = '.log'  #rename as log_extension_file - Ramesh Done
CONFIGFILE_EXTENSION_STRING = '.conf'

OLD_STRING = 'old'
SYSLOG_STRING = 'Syslog'

DOT_DELIMITER = '.'
UNDERSCORE_CHARACTER = '_'
PATH_SEPERATOR_CHARACTER = os.path.sep

DEFAULT_TIME_INTERVAL = 60    # Unit in seconds - default compression time interval


class SyslogManager:
    """
        Syslog Manager is used to get the log file from the system and Compress the log file for every certain interval of time 
        and send it to the server
    """

    def __init__(self):
        self.__logger = Logger.get_logger(logger_name=__name__)
        self.__logger.info("SyslogManager object initialization start")

        self.__syslog_compression_interval_time = DEFAULT_TIME_INTERVAL 

        self.__compress_syslog_thread_event = threading.Event()

        self.__syslog_start_lock = threading.Lock()
        self.__syslog_stop_lock = threading.Lock()

        self.__compress_syslog_thread = threading.Thread(target=self.__syslog_manager_thread, daemon=True)

        # Check for the presence of dependent file/directory
        if self.__dependency_check() == SUCCESS:    
            self.__compress_syslog_thread.start()

        self.__logger.info("SyslogManager object initialization end")


    def deinitializer(self):
        """
        To deinitialize the SyslogManager threads and events
        Args   - none
        Return - None
        Raises - None
        """
        self.__logger.info("SyslogManager object deinitialization start")

        if not self.__compress_syslog_thread_event.is_set():
            self.__compress_syslog_thread_event.set()
            
        if self.__compress_syslog_thread.is_alive():
            self.__compress_syslog_thread.join()
        
        self.__logger.info("SyslogManager object deinitialization end")


    def update_system_syslog_configfile(self):
        """
        Whenever this function gets called it automaticaly replace the system config file [/etc/rsyslog.comf] with user 
        config file [from {$userpath}/Syslog/UserConfigFile/rsyslog.conf] and renames the old config file as rsyslog_old.conf
        Args   - None
        Return - 0 [SUCCESS] when config file updated successfully
                 1 [FAILURE] when user config file [{userpath}/Syslog/UserConfigFile/rsyslog.conf] not exist
        Raises - None
        """
        return_value = FAILURE
        if os.path.exists(USER_CONFIGFILE):
            self.__stop_syslog()

            self.__rename_existing_configfile()
            system_syslog_config_path = os.path.dirname(SYSTEM_SYSLOG_CONFIGFILE) + PATH_SEPERATOR_CHARACTER
            shutil.copy(USER_CONFIGFILE, system_syslog_config_path)   # Copy src to dst

            self.__start_syslog()

            return_value = SUCCESS
        else:
            self.__logger.error("{} file not exist, Config File not get updated ".format(USER_CONFIGFILE))
        
        return return_value


    def set_syslog_compress_time_interval(self, time_interval=DEFAULT_TIME_INTERVAL):
        """
        It is used to set the time interval at which syslog file get compressed
        The default parameter is time_interval with the default time interval of 60 seconds 
        Args   - time_interval (Unit in seconds)
        Return - None
        Raises - None
        """
        self.__syslog_compression_interval_time = time_interval


    def __dependency_check(self):
        return_value = SUCCESS

        if not os.path.exists(SYSTEM_SYSLOG_CONFIGFILE):   # Check for the presence of /etc/rsyslog.conf file
            self.__logger.error("{} - config file doesn't exist".format(SYSTEM_SYSLOG_CONFIGFILE))
            return_value = FAILURE
        
        if not os.path.exists(CUSTOM_COMPRESSED_SYSLOGFILE_PATH):
            os.makedirs(CUSTOM_COMPRESSED_SYSLOGFILE_PATH + PATH_SEPERATOR_CHARACTER)
        
        return return_value


    def __start_syslog(self):  # check for exception - Anirudhan
        with self.__syslog_start_lock:
            os.system(RSYSLOG_START_COMMAND)


    def __stop_syslog(self):   # check for exception - Anirudhan
        with self.__syslog_stop_lock:
            os.system(RSYSLOG_STOP_COMMAND)


    def __get_syslogfile_list(self, source_directory):
        syslogfile_list = os.listdir(source_directory)

        syslogfile_list_absolute_path = [(source_directory + os.path.sep + syslogfile) 
                                        for syslogfile in syslogfile_list 
                                        if syslogfile.endswith(LOG_EXTENSION_STRING)]
            
        return syslogfile_list_absolute_path


    def __move_system_syslogfile(self):
        syslogfile_list = self.__get_syslogfile_list(CUSTOM_SYSLOGFILE_DIRECTORY)

        for syslogfile in syslogfile_list:
            shutil.move(syslogfile, CUSTOM_COMPRESSED_SYSLOGFILE_PATH)


    def __rename_existing_configfile(self): 
        # Name preparation
        existing_configfile = os.path.basename(SYSTEM_SYSLOG_CONFIGFILE)  # existing_configfile = rsyslog.conf
        existing_configfile_name = existing_configfile.split(DOT_DELIMITER, 1)[0]   
        backup_configfile_name = existing_configfile_name + UNDERSCORE_CHARACTER + OLD_STRING + CONFIGFILE_EXTENSION_STRING
        backup_configfile = os.path.dirname(SYSTEM_SYSLOG_CONFIGFILE) + PATH_SEPERATOR_CHARACTER + backup_configfile_name  # backup_configfile = rsyslog_old.conf

        existing_old_configfile = backup_configfile
        if os.path.exists(existing_old_configfile): 
            os.remove(existing_old_configfile)  # Delete the existing old config file - /etc/rsyslog_old.conf 

        # Rename existing config file to rsyslog_old.conf
        os.rename(SYSTEM_SYSLOG_CONFIGFILE, backup_configfile)


    def __remove_temp_syslogfile(self):
        syslogfile_list = self.__get_syslogfile_list(CUSTOM_COMPRESSED_SYSLOGFILE_PATH)
        
        for syslogfile in syslogfile_list:
            os.remove(syslogfile)


    def __syslog_manager_thread(self):  # rename as syslog_manager_thread - Ramesh done

        while not self.__compress_syslog_thread_event.wait(self.__syslog_compression_interval_time):

            self.__stop_syslog()
            self.__move_system_syslogfile()
            self.__start_syslog()

            syslogfile_list = self.__get_syslogfile_list(CUSTOM_COMPRESSED_SYSLOGFILE_PATH)

            if syslogfile_list == []:
                self.__logger.error("{} - No log files present".format(CUSTOM_COMPRESSED_SYSLOGFILE_PATH))
            else:
                tarfile_name = SYSLOG_STRING + UNDERSCORE_CHARACTER + str(int(time.time())) + TARFILE_EXTENSION_STRING
                tarfile_path = CUSTOM_COMPRESSED_SYSLOGFILE_PATH + PATH_SEPERATOR_CHARACTER + tarfile_name

                with tarfile.open(tarfile_path, WRITE_COMPRESS_OPTION ) as tar:  # give absolute path - Ramesh Done
                    for syslogfile in syslogfile_list:
                        syslogfile_basename = os.path.basename(syslogfile)
                        tar.add(syslogfile, syslogfile_basename)   # add the log file to the compressed tar file

                self.__logger.info("{} - compressed successfully".format(tarfile_name))        
                self.__remove_temp_syslogfile()
