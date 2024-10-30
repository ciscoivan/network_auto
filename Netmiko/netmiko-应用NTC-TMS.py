from netmiko import ConnectHandler
import json

R1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.200.1',
    'username': 'ivan',
    'password': '123.com',
}

connect = ConnectHandler(**R1)
print ("Sucessfully connected to " + R1['ip'])
interfaces = connect.send_command('show ip int brief', use_textfsm=True)
print (json.dumps(interfaces, indent=2))