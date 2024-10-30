from netmiko import ConnectHandler

import logging

logging.basicConfig(
    level=logging.DEBUG,
)

if __name__ == '__main__':
    '''
    配置三种方式，先写笔者最建议使用的是send_config_set
    传入command的list即可
    连接对象会自动进入config模式
    初学者在使用配置的时候需谨慎，推荐先使用send_command去采集信息，在慢慢掌握之后配置一些风险小的配置，小步慢走
    '''
    dev = {
        'device_type': 'cisco_ios',
        'host': '192.168.137.202',
        'username': 'netdevops',
        'password': 'admin123!',
        'port': 22,  # optional, defaults to 22
        'secret': 'admin1234!',  # optional, defaults to ''
        'session_log':'config_example.log'
        # 保存到指定文件，完整的呈现整个登录和执行命令的过程
    }
    # dev['session_log'] = f"{dev['host']}.log"
    with ConnectHandler(**dev) as net_conn:
    # 初学者建议执行以下两条命令，显示调用保证进入config模式
        net_conn.enable() # 进入特权模式，这个一定要写
        net_conn.config_mode() # 建议写一下，进入config模式
        configs = ['interface Ethernet0/2',
                    'description configed by netmiko']
        # 执行配置命令（一次性），执行完默认自动退出config模式
        output = net_conn.send_config_set(config_commands=configs)
        print('send_config_set::', output)
        # output = net_conn.commit() # 按需进行commit  和设备有关系
        output = net_conn.save_config()

        print('save_config::', output)


        #  # 以下代码演示的是通过文件推送配置
        # '''
        # 从指定文件读取配置的方式，将代码和实际配置内容解耦，也是非常推荐的一种方式，大家可以专注于配置的准备
        # 但此类配置不建议有交互
        # '''
        # net_conn.send_config_from_file(config_file='config.txt')
        # net_conn.save_config()
