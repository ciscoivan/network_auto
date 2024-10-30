from netmiko import  ConnectHandler
import re

import pandas as pd

from dev_manage import get_devs_in_df



def get_dev_interfaces(dev_info, cmd='show interface'):

    with ConnectHandler(**dev_info) as conn:
        datas = conn.send_command(cmd,use_textfsm=True,textfsm_template='2.textfsm')
        print(datas)

        df = pd.DataFrame(datas)
        df.to_excel('interfaces.xlsx',index=False)

        





if __name__ == '__main__':
    dev_info = {
        'device_type': 'cisco_ios',
        'host': '192.168.137.202',
        'username': 'netdevops',
        'password': 'admin123!',
        'port': 22,  # optional, defaults to 22
        'secret': 'admin1234!',  # optional, defaults to ''
        'session_log':'config_example.log'
        # 保存到指定文件，完整的呈现整个登录和执行命令的过程
    }
    get_dev_interfaces(dev_info)
    # version = get_dev_version(dev_info=dev_info)
    