def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        a , b = b , a + b

for x in lucas():
    print(x)
    