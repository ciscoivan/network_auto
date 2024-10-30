import difflib
import paramiko
import datetime
import time

f = open('ip_list')

for line in f.readlines():
    ip = line.strip()
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip,username='ivan',password='123.com',look_for_keys=False)
    print('已经成功登陆交换机',ip)
    command = ssh_client.invoke_shell()
    command.send('term len 0\n')
    command.send('show run\n')
    time.sleep(5)
    output = command.recv(65535).decode("ascii").replace('\r','')
    output = output[output.find('!'):]   # 把前面登录信息和敲指令过程截图掉。
    with open(ip + '_' + (datetime.date.today() - datetime.timedelta(days=1)).isoformat() +'.txt', 'w+') as old_file:
         old_file.write(output)