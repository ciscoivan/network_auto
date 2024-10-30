from netmiko import ConnectHandler
from pprint import  pprint
connection_info = {
        'device_type': 'cisco_ios',
        'host': '192.168.200.10',
        'username': 'ivan',
        'password': '123.com'
}

with ConnectHandler(**connection_info) as conn:
    out = conn.send_command("show interfaces", use_textfsm=True)
    print(out)