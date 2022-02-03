p = {6,89,62,98538,456}
print(type(p))
#it remove duplicate items
f = {1,1,1,2,2,3,3,3,4,4,4,5,5,5,6,6,6}
print(f) 
#add element in set
f.add(12)
f.update([12,23,56,69])
#iterate the elements in set
for x in f:
    print(x)
#remove
f.remove(69)
f.discard(23)
print(f)