g = open('sample.txt', mode='rt', encoding='utf-8')
g.read(11) #read it by length of the text
g.read() #read remainig all of the text
g.seek(0) #move to beginning of the file
g.readline() #read the line one by one
g.readlines() #read all the text in the file


