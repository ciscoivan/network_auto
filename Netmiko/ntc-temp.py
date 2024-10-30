from  netmiko import ConnectHandler


A1 = { 'device_type' : 'cisco_ios',
                 'ip':'192.168.10.1',
                 'port':'9301',
                 'username':'ivan',
                 'password':'1A.liyang.com'}

connect = ConnectHandler(**A1)
output = connect.send_command('show ip route  ',use_textfsm=True)
print(type(output))
print(output)
for i in output:
#    print(i['version'])
#    print(i['uptime'])
 print(i['protocol'])