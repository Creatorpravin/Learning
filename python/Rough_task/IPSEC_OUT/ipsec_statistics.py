import re
temp = []
temp_2 = []
temp_3 = []
with open(file="ipsec_text.txt",mode="+r") as stas:
    
    for i in stas:
        temp.append(i)
     
    #   temp.append(i.replace("=",":").replace("\n",","))
    for j in temp:
        if " =" in j:
            temp_2.append(j.replace(" ="," :"))
        elif " {" in j:
            temp_2.append(j.replace(" {"," : {"))
        else:
            temp_2.append(j)
    for k in temp_2:
        temp_3.append(k.replace("\n",",").replace("{,","{"))
    for j in temp_3:
        print(re.findall("\w+",j))