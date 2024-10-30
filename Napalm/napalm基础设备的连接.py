from napalm import get_network_driver
import pprint

pp = pprint.PrettyPrinter(indent=2)

# drive是一个类class，传入drive_name
drive = get_network_driver('ios')
# 类实例化
conn = drive(hostname='192.168.0.20',
             username='cisco',
             password='cisco',
             optional_args={'port': 22})
# 建立连接会话
conn.open()
# 使用其中一个方法，获取接口ip地址
ouput = conn.get_interfaces_ip()
# 打印结果
pp.pprint(ouput)

# 关闭连接
conn.close()