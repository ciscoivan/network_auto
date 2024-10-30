import  smtplib
from  email.mime.text import  MIMEText
from  email.header import  Header

mail_host = 'smtp.qq.com' #设置服务器
mail_user = '513046322'
mail_password = 'ljmnaaxozrlybhcg'


sender = '513046322@qq.com'  #发送的游戏
receivers = ['513046322@qq.com']
log = "ciscoasdasdasd"

message = MIMEText('%s'%log,'plain','utf-8')

message['From'] = Header(sender)
message['Subject'] = Header('python测试','utf-8')
print(message.as_string())
try:
    smtpobj = smtplib.SMTP()
    smtpobj.connect(mail_host, 25)
    smtpobj.login(mail_user,mail_password)
    smtpobj.sendmail(sender,receivers,message.as_string())
except smtplib.SMTPException as e:
    print('error:%s' % e)