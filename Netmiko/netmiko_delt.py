from netmiko import ConnectHandler,BaseConnection,platforms
import logging

logging.basicConfig(filename='aaaaaadebug.log', level=logging.DEBUG)
logger = logging.getLogger('netmiko')



device = { 'host':'192.168.10.1',
           'device_type':'cisco_ios',
           'username':'steven',
           'password':'Tian.siyu1',
           'secret':'123.com'
           }

conn = ConnectHandler(**device)
conn.enable()


output = conn.send_command(command_string="delete  flash0:asdm-792.bin",
                              expect_string=r"Delete .*",
                              strip_prompt=False,
                              strip_command=False,
                              cmd_verify = False
                              )


output += conn.send_command(command_string="",
                               expect_string=r"Delete flash0:.*",
                               strip_prompt=False,
                               strip_command=False,
                               cmd_verify = False
                              )

print(output)
print("image删除成功")
conn.disconnect()

