import os

if os.path.exists(path="/home/praveen/Learning"):
    print("Exists")
else:
    print("Not Exists")

if len(os.listdir(path="/home/praveen/55")) != False:
    print("Not Empty")
else:
    print("Empty")

print(len(os.listdir(path="/home/praveen/55")))