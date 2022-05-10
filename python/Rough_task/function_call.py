import function_list

number = ["hello", "yes", "there", "fine"]
list1 = []

status, lister = function_list.list(number=number,list=list1)

print(str(status) + "\t"+ str(lister))


