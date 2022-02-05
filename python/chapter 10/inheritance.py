# Base class1
class Mother:
    mothername = ""
    def mother(self):
        print(self.mothername)
 
# Base class2
class Father:
    fathername = ""
    def father(self):
        print(self.fathername)
 
# Derived class
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
 
# Driver's code
s1 = Son()
s1.fathername = "RAM" #passing arguments for father class
s1.mothername = "SITA" #passing arguments for mother class
s1.parents()