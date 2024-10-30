import pandas as pd
import  netmiko
from netmiko import Netmiko

def get_devs_in_list(filename='inventory.xlsx'):
    df = pd.read_excel(filename)
    items = df.to_dict(orient='records')
    return items



def get_netmiko_conn(dev,enable=True):
    datas = []


    for dev in devs:
        version = None
        interfaces = None
        sn = None
        conn = Netmiko(**dev)
        if enable:
            conn.enable()
        output = conn.send_command('show version', use_textfsm=True, textfsm_template='1.textfsm')
        print(output)
        if output and isinstance(output, list):
            version = output[0]['version']
        else:
            print('{}的version解析无数据，请注意'.format(dev['host']))

        output = conn.send_command('show inventory',use_textfsm=True, textfsm_template='sn.textfsm')

        if output and isinstance(output, list):
            sn = output[0]['sn']
        else:
            print('{}的sn解析无数据，请注意'.format(dev['host']))

        output = conn.send_command('show interfaces', use_textfsm=True, textfsm_template='cisco_interface.template')
        if output and isinstance(output, list):
            interfaces = output
        else:
            print('{}的端口解析无数据，请注意'.format(dev['host']))
        close_nemiko_conn(conn)
        datas.append({
            'host': dev['host'],
            'version': version,
            'sn':sn,
            'interfaces': interfaces
        })
    df = pd.DataFrame(datas)
    df.to_excel('巡检解析作业.xlsx', index=False)




def close_nemiko_conn(conn):
    conn.disconnect()


if __name__ == '__main__':
    devs = get_devs_in_list()
    get_netmiko_conn(devs)
