# python3 files.py sample.txt
"""open a file lines in iteration"""
import sys
f = open(sys.argv[1], mode='rt', encoding='utf-8')
for line in f:
    #print(line) #print it line by line
    sys.stdout.write(line)#print without white space
f.close()


