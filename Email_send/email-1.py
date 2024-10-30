#这份代码比较标准了，可以直接用了
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

#发件人邮箱
sender="xxxxxxx@qq.com"#改成自己的邮箱，相当于自己给自己放邮件
#收件人邮箱
receiver="xxxxxxx@qq.com"#改成自己的邮箱
#抄送人邮箱
acc = 'xxxxxx@qq.com'#填写抄送人的邮箱
#邮件主题
subject = '这是一份测试邮件'#这是邮箱的题目

#邮箱密码（授权码）
password="xxxxxxxxxxx"#授权码要从邮箱界面获取，后面有介绍

#邮件设置
msg = MIMEMultipart()
msg['Subject'] = subject#主题
msg['to'] = receiver#接收者
msg['Cc'] = acc#抄送者
msg['from'] = "信息化员工"#发件人

#邮件正文
content = "你好，这是一份测试邮件"

#添加邮件正文:
msg.attach(MIMEText(content, 'plain', 'utf-8'))# content是正文内容，plain即格式为正文，utf-8是编码格式

#添加附件
#注意这里的文件路径是斜杠
file_name='D:\\学习\\test\\test.txt'
file_name_list=file_name.split('\\')[-1]#获得文件的名字
xlsxpart = MIMEApplication(open(file_name, 'rb').read())
xlsxpart.add_header('Content-Disposition', 'attachment', filename=file_name_list)
#服务端向客户端游览器发送文件时，如果是浏览器支持的文件类型，一般会默认使用浏览器打开。
#比如txt、jpg等#会直接在浏览器中显示，如果需要提示用户保存，就要利用Content-Disposition进行一下处理，关键在于一定要加上attachment
msg.attach(xlsxpart)

#设置邮箱服务器地址以及端口
smtp_server ="smtp.qq.com"#'smtp.qq.com'是QQ邮箱发邮件的服务器，用新浪邮箱就是'smtp.sina.com'，就是smtp加上你们邮箱账号@符号后面的内容。
smtp = smtplib.SMTP(smtp_server, 25)#端口默认是25。
smtp.set_debuglevel(1) #显示出交互信息

#登陆邮箱
smtp.login(sender, password)

#发送邮件
smtp.sendmail(sender, receiver.split(',')+acc.split(','), msg.as_string())
#receiver.split(',')+acc.split(',')是['xxxxxxxxx@qq.com', 'xxxxxxxxx@qq.com']

#断开服务器链接
smtp.quit()