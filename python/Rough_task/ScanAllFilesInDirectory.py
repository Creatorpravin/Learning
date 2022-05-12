import os
import glob

path = "/home/praveen/CPE"
path01 = "/home/praveen/CPE/**/*.py"
count = 0
count01 = 0
file_list=[]
# for root, directories, files in os.walk(path):
#     for f in files:
#         if(f.endswith(".py")):
#             count = count + 1
#             file_list.append(f"{root}/{f}")

# print(count, file_list)
# file_list=[]
#file_list = [f"{root}/{file}" for root, directories, file in os.walk(path) if file.endswith(".sh")]
# #[f"/home/nithin/Desktop/_python/{file}" for file in os.listdir("./") if file.endswith(".ipynb")]

for root, directories, file in os.walk(path):
      
    file_list  += [f"{root}/{f}" for f in file if f.endswith(".py")]
#         # file_list.extend(li)
#         # if(file.endswith(".py")):
#         #     count = count + 1
#         #     print(os.path.join(root,file))
print(file_list)
for f in file_list:
    count01 += 1
print(count01)
#print(count(file_list))

# file = glob.iglob(path01, recursive=True)
# for i,f in enumerate(file,1):
#     print(f)

# print("glob "+str(i))