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
time.sleep(1)
command.send("123.com\n")
time.sleep(1)
command.send('terminal length 0  ')

with open('aaaa.txt','wb') as f :
    command.send("show run\n")
    time.sleep(2)
    file_infp = command.recv(65535)
    f.write(file_infp)

print(file_infp)
ssh_client.close