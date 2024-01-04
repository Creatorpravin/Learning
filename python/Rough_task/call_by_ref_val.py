
def foo(a):
    a[0] = "Nothing"
    print("Inside Function : ",a)
    print(id(a))
bar = ['Hi', 'how', 'are', 'you', 'doing']
foo(bar)
print("Outside Function : ",bar)
print(id(bar))


def foo(b):
    b = "Nothing"
    print("Inside Function : ",b)
    print(id(b))
# Driver' code
car = "Anything"
foo(bar)
print("outside Function : ",car)
print(id(car))