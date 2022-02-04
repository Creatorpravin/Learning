#ERR
class Flight:
    def __init__(self, number, registration, model,numRows,numSeatsPerRow):
        if not number[:2].isalpha():
            raise ValueError("No arline code")
        if not number[:2].isupper():
            raise ValueError("Invalid airline code")
        if not (number[2:].isdigit() and int(number[2:])<= 9999):
            raise ValueError("Invalid rout number")
        self._number = number
        self._registration = registration
        self._model = model
        self._numRows = numRows
        self._numSeatsPerRow = numSeatsPerRow
        rows, seats = numRows , numSeatsPerRow
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return print(self._number)
    def aircraftModel(self):
        return print(self._model)
    def registration(self):
        return print(self._registration)
    def model(self):
        return print(self._model)
    def seatingPlan(self):
        return print((range(1, self._numRows),"ABCDEFGHJK"[:self._numSeatsPerRow]))
    

f = Flight("GF474","G9474","Airbus 320", 22,6)
f.aircraftModel()
print(f._seating())