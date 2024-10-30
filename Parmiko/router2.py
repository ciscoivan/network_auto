import paramiko
import time
import getpass


ip = "192.168.100.227"
username = "ivan"
password = "123.com"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip, username=username, password=password,look_for_keys=False,allow_agent=False)
command = ssh_client.invoke_shell()
command.send("enable\n")
command.send("123.com\n")
command.send("configure terminal\n")
print("正在批量创建IP地址")
for i in range(20,30):
    ipp = "192,168," + str(i) +","+ str(i)
    command.send(" interface loopback" + str(i) + '\n' )
#    command.send("ip address" + " "+ ipp.replace(",", ".") + " "+  "255.255.255.0" + '\n')
    time.sleep(1)
    print("创建完成")
output = command.recv(65535)
output = str(output)
ssh_client.close