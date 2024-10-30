from netmiko import Netmiko
import os
from dev_info import nxosv9k

def save_dev_log_2_file(host,cmd,output):
    if not os.path.exists(host):
        os.mkdir(host)
    log_path = os.path.join(host, cmd.replace(' ', '_'))
    log_file_name = f"{log_path}.log"
    with open(log_file_name,mode='w',encoding='utf8') as f:
        f.write(output)
        f.write('\n')


def ssh_dev_show_commands(dev_info,cmds):
    with Netmiko(**dev_info) as dev_con:
        for cmd in cmds:
            output = dev_con.send_command_timing(cmd)
            save_dev_log_2_file(dev_info['host'],cmd,output)

if __name__ == '__main__':
    nxosv9k['timeout'] = 120
    nxosv9k['conn_timeout'] = 20

    ssh_dev_show_commands(nxosv9k,['show version'])