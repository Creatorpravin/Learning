import subprocess
import time

def ping_google(command):
    ping_out = subprocess.run(command, shell=True, universal_newlines=True)

    if ping_out.returncode == 0:
        with open('google.txt', 'a') as f:
            f.write(ping_out.stdout)
    else:
        with open('google.txt', 'a') as f:
            f.write("Fail to execute ping command")



ping_google("ping -i1 8.8.8.8 > google.txt ")

 