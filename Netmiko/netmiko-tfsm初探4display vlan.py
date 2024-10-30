from  netmiko import  ConnectHandler
from  textfsm import    TextFSM


connection_info = {'device_type':'huawei',
      'ip':'10.1.1.1',
      'username':'ivan',
      'password':'123.com'}

with ConnectHandler(**connection_info) as conn:
    output = conn.send_command("display vlan")
print(output)
print(type(output))

with open('display_vlan.template') as f :
    result = TextFSM(f).ParseText(output)
    print(result)

for each in result:
    print(each[0],each[-1])