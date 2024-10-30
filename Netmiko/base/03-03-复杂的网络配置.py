from netmiko import ConnectHandler, Netmiko

import logging
import re


# 进行debug，方便调试
# logging.basicConfig(
#     level=logging.DEBUG,
# )

def get_dev_hostname(prompt):
    match = re.search(r'\w[\w\-]+\w', prompt)
    if match:
        return match.group()
    else:
        raise Exception(f'无法提取hostname in {prompt}')


if __name__ == '__main__':
    """
    以下是一种比较python风格的书写方式，字典前加 ** 将字段以k1 = v1, k2 = v2的方式在函数里自动展开
    with 上下文管理 可以非常优雅的处理与设备连接断开(离开with的代码逻辑块后，Python会自动帮我们把netmiko的连接disconnect)
    import logging
    logging.basicConfig(
    level=logging.DEBUG,
    )
    开启debug模式，会详细的输出相关的netmiko执行情况，方便排障
    'session_log'可以将执行的结果完整的记录下来，包含了netmiko帮助我们进行的相关操作，也可以用于排障，查询一下为什么命令执行失败了
    """
    # # 将设备信息放入到字典中 可以让代码更加整洁

    dev = {
        'device_type': 'cisco_ios',
        'host': '192.168.137.201',
        'username': 'netdevops',
        'password': 'admin123!',
        'port': 22,  # optional, defaults to 22
        'secret': 'admin1234!',  # optional, defaults to ''
        'session_log': 'netdevops_201.log',  # 保存到指定文件，完整的呈现整个登录和执行命令的过程
        # 'session_log_record_writes':True, # 在channel中收发的内容均记录到log
        'session_log_file_mode': 'write',  # write 或者是append 重写或者追加
        'conn_timeout': 5,  # ssh登录设备的超时时间，默认5秒，如果设备的网络情况并不好，建议调大此数据，我们可以调小此数据用于演示
        'timeout': 100  # 简单理解为执行一条命令并等待回显的时间，默认100，如果是show running或者interface 回显时间特别长的可以调大此参数
    }
    # 如果log想以某种规律命名，可以修正一下 f-string 或者format函数
    # dev['session_log'] = f"{dev['host']}.log"
    # dev['session_log'] = "{x}.log".format(x=dev['host'])



    # # 使用send_command expect_string参数 实现enable
    with Netmiko(**dev) as net_conn:
        prompt = net_conn.find_prompt()

        hostname = get_dev_hostname(prompt)
        expect_string = rf'{hostname}.*'
        output = net_conn.send_command('enable',expect_string=r'assword:')
        print(output)
        output = net_conn.send_command('admin1234!',cmd_verify=False,expect_string=expect_string)
        print(output)
        output = net_conn.send_command('show runn')
        print(output)

    # # 使用 send_command_timing 发送命令，无需等待回显，超时自动下发下一条命令，在一些特殊情况下，实现一些特殊的需求，比如enable，不建议用于推送配置
    # with Netmiko(**dev) as net_conn:
    #     # net_conn.enable()
    #     output = net_conn.send_command_timing('enable')
    #     print(output)
    #     output = net_conn.send_command_timing('admin1234!')
    #     print(output)
    #     output = net_conn.find_prompt()
    #     print(output)




    # # 使用send_command expect_string参数 实现enable和配置端口
    # with Netmiko(**dev) as net_conn:
    #     prompt = net_conn.find_prompt()
    #
    #     hostname = get_dev_hostname(prompt)
    #     expect_string = rf'.*{hostname}.*'
    #     # net_conn.enable()
    #     output = net_conn.send_command('enable', expect_string=r'assword:')
    #     print(output)
    #     output = net_conn.send_command('admin1234!', cmd_verify=False, expect_string=expect_string)
    #     print(output)
    #     output = net_conn.send_command('config  terminal', expect_string=expect_string)
    #     print(output)
    #     output = net_conn.send_command('interface  eth0/1', expect_string=expect_string)
    #     print(output)
    #     output = net_conn.send_command('description config by send_command', expect_string=expect_string)
    #     print(output)

