import os
import glob
import shutil

DIRECTORY = '/home/ragu/FactoryReset'
files = os.listdir(DIRECTORY)
for f in files:
    if os.path.isdir(DIRECTORY +'/'+ str(f)): #check that is a dir
        print(f)
        shutil.rmtree(DIRECTORY +'/'+ str(f)) 
    #elif os.path.isfile(DIRECTORY + "/" + str(f)):
     #   os.remove(DIRECTORY + '/' + str(f))

# os.rmdir('/home/ragu/Definitions')
#shutil.rmtree('/home/ragu/FactoryReset') #hard delete the folder

#list( map( os.unlink, (os.path.join( '/home/ragu/Definitions',f) for f in os.listdir('/home/ragu/Definitions')) ) ) #hard delete all files in a dir  
