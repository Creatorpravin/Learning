h = open('sample.txt', mode='at',encoding='utf-8') # a t = "append text"
#append the text
h.writelines(
   ['Son of man, \n',
    'You cannot say, or guess, \n',
    'for you know only,\n'])
h.close()
