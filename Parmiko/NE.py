devices = {'R1':{'ip':'192.168.100.1'},'R2':{'ip':'192.168.100.2'}}

for a in devices.keys():
    print(devices[a]['ip'])


source="7782,helen,IT,SALES,5000$7783,amanda,IT,SALES,6000$7784,ivan,IT,SALES,7000"
list1=source.split("$")

all_list={}
for i in range(0,len(list1)):
    e=list1[i].split(',')
    emp={"no":e[0],"name":e[1],"job":e[2],"dep":e[3],"mem":e[4]}
    print(emp)
    all_list[emp['no']]=emp
print(all_list)
empon=input("xxx")
emp=all_list.get(empon)
print(emp)

