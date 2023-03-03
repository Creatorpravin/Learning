import sys
import socket
import ujson
import vici
import orjson
import json

try:
    s = vici.Session()
except socket.error:
    # cannot connect to session, strongswan not running?
    print ('ipsec not active')
    sys.exit(0)


def parse_sa(in_conn):
    result = {'local-addrs': '', 'remote-addrs': '', 'children': '', 'local-id': '', 'remote-id': ''}
    result['version'] = in_conn['version']
    if 'local_addrs' in in_conn:
        result['local-addrs'] = b','.join(in_conn['local_addrs'])
    elif 'local-host' in in_conn:
        result['local-addrs'] = in_conn['local-host']
    if 'remote_addrs'  in in_conn:
        result['remote-addrs'] =  b','.join(in_conn['remote_addrs'])
    elif 'remote-host' in in_conn:
        result['remote-addrs'] = in_conn['remote-host']
    if 'children' in in_conn:
        result['children'] = in_conn['children']

    result['sas'] = []
    return result

result = dict()
# parse connections
dict = {}
dict2 = {}
for conns in s.list_conns():
    print(type(conns))
    # print("+++++++++++++++++++++++++++")
    # # output = ujson.loads(ujson.dumps(conns))
    # # print(output)
    for key1, val1 in conns.items():
        #print(key1, val1)        
        for key2, val2 in val1.items():
            #print(key2, val2)            
            dict[str(key2)] = [str(val2)]
            
            # if "OrderedDict" in str(val2) :
            #     print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            #     print(val2)
            #     print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            #     for key3, val3 in val2:
            #         print(key3, val3)
        dict2[str(key1)] = dict

            # for key3, val3 in val2.items():
            #      print(key3,val3)
print(dict2)



for connection_id in conns:
        result[connection_id] = parse_sa(conns[connection_id])
        result[connection_id]['routed'] = True
        result[connection_id]['local-class'] = []
        result[connection_id]['remote-class'] = []
        # parse local-% and remote-% keys
        for connKey in conns[connection_id].keys():
            if connKey.find('local-') == 0:
                if 'id' in conns[connection_id][connKey]:
                    result[connection_id]['local-id'] = conns[connection_id][connKey]['id']
                result[connection_id]['local-class'].append(conns[connection_id][connKey]['class'])
            elif connKey.find('remote-') == 0:
                if 'id' in conns[connection_id][connKey]:
                    result[connection_id]['remote-id'] = conns[connection_id][connKey]['id']
                result[connection_id]['remote-class'].append(conns[connection_id][connKey]['class'])
        result[connection_id]['local-class'] = b'+'.join(result[connection_id]['local-class'])
        result[connection_id]['remote-class'] = b'+'.join(result[connection_id]['remote-class'])

# attach Security Associations
for sas in s.list_sas():
    for sa in sas:
        if sa not in result:
            result[sa] = parse_sa(sas[sa])
            result[sa]['routed'] = False
        result[sa]['sas'].append(sas[sa])

#print (ujson.dumps,(result, reject_bytes=False))
#print(orjson.dumps(result), "utf-8")#, orjson.loads)