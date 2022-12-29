import shutil

source = "/home/praveen/test/yes"
destination = "/home/praveen/test/telegraf"

resu = shutil.move( source , destination )
print(resu)