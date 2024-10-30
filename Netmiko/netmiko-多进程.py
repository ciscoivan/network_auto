import getpass
import sys
from netmiko import ConnectHandler
from concurrent.futures import ThreadPoolExecutor as Pool



#user = input('Username: ')
#passwd = getpass.getpass('Password: ')


def write_txt(filename, config_list):
    with open(filename, 'w+') as f:
        for config in config_list:
            f.write(config)

def ssh_action(ip):
    sw_info = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': 'ivan',
        'password': '123.com'
    }
    ssh_client = ConnectHandler(**sw_info)
    print('login ' + sw_info['ip'] + ' success\n')
    output = ssh_client.send_command('show run')
    print(output)
    file_name = f'{ip}.txt'
    write_txt(file_name, output)

with Pool(max_workers=3) as t:
    with open('ipfile', 'r') as ip_list:
        for ip in ip_list.readlines():
            ip = ip.strip()
            task = t.submit(ssh_action, ip)
