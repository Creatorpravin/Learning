with open('sample.txt', 'a') as file: #write the file
    file.writelines('\n then this is next')
#automatically enter and exit
with open('sample.txt', 'r') as file:
    print(file.readlines()) #read the file
