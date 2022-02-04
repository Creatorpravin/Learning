def gen123(): #its also define like a noraml function
    print('i am yield 1')
    yield 1
    print('i am yield 2')
    yield 2
    print('i am yield 3')
    yield 3
    return print("This is the end")
g = gen123() #assign function to varaible then only access
print(g)#not like this
print(next(g)) #access the yield one y one by next keyword
print(next(g))
print(next(g))

#use loop
for i in gen123():
    print(i)
