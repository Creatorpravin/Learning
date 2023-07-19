import pandas as pd

a = [1, 7, 2]
#If we use defined lables as int means not work with access of index values
myvar = pd.Series(a, index= [5, "y", "z"])

print(myvar)
print(myvar["y"])
print(myvar[5]) #can access using index and its defined lables



calories = {"day1": 420, "day2": 380, "day3": 390}
#Create a Series using only data from "day1" and "day2
myvar1 = pd.Series(calories, index = ["day1", "day2"])
print(myvar1)