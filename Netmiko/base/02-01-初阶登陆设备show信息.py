from netmiko import ConnectHandler, Netmiko

import logging

logging.basicConfig(
    level=logging.DEBUG,
)


if __name__ == '__main__':
    '''
    通过ConnectHandler（等价于Netmiko，两个是完全一致的） ，输入设备类型 ip(host) 用户名密码 端口（默认是ssh的22）等
    这其实是一个函数，它会根据你的device_type给你用对应的类实例化成对象
    nxosv9k = {
    'device_type': 'cisco_nxos',
    'host': 'sbx-nxos-mgmt.cisco.com',
    'username': 'admin',
    'password': 'Admin_1234!',
    'port': 22,  # optional, defaults to 22
    # 'secret': 'secret',  # optional, defaults to ''
    'session_log':'test111111s.log',
    'conn_timeout':20,
    'timeout':120,
    }
    相关后续演示，如果涉及到设备大家可以参考以上配置，这是思科devnet的一台Nexus 9000的交换机
    
    '''

    net_conn = Netmiko(device_type='cisco_ios',   # device_type为支持的platform,本章节的01代码
                       host='192.168.137.201',  # 这个参数写成ip也可以
                       username='netdevops',
                       password='admin123!',
                       port=22,  # 可选参数, 默认是22端口，可以不写，在模拟环境可能会有端口映射，或者是使用Telnet等可以指定其他端口
                       # secret='admin123!',  # 选填，, 默认值是''，空字符串,这个是enable的密码,如果非空，则会尝试进入enable模式
                       )
    output = net_conn.send_command('show version')
    # 关闭连接 显式关闭
    net_conn.disconnect()
    print(output)

