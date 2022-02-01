d = {"brand":"ford",
    "model":"mustang",
    "year":2015}

d["year"]=2016 #Update the value
d["engine"] = "petrol" #Add the new value

for value in d:
    print(value,d[value]) #Print by it's key value

