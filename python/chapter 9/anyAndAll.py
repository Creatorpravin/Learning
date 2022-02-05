print(any([False,False,True]))
print(all([False,False,True]))
#any
from filterigComprehension import isPrime #import isprime module and use it
print(any(isPrime(x)for x in range (1328,1360)))
#all
#check all the names are starts with capital
print(all(name == name.title()for name in ['London','Paris','Dubai','India']))
