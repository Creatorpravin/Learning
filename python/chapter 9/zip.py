from audioop import reverse


group1 = [1,2,3,4,5,6,7,8,9]
group2 = [9,8,7,6,5,45,3,2,1]
for item in zip(group1, group2): #use to zip the both value in both list
    print(item)
#iterate the value and perform some operations for each values
for gr1,gr2 in zip(group1,group2):
    print("average=",(gr1 + gr2 )/2)