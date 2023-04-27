def my_function(x):
    if x == 0:
        return 0
    else:
        return x + my_function(x-1)

print(my_function(5))