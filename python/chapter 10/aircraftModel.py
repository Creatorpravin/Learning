class Aircraft:
    def __init__(self, registration, model,numRows,numSeatsPerRow):
        self._registration = registration
        self._model = model
        self._numRows = numRows
        self._numSeatsPerRow = numSeatsPerRow
    def registration(self):
        return print(self._registration)
    def model(self):
        return print(self._model)
    def seatingPlan(self):
        return print((range(1, self._numRows),"ABCDEFGHJK"[:self._numSeatsPerRow]))

a = Aircraft("G9474","Airbus 320", 22,6)
a.registration()
a.model()
a.seatingPlan()
# Output
# G9474
# Airbus 320
# (range(1, 22), 'ABCDEF')