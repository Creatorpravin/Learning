import subprocess
"""Used to run shell command in python and get the output"""
cmd = "ip a"

p1 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
out, err = p1.communicate()



if p1.returncode == 0: #used to get return value in shell 'echo $?' if == 0 means success if == other than 0 means fail 
    print("out: {0}". format(out))
    print("command : success")
else:
    print("error: {0}". format(err))
    print("command : failure")


