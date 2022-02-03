t = ("norway",4.56,3) #tuple with multi data type
print(t[0]) #Access the values in tuples
for item in t:
    print(item) #iterate and print single values of tuple
print(t + (563,56.2)) #add values with tuples
print(t * 3) #Multiply the tuples
a = (56,) #single element tuples
print (type(a))

def minMax(items): #print max and min value in function
    return min(items), max(items)

low, upper = minMax([45,2,69,589,562]) #get the return value in separate variables
print(low)
print(upper)

(x, (y,(z,e))) = (1, (2,(3,4))) #assing values for each tuples
print(x,e)

r = 'jelly'
p = 'bean'
r, p = p, r #swaping the values
print (p, r)
#using in and not in operator to check true or false
print(561 in tuple([561,568,59,6])) 
print(561 not in tuple([561,568,59,6]))