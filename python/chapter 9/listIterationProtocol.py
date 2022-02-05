iterable = ['spring','summer','autumn','winter']
iterator = iter(iterable) #iter the values in list
print(next(iterator)) #iter one by one values in list
print(next(iterator))
print(next(iterator))
print(next(iterator))
#add all the values in list using sum funciton
a = [1,2,2,3,6,589,9]
print(sum)
#use exception handling
def first(iterables):
    iterator=iter(iterables)
    try:
        return next(iterator) #return only the first value in list
    except StopIteration:
        raise ValueError("iterable is empty")

print(first(['1st','2nd','3rd']))
print(first([]))
a = [1,2,2,3,6,589,9]
print(sum)