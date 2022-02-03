
print(len("sgdfjasdkfhajdf")) #find length
print("new"+"found"+"land") #concat the string values

colors = ';'.join(['red', 'blue', 'orange', 'yellow'])
print(colors)
print(colors.split(';'))

#partition
print("unforgetable".partition('forget'))#('un', 'forget', 'able')

#format String
print(('The age of {0} is {1}').format('jim',32))
#f string
print(f'The value is {4*3} and the colors are {colors.split(";")}')
