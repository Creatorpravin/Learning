import geocoder as geo

ip_addr = "13.107.6.171"

ip = geo.ip(ip_addr)

print(ip.city)
print(ip.country)
print(ip.latlng)
print(ip)


