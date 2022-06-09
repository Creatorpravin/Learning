import subprocess

p1 = subprocess.Popen('cat nmap.json', shell=True,     stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
json_out, json_err = p1.communicate()

if p1.returncode == 0: #used to get return value in shell 'echo $?' if == 0 means success if == other than 0 means fail 
    print("out: {0}". format(json_out))
    print("command : success")
else:
    print("error: {0}". format(json_err))
    print("command : failure")