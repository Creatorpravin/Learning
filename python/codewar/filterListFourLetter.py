#Make a program that filters a list of strings and returns a list with only your friends name in it.
#If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
def friend(x):
    lenth = len(x) - 1
    i = 0
    result = list()
    while i <= lenth:
        if len(x[i]) == 4:
            result.append(x[i])
        i = i + 1
    return result

print(friend(["Ryan", "Kieran", "Mark",]))

# second method
# def friend(x):
#     return [f for f in x if len(f) == 4]