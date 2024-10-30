from netmiko import ConnectHandler
from pprint import  pprint
connection_info = {
        'device_type': 'cisco_ios',
        'host': '172.16.1.1',
        'username': 'noc',
        'password': '123.Com'
}

with ConnectHandler(**connection_info) as conn:
    out = conn.send_command("show interfaces", use_textfsm=True)
    print(out)