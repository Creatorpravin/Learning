#read the lenth of the each words
def wordsPerLine(flo): #get the text file
    return [len(line.split()) for line in flo.readlines()] #split the file and get the length then make it as list
with open("sample.txt", mode='rt',encoding='utf-8') as realFile:
    wpl = wordsPerLine(realFile) #read the text file and pass to the function
print(wpl)