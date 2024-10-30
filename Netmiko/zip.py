import os

list_A = ['192.168.11.11','192.168.11.12','192.168.11.13','192.168.11.14','192.168.11.15']
list_B = ['1.1.1.1','2.2.2.2','3.3.3.3','4.4.4.4','5.5.5.5']

c = list(zip(list_A,list_B))

for i ,a in c:
    print(i,a)
for i ,a in c:
    print(i,a)

with open('devices_list.txt') as f:
    for ips, a in zip(f.readlines(), range(1,3)) :
        print(ips ,a)


print(os.getcwd())