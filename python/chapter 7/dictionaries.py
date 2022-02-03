
#convert this to dictionary
namesAndAges = [('alice',32),('pravin',23)]
d = dict(namesAndAges)
print(d)
#copy
f = d.copy()
print(f)
#another method
g = dict(d)
print(g)
cars = {"brand":"bugati",
       "model":"veyron"}
cars2 = {"year":2019,
         "engine":"petrol"}
#Update or merge
cars.update(cars2)
cars.update({"abs":"cornering abs"})
cars["cooling"] = "liquid"
print(cars)
#iteration
for keys in cars:
    print(f'{keys} => {cars[keys]}')
for values in cars.values():#print only the values
    print(values)
#delete
del cars['engine']
print(cars)