import xlrd
import xlwt
import paramiko
import time
import os

excel_path = '../netmiko/devicelist.xlsx'


# 读取excel的数据
def getExcelData(excel_path):
    excel = xlrd.open_workbook(excel_path)  # 加载excel文件
    table = excel.sheet_by_index(0)  # 读取第几个sheet
    data = []
    for n in range(table.nrows):  # 遍历zheng
        #print(type(n))
        if n == 0  :
            continue
        value = table.row_values(n)
        if value[2] == "":
            continue
        sep = {
            "name": value[0],
            "ip": value[1],
            "port": int(value[2]),
            "user": value[3],
            "password": value[4]
        }
        print(sep)
        data.append(sep)
    table1 = excel.sheet_by_index(1)  # 读取第2个sheet  命令
    command_list = []
    for n in range(table1.nrows):  # 遍历zheng
        print(n)
        if n == 0:
            continue
        value = table1.row_values(n)
        command_list.append(value[0])
    print(command_list)

    return {
        'data':data,
        'command_list':command_list
    }


# ssh 连接并执行命令
def sshExec(ssh_data,command_list):
    show_data = {}
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(
        hostname=ssh_data['ip'],
        port=ssh_data['port'],
        username=ssh_data['user'],
        password=ssh_data['password'],
        allow_agent=False,
        look_for_keys=False)
    command = ssh_client.invoke_shell()
    time.sleep(1)
    output = command.recv(65535)
    output.decode("utf-8")
    # 发送命令
    for command_i in command_list:
        command.send(command_i + ' \n')
        time.sleep(1)
        output = command.recv(65535)
        re_str = output.decode("utf-8")
        f = open('run.txt', 'w')
        f.write(re_str)
        f.close()
        spaceRecursion(command, 'run.txt')
        environment_str = open('run.txt', encoding='utf-8')
        show_data[command_i] = environment_str.read()
    return show_data


def spaceRecursion(command, file_name):
    command.send(' ')
    time.sleep(1)  # 有时候输出较多，需要将等待延长几秒
    output = command.recv(65535)
    space_str = output.decode("utf-8")
    print(space_str)
    f = open(file_name, 'a+')
    f.write(space_str)
    f.close()
    if space_str.find("--More--") != -1:
        spaceRecursion(command, file_name)




# 获取到excel里的服务器地址
ssh_list = getExcelData(excel_path)

# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding='utf-8')    # 循环服务器执行命令

# 创建一个worksheet
worksheet = workbook.add_sheet('ssh')
worksheet.write(0, 0, label='IP')
key = 1
for command_i in ssh_list['command_list']:
    worksheet.write(0, key, label=command_i)
    key = key+1
num = 1
for i in ssh_list['data']:
    print(i)
    re_data = sshExec(i,ssh_list['command_list'])
    # 保存数据
    #保存show run


    worksheet.write(num, 0, i['ip'])
    key = 1
    for command_i in ssh_list['command_list']:
        if command_i.find("show run") != -1:
            f = open(i['ip'] + '.txt', 'w')
            f.write(re_data[command_i])
            f.close()
        worksheet.write(num, key, re_data[command_i])
        key = key +1
    num = num + 1
workbook.save('show.xls')