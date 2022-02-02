count = 0
def showCount():
    print(count)
def setCount(c):
    global count #use global to access global
    count = c
    print(c)

setCount(5)
showCount()
