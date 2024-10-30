import netmiko
from netmiko import ConnectHandler,file_transfer

sw1 = {'device_type':'huawei',
      'ip':'192.168.11.12',
      'username':'python',
      'password':'123',
      'secret':'123'}

with ConnectHandler(**sw1) as connect:
    print ("已经成功登陆交换机" + sw1['ip'])

    output = connect.send_command_timing(command_string="dir",)
    output += connect.send_command_timing(command_string="ftp 192.168.11.11")
    output += connect.send_command_timing(command_string="python")
    output += connect.send_command_timing(command_string="123")
    output += connect.send_command_timing(command_string="dir")
    output += connect.send_command_timing(command_string="get text.txt")
    output += connect.send_command_timing(command_string="quit")
    print(output)

"""
timing这条函数可以帮我们屏蔽掉一些等待控制等，彰显netmiko的各种人性化哈哈。）
实验目的
（1）FTP（或SCP）将同目录下的text.txt送入设备Layer3Switch-1（其实这部分不是python内容，但过程也记录下吧）。

（2）通过netmiko登录设备Layer3Switch-2，FTP连接设备Layer3Switch-1，拷贝text.txt。
sys
ftp server enable 
aaa
 local-user python ftp-directory flash:
 local-user python service-type telnet ssh ftp


"""