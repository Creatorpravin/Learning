import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45],
  "time" : [1,2,3]
}
df = pd.DataFrame(data)
df1 = pd.DataFrame(data, index=["Day1", "Day2", "Day3"]) # Length of all values in list must be same

print(df["calories"])
print(df.loc[0]) # Use loc to access by index
print(df.loc[[0, 2]])

print(df1)