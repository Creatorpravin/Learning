import subprocess
import re
import os
# myFile = open("/home/praveen/replace/data", "w")
# writenFile = open("/home/praveen/data",)
# myFile.write(writenFile)

# with open("/home/praveen/replace/data","r+") as f:
#     writenFile = open("/home/praveen/data","w")
#     file_test = writenFile.read()
#     f.write(file_test)
#     f.close()

if os.path.isdir("/home/praveen/replace"):
    remove_command = "sudo rm -r /home/praveen/replace"
    execution = subprocess.Popen(remove_command, shell=True,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)#print("dir")

if os.path.isfile("/home/praveen/data"):
    os.remove("/home/praveen/data")
    #print("file")

a = "/home/praveen/replace"
b = "data"

file_loc = os.path.join(a,b)
print(file_loc)