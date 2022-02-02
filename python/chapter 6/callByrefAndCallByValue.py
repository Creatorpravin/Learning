#call by value
a = 5
b = a
a = 6
print(b)#5
print(a)#6
#call by referance
x = [1,56,69]
y = x
y[1] = 60
print(y)#[1, 60, 69]
print(x)#[1, 60, 69]


