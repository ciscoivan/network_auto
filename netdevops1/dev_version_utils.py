from netmiko import  ConnectHandler
import re

import pandas as pd

from dev_manage import get_devs_in_df



def get_dev_version(dev_info, show_ver_cmd='show version',version_pattern=r'Version (\S+)\('):

    with ConnectHandler(**dev_info) as conn:
        version = conn.send_command(show_ver_cmd,use_textfsm=True,textfsm_template='1.textfsm')
        if isinstance(version,list):
            return version[0]['version']
        raise Exception('err textfsm')

def get_dev_version4pd(dev_info):
    dev_info_in_dict = {
        'host':dev_info['host'],
        'username':dev_info['username'],
        'password':dev_info['password'],
        'device_type':dev_info['device_type'],
        # 'host':dev_info['host'],
    }

    return get_dev_version(dev_info_in_dict)

        

def data2excel(data,file_name,sheet_name=0):

    df = pd.DataFrame(data)
    df.to_excel(file_name, sheet_name=sheet_name, index=False)

    return 'success'


def check_devs_version(filename='inventory,xlsx'):
    devs_df = get_devs_in_df()

    devs_df['version'] = devs_df.apply(get_dev_version4pd,axis=1)

    devs_df.to_excel('version_check.xlsx', sheet_name='version', index=False)


if __name__ == '__main__':
    # dev_info = {
    #     'device_type': 'cisco_ios',
    #     'host': '192.168.137.202',
    #     'username': 'netdevops',
    #     'password': 'admin123!',
    #     'port': 22,  # optional, defaults to 22
    #     'secret': 'admin1234!',  # optional, defaults to ''
    #     'session_log':'config_example.log'
    #     # 保存到指定文件，完整的呈现整个登录和执行命令的过程
    # }

    # version = get_dev_version(dev_info=dev_info)
    # version_data = [{'ip':dev_info['host'],'version':version}]
    # result = data2excel(data=version_data,file_name='version.xlsx',sheet_name='version')
    # print(result)
    check_devs_version()