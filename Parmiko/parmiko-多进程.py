#多进程创建文件件并且进入创建的文件件保存配置
import paramiko
import  os
import sys
import time
from  datetime import datetime
from concurrent.futures import ThreadPoolExecutor as pool


def wire_config(filename,config_list):
    with open(filename,'w+') as f:
        for config in config_list:
            f.write(config)


def ssh_action(ip):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip,username='ivan',password="123.com",look_for_keys=False)
    print("ssh login "+ip+"success\n")
    command = ssh_client.invoke_shell()
    command.send('ter len 0\n')
    command.send('show run\n')
    time.sleep(3)
    output = command.recv(6553555).decode('ascii')
    ssh_client.close()
    file_name = f'{ip}.txt'
    wire_config(file_name,output)


now_time = datetime.now()
now_time = str(now_time)
now_time = now_time.split()[0]
foldername = now_time
old_folder_name = os.path.exists(foldername)
if old_folder_name == True:
    print("文件件存在，程序终止")
    sys.exit()
else:
     os.mkdir(foldername)
     os.chdir(foldername)

ip_file = 'D:/code/parmiko/iplist.txt'

with pool(max_workers=6) as t:
    with open(ip_file,'r') as ip_list:
        for ip in ip_list.readlines():
           ip = ip.strip()
           task = t.submit(ssh_action,ip)

        print(task.result())