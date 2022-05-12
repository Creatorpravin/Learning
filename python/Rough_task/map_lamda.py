
# Add two lists using map and lambda
  
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
  
# result = map(lambda x, y: x + y, numbers1, numbers2)
# print(list(result))

list1 = map(lambda x: x + 5, numbers1)

print(list(list1))