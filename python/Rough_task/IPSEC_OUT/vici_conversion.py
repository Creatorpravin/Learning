import socket
import vici


try:
    s = vici.Session()
except socket.error:
    # cannot connect to session, strongswan not running?
    print ('ipsec not active')
    

# parse connections
dict1 = {}
dict2 = {}
for conns in s.list_conns():
    for key1, val1 in conns.items():
        for key2, val2 in val1.items():            
            if "OrderedDict" in str(val2) :
                for key3, val3 in val2.items():
                    dict3 = {}
                    if "OrderedDict" in str(val3):
                      dict4 = {}
                      for key4, val4 in val3.items():                        
                        if type(val4) is list:
                            byteconversion4 = []
                            for i in val4:
                                byteconversion4.append(i.decode())                                                            
                            dict4[key4] = [byteconversion4]
                            #byteconversion = { key4:i4.decode() for (key4,i4) in (key4,val4) }
                        else:
                           dict4[key4] = [val4.decode()]                                               
                      dict3[key4] = dict4
                    else:
                        if type(val3) is list:
                            byteconversion3 = []
                            for j in val3:
                                byteconversion3.append(j.decode())                                                   
                            dict3[str(key3)] = [byteconversion3]
                        else:
                            dict3[str(key3)] = [val3.decode()]
                    dict2[str(key2)] = dict3
            else:
                if type(val2) is list:
                    byteconversion2 = []
                    for k in val2:
                        byteconversion2.append(k.decode())
                    dict2[str(key2)] = [byteconversion2]
                else:
                    dict2[str(key2)] = [val2.decode()]
        dict1[str(key1)] = dict2
print(dict1)

#Another method done by santhosh

import vici
import json


# Learn from https://docs.python.org/3/library/json.html

class ChiefNETJsonBinaryEncoder(json.JSONEncoder):

    def default(self, data):
        # check whether the received data is of type bytes
        if isinstance(data, bytes):
            # decode if the received type is byte
            return data.decode("utf-8")
        # super() to access the base class method. We can also use json.JSONEncoder.default(data) instead of below line
        return super().deafult(data)


stats = (vici.Session()).list_sas()

for stat in stats:
    print(json.dumps(stat, cls = ChiefNETJsonBinaryEncoder))