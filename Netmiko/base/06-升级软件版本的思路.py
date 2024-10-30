import ping3
from netmiko import ConnectHandler, Netmiko

import logging
import re
import time


# 进行debug，方便调试
# logging.basicConfig(
#     level=logging.DEBUG,
# )

def get_dev_hostname_prompt_pattern(prompt):
    match = re.search(r'\w[\w\-]+\w', prompt)
    if match:
        hostname = match.group()
        expect_string = rf'{hostname}.*'
        return expect_string
    else:
        raise Exception(f'无法提取hostname in {prompt}')


'''
Python 2

# 采用默认端口（8000）建立HTTP服务
$ python -m SimpleHTTPServer
# 采用自定端口（8765）建立HTTP服务
$ python -m SimpleHTTPServer 8765
1
2
3
4
Python 3

# 采用默认端口（8000）建立HTTP服务
$ python -m http.server
# 采用自定端口（8765）建立HTTP服务
$ python -m http.server 8765

netdevops01#copy http: unix:   
Address or name of remote host [192.168.203.58]? 192.168.137.132:8000
Source filename [a.ios]? 
Destination filename [a.ios]? 
Accessing http://192.168.137.132:8000/a.ios...
Loading http://192.168.137.132:8000/a.ios 
0 bytes copied in 0.019 secs (0 bytes/sec)
netdevops01#



'''


class SwitchUpdater:

    def __init__(self, dev_in_netmiko):
        self.dev_in_netmiko = dev_in_netmiko
        self.conn = ConnectHandler(**dev_in_netmiko)
        self.ip = self.dev_in_netmiko['ip'] if 'ip' in self.dev_in_netmiko else self.dev_in_netmiko['host']
        self.hostname_prompt_pattern = get_dev_hostname_prompt_pattern(self.conn.find_prompt())
        self.conn.enable()

    def copy_file_from_http(self, source_file, http_server, dest_file=None, cmd='copy http: unix:'):
        dest_file = dest_file if dest_file else source_file
        file_exist = self.is_file_in_switch(dest_file)
        if file_exist:
            raise Exception('目标文件已存在')
        # self.conn.enable()
        output = f'{cmd}\n' + self.conn.send_command(cmd, expect_string=']?')
        output += f'{http_server}\n' + self.conn.send_command(http_server, expect_string=']?')
        output += f'{source_file}\n' + self.conn.send_command(source_file, expect_string=']?')
        output += f'{dest_file}\n' + self.conn.send_command(dest_file if dest_file else source_file,
                                                            expect_string=self.hostname_prompt_pattern)
        print(output)
        return self.is_file_in_switch(dest_file)

    def is_file_in_switch(self, file, cmd='dir flash:'):
        # self.conn.enable()
        output = self.conn.send_command(cmd)
        return file in output

    def update_version(self, cmd='boot system flash:cat9k_lite_iosxe.16.12.04.SPA.bin', timeout=180):
        try:
            # self.timeout = timeout
            # self.conn.config_mode()
            # self.conn.send_config_set(cmd)
            # self.conn.exit_enable_mode()
            # self.conn.send_command('write')
            self.conn.send_command('reload')
            loop = 0
            delay = 0.5
            max_loop = timeout / delay
            while loop < max_loop:
                time.sleep(delay)
                if self.conn.is_alive():
                    loop += 1
                else:
                    return True
            return False

        except Exception as e:
            import traceback
            traceback.print_exc()
            return False

    def check_dev_reboot(self, timeout=180):
        loop = 0
        delay = 0.5
        max_loop = timeout / delay
        while loop < max_loop:

            time.sleep(delay)
            if ping3.ping(self.ip):
                return True
            loop += 1
        return False

    def check_update_succes(self, target_version, reboot_timeout=180, show_version_cmd='show version'):
        reboot_success = self.check_dev_reboot(timeout=180)
        if reboot_success:
            self.conn = ConnectHandler(**self.dev_in_netmiko)
            self.check_version(cmd=show_version_cmd, target_version=target_version)

    def check_version(self, cmd, target_version='11'):
        version = self.conn.send_command(cmd, use_textfsm=True)
        print(version)
        return version == target_version

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.conn.disconnect()
        except:
            ...

    def __enter__(self):
        return self


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
    with SwitchUpdater(dev) as swith_updater:
        # success = swith_updater.copy_file_from_http(source_file='a.ios',
        #                                             http_server='192.168.137.132:8000',
        #                                             dest_file='o.ios',
        #                                             )
        # print(success)
        result = swith_updater.check_version('show version',target_version='11')
        print(result)
