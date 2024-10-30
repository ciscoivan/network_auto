import  napalm
from  napalm import  get_network_driver
import  pprint

pp = pprint.PrettyPrinter(indent=2)
# drive是一个类class
drive = get_network_driver('ios')
# 类实例化
conn = drive(hostname='192.168.0.20',
             username='cisco',
             password='cisco',
             optional_args={'port': 22})
# 建立连接会话
conn.open()
# 获取接口ip地址
output = conn.get_facts()
# 打印结果
pp.pprint(output)
# 关闭连接
conn.close()