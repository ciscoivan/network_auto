from netmiko import  ConnectHandler

import pandas as pd


def get_dev_version(dev_info, show_ver_cmd='show ip interface brief'):
    data = []
    with ConnectHandler(**dev_info) as conn:
        interface = conn.send_command(show_ver_cmd,use_textfsm=True,textfsm_template='cisco_interface.template')
    return interface


def get_dev_version4pd():
    f = []
    dev_info = pd.read_excel('inventory.xlsx')
    dev = dev_info.to_dict(orient='records')
    for i in range(0,2):
        dev_info_in_dict = {
            'host': dev[i]['host'],
            'username': dev[i]['username'],
            'password': dev[i]['password'],
            'device_type': dev[i]['device_type'],

        }
        f.append(dev_info_in_dict)
    return f

def data2excel(data,file_name,sheet_name):

    df = pd.DataFrame(data)
    print(df)
    df.to_excel(file_name, sheet_name=sheet_name, index=False)



if __name__ == '__main__':
    all_version = []
    c = get_dev_version4pd()
    for i in c:
        e = get_dev_version(i)
        all_version.extend(e)
    data2excel(data=all_version, file_name='interface.xlsx', sheet_name='face')