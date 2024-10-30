"""
在网络设备中输入某些命令后系统会返回一个提示命令，询问你是继续执行命令还是撤销命令，比如我们在实验7中向SW1传入了test.txt这个文件，
如果这时我们想将它删除，则需要输入命令del flash0:/test.txt，输入该命令后，系统会询问你是否confirm，如下：\
这时如果你输入字母y或者敲下回车键则系统会执行del命令将该文件删除，如果你输入字母n，则系统会中断该命令，该文件不会被删除。
在Netmiko中我们可以调用send_command()函数中的command_string，expect_string，strip_prompt，strip_command四个参数来应对这种情况。
我们在第一个send_command()函数中通过command_string这个参数向SW1输入命令del flash0:/test.txt，然后在expect_string这个参数里告知Netmiko去SW1的回显内容里查找
“Delete flash0:/test.txt?”这段系统返回的提示命令，如果查到了的话，则继续输入命令y（第二个send_command()）让脚本删除test.txt这个文件，
之后如果接收到命令提示符"#"，则继续执行脚本后面的代码。strip_prompt和strip_command两个参数这里放Fasle就行
"""

from netmiko import ConnectHandler
sw1 = {
        'device_type': 'cisco_ios',
        'ip': '192.168.2.11',
        'username': 'python',
        'password': '123'
}

with ConnectHandler(**sw1) as connect:
    print ("已经成功登陆交换机" + sw1['ip'])
    output = connect.send_command(command_string="del flash0:/test.txt",
                  expect_string=r"Delete flash0:/test.txt?",
                  strip_prompt=False,
                  strip_command=False)
    output += connect.send_command(command_string="y",
                  expect_string=r"#",
                  strip_prompt=False,
                  strip_command=False)

print(output)

"""
 import netmiko
from netmiko import ConnectHandler,file_transfer

sw1 = {'device_type':'huawei',
      'ip':'192.168.11.12',
      'username':'python',
      'password':'123',
       }

with ConnectHandler(**sw1) as connect:
    print ("已经成功登陆交换机" + sw1['ip'])

    output = connect.send_command(command_string="delete flash:/text.txt",
                  expect_string=r"Delete flash:/text.txt?",
                  strip_prompt=False,
                  strip_command=False)
    output += connect.send_command(command_string="y",
                  expect_string=r">",
                  strip_prompt=False,
                  strip_command=False)

    print(output)
"""