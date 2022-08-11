from logging import exception
import re
import subprocess
import json
import os
from sys import stderr
import shutil


def main(installation_json):

    if os.path.exists(installation_json) is True:
        with open(file=installation_json, mode="r") as install_json:
            json_data = json.loads(install_json.read())
            key_list = [i for i in json_data]
            for i in key_list:
                if (len(json_data[i])) > 1:
                    for j in range(len(json_data[i])):
                        # print(key_list[0])
                        if (len(json_data[i])) > 3:
                            return_value = shell_execution(json_data[i][j]["package"])
                            if return_value==True:
                                print(json_data[i][j]["package"]+" Installed successfully")
                            else:
                                print(json_data[i][j]["package"]+" Installation failed")
                        else:
                            print(json_data[i][j]["file_name"])

                else:
                    print(json_data[i])


def shell_execution(shell_file_name):
    print(shell_file_name+" is installing")
    execution_command = "./"+shell_file_name
    print(execution_command)
    execution = subprocess.Popen(execution_command, shell=True,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    result_out, result_err = execution.communicate()

    if execution.returncode == 0:
        print("out: {0}". format(result_out))
        print(shell_file_name+" install successfully")
    else:
        print("error: {0}". format(result_err))
        print(shell_file_name+" installation failed")
        return False

    return True


def move_files_in_directory(source_directory_path, destination_directory_path):

    if os.path.isdir(source_directory_path) != True:
        print("{} path is not a valid directory".format(source_directory_path))
        return False

    if os.path.isdir(destination_directory_path) != True:
        print("{} path is not a valid directory".format(
            destination_directory_path))
        return False

    try:
        shutil.move(source_directory_path, destination_directory_path)

    except Exception as exeception:
        print(exception)
        return False


if __name__ == "__main__":
    main("installation.json")

