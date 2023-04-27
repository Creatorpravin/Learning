import os

if "/home/praveen/Learning/Networking" in "/home/praveen/Learning/Networking-1":
    print("same") 
else:
    print("not same")
 
a = os.listdir("/home/praveen/Learning/Networking")

directory = "/home/praveen/Learning/Networking-1"
for i in a:
    # print(i)
    if i in os.listdir(directory):
        print(i)
        
        print(os.remove(directory+os.path.sep+i))