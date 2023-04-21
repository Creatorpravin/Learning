# Find the first python developer from below dictionary using while loop

list1 = [
    {"firstName": 'Mark', "lastName": 'G.', "country": 'Scotland',
        "continent": 'Europe', "age": 22, "language": 'JavaScript'},
    {"firstName": 'Victoria', "lastName": 'T.', "country": 'Puerto Rico',
        "continent": 'Americas', "age": 30, "language": 'Python'},
    {"firstName": 'Emma', "lastName": 'B.', "country": 'Norway',
        "continent": 'Europe', "age": 19, "language": 'Clojure'}
]

list2 = [
  { "first_name": "Kseniya", "last_name": "T.", "country": "Belarus", "continent": "Europe", "age": 29, "language": "JavaScript" },
  { "first_name": "Amar", "last_name": "V.", "country": "Bosnia and Herzegovina", "continent": "Europe", "age": 32, "language": "Ruby" }
]

def get_first_python(users):
    i = 0
    state = False
    iteration = len(users) - 1
    while i <= iteration:
        dict_var = users[i]        
        if dict_var["language"] == "Python":            
            #print(dict_var["firstName"], dict_var["country"])
            state = True            
            result = dict_var["firstName"]
            result = result + ", "+dict_var["country"]
            break
            #return result
        i = i + 1    
    if state:
        return result 
    else:
        return "There will be no Python developers"
            
        

print(get_first_python(list1))