from netmiko import ConnectHandler,BaseConnection,platforms
from jinja2 import FileSystemLoader,Environment
import  time




device = { 'host':'192.168.200.1',
           'device_type':'cisco_ios',
           'username':'ivan',
           'password':'123.com',
           'secret':'123.com'
           }

conn = ConnectHandler(**device)
conn.enable()
#config_commands = ['interface LoopBack 0','ip add 2.2.2.2 32']
#output = conn.send_config_set(config_commands)
#print(output)
result = conn.send_command('show run')
print(result)
with open('d://'+device['host']+'.cfg', 'w') as f:
    f.write(result)

conn.disconnect()

