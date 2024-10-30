import paramiko,getpass,time

devices = {'home-router':{'ip':'192.168.10.48'}}

comands = ['show run\n','show ip int br\n','show ver\n']


username = input("Username: ")
password = getpass.getpass('请输入密码Password: ')

for device in devices.keys():
        file_name = device + 'info.txt'
        conn = paramiko.SSHClient()
        conn.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        conn.connect(devices[device]['ip'],username=username,password=password,look_for_keys=False,allow_agent=False)
        conn_new = conn.invoke_shell()
        conn_new.send('term len 0\n')
        conn_new.recv(65535)
        with open(file_name,'wb') as f:
            for comand in comands:
                conn_new.send(comand)
                time.sleep(2)
                file_info = conn_new.recv(65535)
                print("正在执行操作命令")
                f.write(file_info)
                print("操作完成")
        conn_new.close()




