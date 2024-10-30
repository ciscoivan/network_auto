
mac = 'aabb:cc80:7000'
print(mac.replace(':',"-"))
print(mac.replace(':',"."))

a = 'info-center loghost 192.168.10.1 source-ip 10.10.10.10'

print(len(a))
print(a[42:54].strip())

a = 'info-center loghost 192.168.10.1 source-ip 10.10.10.10'
c = a.split(" ")
print(c[4])

a = 'info-center loghost 192.168.10.1 source-ip 10.10.10.10'
c = a.find('10.10.10.10')
print(c)