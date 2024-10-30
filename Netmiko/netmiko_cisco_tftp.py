from netmiko import ConnectHandler,BaseConnection,platforms




device = { 'host':'192.168.10.1',
           'device_type':'cisco_ios',
           'username':'steven',
           'password':'Tian.siyu1',
           'secret':'123.com'
           }

conn = ConnectHandler(**device)
conn.enable()

result =conn.send_command_timing(command_string='copy  tftp:  flash0:')

result += conn.send_command_timing(command_string='192.168.100.100')

result += conn.send_command_timing(command_string='asdm-792.bin')
result += conn.send_command_timing(command_string='')

print(result)
if 'asdm-792.bin' in result:
    print("镜像上传成功")



conn.disconnect()

