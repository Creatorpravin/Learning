import shutil

try:
   shutil.move("/home/praveen/tesh.sh","tesh.sh")
except Exception as e:
   print(e)