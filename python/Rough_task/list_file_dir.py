import os

FILE_PATH = "/home/praveen/Learning/python/Rough_task/image"
PDF_SUFIX = ".pdf"

for filename in os.listdir(FILE_PATH):
    if PDF_SUFIX in filename:
        filepath = FILE_PATH + os.path.sep + filename
        print(filename)      

FILE_STUFFS = os.listdir(FILE_PATH)

if "test.p" in FILE_STUFFS:
    print(True)
else:
    print(False)

# Check the file exist exists or not
if os.path.isfile(path=FILE_PATH + "/Employee_detail.pdf") == True:
    print(True)
