from netmiko import ConnectHandler

import logging
import time
import re

logging.basicConfig(
    level=logging.WARN,
)


def get_dev_hostname_prompt_pattern(prompt):
    match = re.search(r'\w[\w\-]+\w', prompt)
    if match:
        hostname = match.group()
        expect_string = rf'{hostname}.*'
        return expect_string
    else:
        raise Exception(f'无法提取hostname in {prompt}')


if __name__ == '__main__':
    '''
   write_channel与read_channel
    '''
    dev = {
        'device_type': 'cisco_ios',
        'host': '192.168.137.201',
        'username': 'netdevops',
        'password': 'admin123!',
        'port': 22,  # optional, defaults to 22
        'secret': 'admin1234!',  # optional, defaults to ''
        # 保存到指定文件，完整的呈现整个登录和执行命令的过程
    }
    dev['session_log'] = f"{dev['host']}.log"
    timeout = 100
    loop_delay = 0.2
    end_prompt = '>'
    with  ConnectHandler(**dev) as net_conn:
        end_prompt = '>'
        net_conn.clear_buffer()

        net_conn.write_channel('ping 192.168.1.1 \n')
        loop = 0
        max_loops = timeout / loop_delay
        result = ''
        while loop < max_loops:

            output = net_conn.read_channel()

            time.sleep(loop_delay)
            if output:
                print(output)
                result += output
            if end_prompt in output:
                print('回显结束!')
                break
            loop += 1
        print(result)
