from napalm import get_network_driver

import pprint
import os

pp = pprint.PrettyPrinter(indent=2)

host = "172.16.1.1"

# drive是一个类class
drive = get_network_driver('ios')
# 类实例化
conn = drive(hostname= host,
             username= 'noc',
             password= '123.Com',
             optional_args= {'port': 22})
# 建立连接会话
conn.open()
# 获取设备配置信息
output = conn.get_config()
# 打印结果
pp.pprint(output)
running_config = output['running']
# 写入文件
with open(os.path.join('LOG', f'{host}-running.conf'), 'w+') as f:
    f.writelines(running_config)

# 关闭连接
conn.close()