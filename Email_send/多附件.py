import  smtplib
from  email.mime.text import  MIMEText
from  email.header import  Header
from email.mime.multipart import  MIMEMultipart

def send(file_list):
    mail_host = 'smtp.qq.com' #设置服务器
    mail_user = '513046322'
    mail_password = 'ljmnaaxozrlybhcg'


    sender = '513046322@qq.com'  #发送的游戏
    receivers = ['513046322@qq.com']
    log = "ciscoasdasdasd"

    #message = MIMEText('<p style="color:red;">这是一个测试</P>','html','utf-8')

    message = MIMEMultipart()

    message['From'] = Header(sender)
    message['Subject'] = Header('python测试','utf-8')
    for file_name in file_list:
        print("file_name",file_name)
        attr = MIMEText(open(file_name,'rb').read(),'base64','utf-8')
        attr['Content-Type'] = 'application/octet-stream'  #定义流类型
        attr['Content-Disposition'] = 'attachment;filename='+file_name
        #print(message.as_string())
        message.attach(attr)
        message.attach(MIMEText('网络巡检收集日志','plain','utf-8'))

    try:
        smtpobj = smtplib.SMTP()
        smtpobj.connect(mail_host, 25)
        smtpobj.login(mail_user,mail_password)
        smtpobj.sendmail(sender,receivers,message.as_string())
    except smtplib.SMTPException as e:
        print('error:%s' % e)

if __name__ == '__main__':
    file_list = ['192.168.100.227--info.txt','192.168.100.228--info.txt']
    email = send(file_list=file_list)