#Have the for loop to calculate a sum at every 5 element until it reaches the end of the data set.
J=[1,2,3,4,5,6,7,8,9,10,96,97,98,99,100]
res=[]

for i in range(0,len(J),5):   #range(start,end,increment by)
    res.append(sum(J[i:i+5])) #sum(listOfRange(start,end))

print(res) #[15, 40, 490]