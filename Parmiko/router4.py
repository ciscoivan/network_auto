import paramiko
import getpass
import time

date1 = time.strftime("%Y-%m-%d",time.localtime())
comands = ['show  environment   power\n' ,'show  environment fan','show run\n','show ip int br\n','show ver\n']
username = input('Username: ')
password = getpass.getpass('password: ')

f = open("ip_list.txt", "r")
for line in f.readlines():
    ip = line.strip()
    file_name = ip + " "+date1 +"info.txt"
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=username, password=password) 
    print("Successfully connect to ", ip)
    remote_connection = ssh_client.invoke_shell()
    with open(file_name,'wb') as f:
        for comand in comands:
            remote_connection.send(comand)
            time.sleep(2)
            file_info = remote_connection.recv(65535)
            print("正在执行操作命令")
            f.write(file_info)
    remote_connection.close()

