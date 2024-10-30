import paramiko
import time
import socket
# 存放认证失败的设备信息
switch_with_authentication_issue = []
# 存放认证失败的设备信息
switch_not_reachable = []

with open('iplist.txt','r') as f:
     for i in f.readlines():
         try:
             ip = i.strip()
             ssh_client = paramiko.SSHClient()
             ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
             ssh_client.connect(hostname=ip,username='ivan',password='123.com',look_for_keys=False)
             print('已经成功登陆交换机 ' + ip)
             command = ssh_client.invoke_shell()
             command.send('show run\n')
             time.sleep(5)
             output = command.recv(65535).decode('ASCII')
             print(output)
         except paramiko.ssh_exception.AuthenticationException:
             print(ip + "用户验证失败！")
             switch_with_authentication_issue.append(ip)
         except socket.error:
             print(ip + "目标不可达！")
             switch_not_reachable.append(ip)
ssh_client.close()

print('\n 下列交换机用户验证失败：')
for i in switch_with_authentication_issue:
    print(i)

print('\n 下列交换机不可达：')
for i in switch_not_reachable:
    print(i)