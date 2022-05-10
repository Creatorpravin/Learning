import subprocess
"""Used to run shell command in python and get the output"""
cmd = "ip a"

p1 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
out, err = p1.communicate()

print("out: {0}". format(out))
print("error: {0}". format(err))

if p1.returncode == 0:
    print("command : success")
else:
    print("command : failure")


