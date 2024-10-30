#coding:utf-8
#查看CPU利用率 内存情况 服务列出前20个
import os
import socket
import threading
from tabulate import tabulate
from textfsm import TextFSM
import paramiko
import time
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def device_textfsm(muban,file):
    with open(muban) as template, open(file) as output:
        template_FSM = TextFSM(template)
        result = template_FSM.ParseText(output.read())  # .read()千万别忘了
        #print(result)
        header = template_FSM.header
        #print(header)
        device_output=tabulate(result, headers=header)
        #print(device_output+"\n")
    return device_output+"\n"


def pid_textfsm(muban,file,num):
    with open(muban) as template, open(file) as output:
        j_list = []
        list_values_fin = []
        dict_total_mem_all = {}

        template_FSM = TextFSM(template)
        result_list2 = template_FSM.ParseText(output.read())  # .read()千万别忘了
        #print(result_list2)
        for i in result_list2:
            dict_total_mem = {(i[num], i[0]): i}
            dict_total_mem_all.update(dict_total_mem)
        mid_list = sorted(dict_total_mem_all.items(), key=lambda x: float(x[0][0]), reverse=True)  # 是个元组
        # print(mid_list)
        fin_list = [{x[0]: x[1]} for x in mid_list]
        # print(fin_list)

        for i in fin_list:
            list_values = list(i.values())
            list_values = list_values.pop(0)
            # print(list_values)
            list_values_fin.append(list_values)
        # 把每个字典弄出来 然后排序键值
        header = template_FSM.header
        device_output=tabulate(list_values_fin[0:20], headers=header)
        #print(device_output+"\n")
    return device_output+"\n"

def catalague(way,ip):
    #os.chdir(r'/home/rd/python'+'/'+way)  # 每次运行改路径
    file=open(r'/home/rd/python/'+'/'+way+r'/output_from_cli_'+ip,'w')#默认是'r'如果是r 文件不存在则会报错。'w'文件不存在会创建
    return file #这里生成命令输出的文件


def send_email(sender,receicer,password,content):
    # 这份代码比较标准了，可以直接用了

    # 发件人邮箱
    sender = sender
    # 收件人邮箱
    receiver = receicer
    # 抄送人邮箱
    #acc = 'xxxxxxxx@qq.com'
    # 邮件主题
    subject = '服务器运行情况'

    # 邮箱密码（授权码）
    password = password

    # 邮件设置
    msg = MIMEMultipart()
    msg['Subject'] = subject  # 主题
    msg['to'] = receiver  # 接收者
    #msg['acc']=acc#抄送者
    msg['from'] = "信息化员工"  # 发件人

    # 邮件正文
    content = content

    # 添加邮件正文:
    msg.attach(MIMEText(content, 'plain', 'utf-8'))  # content是正文内容，plain即格式为正文，utf-8是编码格式

    # 添加附件
    # 注意这里的文件路径是斜杠
    file_name = r'/home/rd/python/output/check.txt'
    file_name_list = file_name.split('/')[-1]  # 获得文件的名字
    xlsxpart = MIMEApplication(open(file_name, 'rb').read())
    xlsxpart.add_header('Content-Disposition', 'attachment', filename=file_name_list)
    # 服务端向客户端游览器发送文件时，如果是浏览器支持的文件类型，一般会默认使用浏览器打开，比如txt、jpg等，会直接在浏览器中显示，如果需要提示用户保存，就要利用Content-Disposition进行一下处理，关键在于一定要加上attachment
    msg.attach(xlsxpart)

    # 设置邮箱服务器地址以及端口
    smtp_server = "smtp.qq.com"
    smtp = smtplib.SMTP(smtp_server,25)  # 'smtp.qq.com'是QQ邮箱发邮件的服务器，用新浪邮箱就是'smtp.sina.com'，就是smtp加上你们邮箱账号@符号后面的内容。端口默认是25。
    #smtp.set_debuglevel(1)  # 显示出交互信息

    # 登陆邮箱
    smtp.login(sender, password)

    # 发送邮件
    smtp.sendmail(sender, receiver.split(',') , msg.as_string())
    # receiver.split(',')+acc.split(',')是['xxxxxxxx@qq.com', 'xxxxxxxx@qq.com']

    # 断开服务器链接
    smtp.quit()

now = datetime.now()
now_time = now.strftime('%Y-%m-%d_%H-%M-%S')
# os.chdir(r'/home/rd/python/output')
# devic_condition=open(now_time+".txt",'a+')

result1_list=[]
result2_list=[]
result3_list=[]
deivece_with_ConnectionsError=[]
thread=[]

ip_list=["10.10.100.201","10.10.100.202","10.10.100.203"]
username = "xxxx"
password = "xxxxxxx"

def Multi_thread(ip):
    devic_condition = open(r'/home/rd/python/output/check.txt', 'a+')
    try:

        devic_condition.write(ip+'\n')
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip,username=username,password=password)
        print ("Sucessfully login to ", ip)
        command = ssh_client.invoke_shell()
        #内存
        command.send("free -m\n")
        time.sleep(1)
        output_mem = command.recv(65535)
        # 把输出内容到指定文件夹并调用这个文件夹下的模板
        file_mem=catalague('free_m',ip)#在特定路径下创建output_from_cli
        file_mem.write(output_mem.decode("ascii"))
        file_mem.close()#初步判断为bug 必须随手关文件 否则会出现没有输出的问题
        output=device_textfsm(r'/home/rd/python/free_m/template.txt',r'/home/rd/python/free_m/output_from_cli_'+ip)
        #os.chdir(r'/home/rd/python/output')
        devic_condition.write("内存占用情况："+"\n")
        devic_condition.write(output+"\n"+"-"*90+"\n")
        #CPU
        command.send("top -bn 1\n")
        time.sleep(1)
        output_cpu = command.recv(65535)
        # 把输出内容到指定文件夹并调用这个文件夹下的模板
        file_cpu=catalague('top_bn_1_cpu',ip)
        file_cpu.write(output_cpu.decode("ascii"))
        file_cpu.close()
        devic_condition.write("CPU占用情况：" + "\n")
        #output=device_textfsm('template.txt','output_from_cli')
        output = device_textfsm(r'/home/rd/python/top_bn_1_cpu/template.txt',
                                r'/home/rd/python/top_bn_1_cpu/output_from_cli_'+ip)
        #os.chdir(r'/home/rd/python/output')
        devic_condition.write(output+"\n"+"-"*90+"\n")

        #列出内存占用前20个和CPU占用前20个
        command.send("top -bn 1\n")
        time.sleep(1)
        output_pid = command.recv(65535)
        # 把输出内容到指定文件夹并调用这个文件夹下的模板
        file_pid=catalague('top_bn_1_pid',ip)
        file_pid.write(output_pid.decode("ascii"))
        file_pid.close()
        output=pid_textfsm(r'/home/rd/python/top_bn_1_pid/template.txt',
                           r'/home/rd/python/top_bn_1_pid/output_from_cli_'+ip,2)
        #os.chdir(r'/home/rd/python/output')
        devic_condition.write("占用内存前20的进程：" + "\n")
        devic_condition.write(output+"\n"+"-"*90+"\n")
        #os.chdir(r'/home/rd/python/top_bn_1_pid')
        output = pid_textfsm(r'/home/rd/python/top_bn_1_pid/template.txt',
                             r'/home/rd/python/top_bn_1_pid/output_from_cli_'+ip, 1)
        #os.chdir(r'/home/rd/python/output')
        devic_condition.write("占用CPU前20的进程：" + "\n")
        devic_condition.write(output+"\n"+"-"*90+"\n")
        devic_condition.write("="*90+"\n")
        ssh_client.close()

    except   socket.error :#连接超时
        print("连接超时"+ ip +'.')
        result1="连接超时"+ ip +'.'
        devic_condition.write(result1 + "\n")
        result1_list.append(result1)
        deivece_with_ConnectionsError.append(ip)
    except     paramiko.ssh_exception.AuthenticationException:#身份验证异常
        print("身份验证异常" + ip + '.')
        result2="身份验证异常" + ip + '.'
        devic_condition.write(result2 + "\n")
        result2_list.append(result2)
        deivece_with_ConnectionsError.append(ip)
    except Exception as e:
        e=str(e)
        print("未知错误:"+e)
        result3="未知错误:"+ ip+ e
        devic_condition.write(result3 + "\n")
        result3_list.append(result3)
        deivece_with_ConnectionsError.append(ip)

if __name__=='__main__':
    print(f'程序于{time.strftime("%X")}开始')
    for ip in ip_list:
        t=threading.Thread(target=Multi_thread,args=(ip,))
        t.start()
        thread.append(t)

    for i in thread:
        i.join()
    print(f'程序于{time.strftime("%X")}结束')
    con = open(r'/home/rd/python/output/check.txt', "r+")
    content=con.read()

    send_email("xxxxxxxx@qq.com", "xxxxxxxx@qq.com", "1q2w3e4r5t",content)
    os.rename(r'/home/rd/python/output/check.txt', r'/home/rd/python/output'+'/'+now_time+'.txt')