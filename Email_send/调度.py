import smtplib
import schedule
import time
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import os
import logging

def send():
    mail_host = 'smtp.qq.com'  # 设置服务器
    mail_user = '513046322'
    mail_password = 'ljmnaaxozrlybhcg'

    sender = '513046322@qq.com'  # 发送的游戏
    receivers = ['513046322@qq.com']
    log = "ciscoasdasdasd"

    message = MIMEMultipart()

    message['From'] = Header(sender)
    message['Subject'] = Header('python测试', 'utf-8')

    file_path = 'send.py'
    with open(file_path, 'rb') as f:
        attr = MIMEText(f.read(), 'base64', 'utf-8')
    attr['Content-Type'] = 'application/octet-stream'  # 定义流类型
    attr['Content-Disposition'] = f'attachment;filename="{os.path.basename(file_path)}"'
    message.attach(attr)
    message.attach(MIMEText('网络巡检收集日志', 'plain', 'utf-8'))
    try:
        smtpobj = smtplib.SMTP()
        smtpobj.connect(mail_host, 25)
        smtpobj.login(mail_user,mail_password)
        smtpobj.sendmail(sender,receivers,message.as_string())
    except smtplib.SMTPException as e:
        logging.error(f'error: {e}')

if __name__ == "__main__":
    schedule.every(10).seconds.do(send)
    while 1:
        schedule.run_pending()
        time.sleep(1)