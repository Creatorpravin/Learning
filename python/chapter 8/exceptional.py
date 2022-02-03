digitMap={
    'zero' : '0',
    'one' : '1',
    'two' : '2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
}
def convert(s):
  try:
    number = ''
    f = list(s.split(" "))#convert string to list
    for token in f:
        number += digitMap[token]#pass the value and get the int
    x=int(number)
  except KeyError:
       print("Conversion failed")
       x=-1
  except TypeError:
       print("Conversion failed")
       x=-1
  except AttributeError:
       print("Conversion failed")
       x=-1
  return x
 
#print(convert("one two"))
