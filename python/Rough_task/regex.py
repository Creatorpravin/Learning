import re

regex = r'[^\w]'
x = "[ ' 1 2 ' ,   ' 9 8 ' ] [ ' 1 ' ,   ' 2 ' ,   ' 3 ' ,   ' 5 ' ,   ' 8 ' ,   ' 9 ' ] [ ' 1 1 ' ]"
# print(type(x))
# d = x.split('[')
# print(d)
# res = json.loads(x)
# for r in res:
#     print(r)
#print(r for res )
print(re.sub(r'[^\w]', ' ', x))


