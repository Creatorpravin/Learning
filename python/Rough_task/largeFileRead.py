#import time
import pandas as pd
from collections import namedtuple
lines = []
#start = time.time()

#Title of row
writer = pd.ExcelWriter('log.xlsx')
row = 0
Line = namedtuple('Line','DateTime Status FileName LineNo Modules FunctionName Message')
count = 0

with open("/home/praveen/CPEApplication_Chennai.log") as file:
    for line in file:
        #print(line)    
        li = line.split("|")
        #print(len(li))
        if len(li) == 7 :            
          lines.append(Line(*li))          
        count = count + 1
        #print("+++++++++++++++++", count)
        #Describe the count of lines (Column)
        if count == 50:
            break

df = pd.DataFrame(lines)
df.to_excel("log.xlsx", index=False)
print("No of lines converted : ", count)



#df = pd.concat(lines)
#df.to_csv("log.csv",index=False)

#Convert dataframe to excel
#csv_read = pd.read_csv("log.csv")

#excel = pd.ExcelWriter("log.xlsx")
#csv_read.to_excel(excel, index=False)
#excel.save()
#end = time.time()
#print("Execution time in seconds: ", (end-start))