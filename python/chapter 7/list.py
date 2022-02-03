r = [1,2,3,6,5,8,6,9,5,9]
print(r[-1])#access the last element by b-1
print(r[-2])#access the before of last element by b -2
#slicing
print(r[1:3])
#add value
a = [[1,2],[2,3]]
a[1].append(5)
print(a)
#mutate list
b=[56,65,98]
d = b * 4
print(d)
#initialize list with constan value
one = [1] * 9
print(one)
#index method
w = "The quick fox jump over the lazy dog".split()
print(w.index('fox'))#to find the index of fox
print(w.count('the'))
print('the' in w)
#delete
del w[0]
w.remove('the')
print(w)
#insert
w.insert(0, 'The')
print(' '.join(w))
print(w)
#concat
p=[1,2,3,5]
r=[6,7,8,9]
print(p+r)#not affect original list
p.extend(r)#changes happen in original array
print(p)
#reverse
p.reverse()
print(p)
#sort
f = [5,2,4,3,6,9,10]
f.sort()
print(f)
f.sort(reverse=True)
print(f)#sort and reverse