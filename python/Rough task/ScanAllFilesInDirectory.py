import os

path = "/home/praveen/CPE"

count = 0
for root, directories, file in os.walk(path):
    for file in file:
        if(file.endswith(".py")):
            count = count + 1
            print(os.path.join(root,file))

print(count)