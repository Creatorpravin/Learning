class Flight:
    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError("No arline code")
        if not number[:2].isupper():
            raise ValueError("Invalid airline code")
        if not (number[2:].isdigit() and int(number[2:])<= 9999):
            raise ValueError("Invalid rout number")
        self._number = number
    
    def number(self):
        return print(self._number)
#create two diffrent instance object
f = Flight("AI474")
f.number()
f1 = Flight("AI473")
f1.number()

