import os

FILE_PATH = "/home/praveen/Learning/python/Rough_task/image"
PDF_SUFIX = ".pdf"

for filename in os.listdir(FILE_PATH):
    if PDF_SUFIX in filename:
        filepath = FILE_PATH + os.path.sep + filename
        print(filename)      
