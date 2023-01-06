import nmap #pip3 install python-nmap

begin = 10
end = 50

target = "127.0.0.1"

scanner = nmap.PortScanner()

# for i in range(begin,end+1):
#     res = scanner.scan(target,str(i))

#     res = res['scan'][target]['tcp'][i]['state']

#     print(f'port {i} is {res}.')

print(scanner.scan("192.168.1.165","1-1000"))