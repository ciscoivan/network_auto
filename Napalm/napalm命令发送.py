import  napalm
import  pprint
# drive是一个类class
from  napalm import get_network_driver

pp = pprint.PrettyPrinter(indent=2)
drive = get_network_driver('ios')
# 类实例化
conn = drive(hostname='192.168.0.20',
             username='cisco',
             password='cisco',
             optional_args={'port': 22, 'secret': 'cisco'})
# 建立连接会话
conn.open()
# 发送命令
output = conn.cli(['show ip int brief', 'show arp'])
pp.pprint(output)

# 关闭连接
conn.close()