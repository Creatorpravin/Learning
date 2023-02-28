import re
temp = []
temp_2 = []
temp_3 = []
temp_4 = []
temp_5 = []
temp_6 = []
temp_7 = []
with open(file="ipsec_text.txt",mode="+r") as stas:
    
    for i in stas:
        temp.append(i)
    
    #   temp.append(i.replace("=",":").replace("\n",","))
    for j in temp:
        if " =" in j:
            temp_2.append(j.replace(" =",'" :'))
        elif " {" in j:
            temp_2.append(j.replace(" {"," : {"))
        else:
            temp_2.append(j)
    for k in temp_2:
        temp_3.append(k.replace("\n",",").replace("{,","{"))
    for i in temp_3:
        temp_4.append(i.replace(": ", ': "').replace(",",'",'))
    for a in temp_4:
        temp_5.append(a.replace('"{', "{").replace('}"',"}"))        
    for b in temp_5:
        if '["' or "/32" or "/24" in b:
            print(b)
            temp_6.append(b.replace('["', '[').replace('",',','))
        # if "/32" or "/24" in b:
        #     temp_6.append(b.replace('",',','))
        
    for c in temp_6:
        print(c) 