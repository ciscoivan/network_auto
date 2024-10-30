from netmiko import ConnectHandler
import json

SW1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.200.1',
    'username': 'ivan',
    'password': '123.com',
}

connect = ConnectHandler(**SW1)
print ("Sucessfully connected to " + SW1['ip'])
interfaces = connect.send_command('show ip int brief', use_textfsm=True)
for interface in interfaces:
    if interface["status"] == 'up':
        print (f'{interface["intf"]} is up!  IP address: {interface["ipaddr"]}')