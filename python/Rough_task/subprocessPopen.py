import subprocess
"""Used to run shell command in python and get the output"""
cmd0 = "ip a"
cmd = "ip a"

p1 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
out, err = p1.communicate()



if p1.returncode == 0: #used to get return value in shell 'echo $?' if == 0 means success if == other than 0 means fail 
    print("out: {0}". format(out))
    print("command : success")
else:
    print("error: {0}". format(err))
    print("command : failure")


p2 = subprocess.run("ip a", capture_output=True, shell=True, universal_newlines=True)

dic2 = dict()
dic2["test"] = (p2.stdout)
print(p2.returncode)