from math import sqrt
def isPrime(x):
    if x<2:
        return False
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0:
            return False
    return True
print([x for x in range(101) if isPrime(x)])