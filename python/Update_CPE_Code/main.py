import subprocess
import json
import os
from sys import stderr


def installation(installation_json):

    if os.path.exists(installation_json) is True:
        with open(file=installation_json, mode="r") as install_json:
            json_data = json.loads(install_json.read())
            key_list = [i for i in json_data]
            for i in key_list:
                if (len(json_data[i])) > 1:
                    for j in range(len(json_data[i])):
                        #print(key_list[0])
                        if (len(json_data[i])) > 3:
                            print(json_data[i][j]["package"])
                        else:
                            print(json_data[i][j]["package"])

                else:
                    print(json_data[i])


def shell_execution(shell_file_name):
    execution_command = "./"+shell_file_name
    print(execution_command)
    execution = subprocess.Popen(execution_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    result_out = execution.communicate()
    print(result_out)





if __name__ == "__main__":
    installation("installation.json")
    shell_execution("aptupdate")
