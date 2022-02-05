from math import factorial
a = {len(str(factorial(x)))for x in range(20)}
print(a)#set comprehension