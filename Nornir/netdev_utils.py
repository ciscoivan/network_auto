from dev_manage import get_devs_in_list
from netmiko import Netmiko
import pandas as pd
import pendulum
from pathlib import Path

config_field_mapping = {
    'version':{'cisco_ios':{'cmd':'show version','field_name':'version'},
               'huawei':{'cmd':'display version','field_name':'version'},
               }
}

def mkdir(path):
    '''
    创建指定的文件夹
    :param path: 文件夹路径，字符串格式
    :return: True(新建成功) or False(文件夹已存在，新建失败)
    '''
    # 引入模块
    import os

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        # print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        # print(path + ' 目录已存在')
        return False


class CommonNetOps(object):
    description = '通用的网络工具类' \
                  '用于提取设备信息' \
                  '用于配置备份' \
                  '用于巡检设备'

    def __init__(self, dev_info=None, enable=True,conn_obj=None) -> None:
        '''
        初始化函数，创建到网络设备的连接
        :param dev_info: 创建netmiko 连接类所用到的参数，一律放入字典
        '''
        if dev_info:
            self.conn = conn = Netmiko(**dev)
            self.host = dev_info.get('host')
            self.ip = dev_info.get('ip')
        elif conn_obj:
            self.conn = conn_obj
            self.host = self.conn.host
            self.ip = self.conn.host
        else:
            raise Exception('无法创建到设备的连接，请确认传入了dev_info或者conn_obj参数')
        if enable:
            self.conn.enable()
        self.dev_type = self.conn.dev_type


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn.is_alive():
            self.conn.disconnect()

    def get_version(self, cmd=None, textfsm_tmpl=None, fieldname=None):
        try:
            if not cmd or not fieldname:
                cmd = config_field_mapping['version'][self.dev_type]['cmd']
                fieldname = config_field_mapping['version'][self.dev_type]['field_name']
        except :
            raise Exception('暂时不支持此类型设备')


        output = self.conn.send_command(cmd, use_textfsm=True, textfsm_template=textfsm_tmpl if textfsm_tmpl else None)
        if output and isinstance(output, list):
            version = output[0][fieldname]
            return version
        else:
            raise Exception('无法提取版本号')

    def get_interfaces(self, cmd='show interface', textfsm_tmpl=None):
        output = self.conn.send_command(cmd, use_textfsm=True, textfsm_template=textfsm_tmpl if textfsm_tmpl else None)
        if output and isinstance(output, list):
            return output
        else:
            raise Exception('无法提取端口列表')

    # def set_interfaces(self,interfaces):
    #     config = jinja2_render(t,interfaces)
    #     self.conn.send_config_set(config)

    def backup(self, cmd='show running-config', filename=None, directory=None, dir_format=1):
        '''

        :param cmd:
        :param filename:
        :param directory:
        :param dir_format: 目录形式，1代表是日期 设备名 文件名
        :return:
        '''
        output = self.conn.send_command_timing(cmd)
        filename = filename if filename else 'config.txt'
        if dir_format == 1:
            if not directory:
                current_path = Path()
                date = pendulum.now().strftime(r'%Y%m%d')
                date_path = current_path / date
                host_path = date_path / self.host
                mkdir(str(date_path))
                mkdir(str(host_path))

            filename = host_path / filename
            with open(str(filename), mode='w', encoding='utf-8') as f:
                f.write(output)

        return str(filename)


if __name__ == '__main__':

    devs = get_devs_in_list()
    files = []

    # for dev in devs:
    #     version = None
    #     interfaces = None
    #     with CommonNetOps(dev) as net_ops:
    #         interfaces = net_ops.get_interfaces()
    #         version = net_ops.get_version(textfsm_tmpl='cisco_ios_version.textfsm')
    #         datas.append({
    #             'host': net_ops.host,
    #             'version': version,
    #             'interfaces': '\n'.join([i.get('interface') for i in interfaces])
    #         })
    #
    # df = pd.DataFrame(datas)
    # df.to_excel('巡检解析作业.xlsx', index=False)
    for dev in devs:
        with CommonNetOps(dev) as net_ops:
            bk_file = net_ops.backup()
            files.append(bk_file)
    print(files)
