x = 1

def f():
    global x
    
    x = x + 1
    return x

print(f())
print(x)