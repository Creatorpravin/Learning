from sys import platform
import re
import os

import helper_functions as HF

class PythonDependencyInstaller():
    def __init__(self):
        print("[+] Python Dependency Installer Initializer Starts")
        
        windows_regex_pattern = re.compile("^win")
        linux_regex_pattern = re.compile("^lin")
        mac_regex_pattern = re.compile("^mac")

        if windows_regex_pattern.match(platform):
            print("[+] Windows OS found")
            python_dep_installation_command = "pip3 install -r " + os.getcwd() + os.path.sep + "requirements.txt"

        elif linux_regex_pattern.match(platform):
            print("[+] Linux OS found")
            python_dep_installation_command = "pip3 install -r requirements.txt"

        elif mac_regex_pattern.match(platform):
            print("[+] MAC OS found")
            python_dep_installation_command = "pip3 install -r requirements.txt"

        else:
            print("[-] Unidentified OS")
            raise "Unidentified OS"

        output, status = HF.execute_command(python_dep_installation_command)

        if status == True:
            print("[+] {}".format(output))
        else:
            print("[-] {}".format(output))
            raise "Failed to execute Status"
        
        print("[+] Python Dependency Installer Initializer Ends")
