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
        output = command.recv(65535).decode("ascii").replace('\r','') # replace效果是去掉多余空行，paramiko模块有专门文章探讨。
        output = output[output.find('!'):] # 把前面登录信息和敲指令过程截图掉。
        with open(ip + '_' + datetime.date.today().isoformat() + '.txt', 'w+') as new_file, open(ip + '_' + (datetime.date.today() - datetime.timedelta(days=1)).isoformat() + '.txt') as old_file:
            new_file.write(output)
            new_file.close()
            new_file = open(ip + '_' + datetime.date.today().isoformat() + '.txt')
            diff = list(difflib.ndiff(old_file.readlines(), new_file.readlines()))
        try:
            with open(ip + '_' + datetime.date.today().isoformat() + '_report' + '.txt', 'w') as report_file:
                for index, line in enumerate(diff):
                    if line.startswith('- ') and diff[index + 1].startswith(('?', '+')) == False:
                        report_file.write('\n已被移除的旧配置： ' + '\n\n' + line + '\n----------------\n\n')
                    elif line.startswith('+ ') and diff[index + 1].startswith('?') == False:
                        report_file.write('\n已被添加的新配置： ' + '\n\n' + '...\n' + diff[index - 2] + diff[index - 1] + line + '...\n' + '\n----------------\n')
                    elif line.startswith('- ') and diff[index + 1].startswith('?') and diff[index + 2].startswith('+ ') and diff[index + 3].startswith('?'):
                        report_file.write('\n已被修改的配置（长度不变或变短）: \n\n' + line + diff[index + 1] + diff[index + 2] + diff[index + 3] + '\n----------------\n')
                    elif line.startswith('- ') and diff[index + 1].startswith('+') and diff[index + 2].startswith('? '):
                        report_file.write('\n已被修改的配置（长度变长）: \n\n' + line + diff[index + 1] + diff[index + 2] + '\n----------------\n')
                    else:
                        pass  # pass是不处理其它的情况，如果还有其它情况，可由这里继续调整代码。
        except IndexError:
            pass
        with open(ip + '_' + datetime.date.today().isoformat() + '_report' + '.txt') as report_file, open('master_report_' + datetime.date.today().isoformat() + '.txt', 'a') as master_report:
            if len(report_file.readlines()) < 1:
                master_report.write('\n\n*** 交换机: ' + ip + ' ***\n')
                master_report.write('\n' + '于' + datetime.date.today().isoformat() + ' 没有发现任何配置变化\n\n\n')
            else:
                report_file.seek(0)
                master_report.write('\n\n*** 交换机: ' + ip + ' 发现以下配置变化***\n\n')
                master_report.write(report_file.read())

