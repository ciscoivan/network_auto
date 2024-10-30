from multiprocessing import Pool

import pandas as pd
from netmiko import ConnectHandler


def get_batch_backup_dev_infos(filename='inventory.xlsx'):
    '''
    读取 Excel 表格加载网络设备基本信息和其配置备份的命令，结果返回一个元组的列表
    :param filename: 表格名称，默认值是 inventory.xlsx
    :return: [(<netmiko 连接设备所需基本信息的字典>,< 配置备份的命令 >)]
    示例：
    [({'host': '192.168.137.201',
       'device_type': 'huawei',
       'username': 'netdevops',
       'password': 'Admin123~',
       'secret': nan,
       'timeout': 180,
       'conn_timeout': 20},
       'display current-configuration'),
    ]
    '''
    # 读取并将表格加载成字典的列表
    df = pd.read_excel(filename)
    items = df.to_dict(orient='records')
    # 构建返回的结果，dev_infos 是一个元组的列表。
    dev_infos = []
    for i in items:
        # 取出配置备份的命令，并用 del 将其从字典中删除
        backup_cmd = i['backup_cmd']
        del i['backup_cmd']
        # 删除配置备份命令后的字典就是 netmiko 登录设备所需的信息
        dev = i
        dev_infos.append((dev, backup_cmd))
    return dev_infos


def network_device_backup(dev, cmd='display current-configuration'):
    """
    登录设备执行配置备份的命令，并将设备回显的配置写入一个 <设备 IP 或者 host>.txt 的文件中，编码格式 utf8
    :param dev: 设备的基础信息，类型字典，key 与创建 netmiko 所需的参数对应
    :param cmd: 要执行的配置备份的命令，默认是华为的 “display current-configuration”
    :return: None 不返回，只打印
    """
    with ConnectHandler(**dev) as conn:
        conn.enable()
        output = conn.send_command(command_string=cmd)
        file_name = '{}.txt'.format(dev['host'])
        with open(file_name, mode='w', encoding='utf8') as f:
            f.write(output)
            print('{} 执行备份成功\n'.format(dev['host']))


def batch_backup_by_pool(inventory_file='inventory.xlsx'):
    print("----批量配置备份开始----")

    # 创建进程池，进程数不宜过大，可以设置为CPU数量的整数倍
    pool = Pool(4)
    # 读取设备信息
    dev_infos = get_batch_backup_dev_infos(inventory_file)
    # 循环读取设备信息，放入进程池进行并行执行
    for dev_info in dev_infos:
        dev = dev_info[0]
        cmd = dev_info[1]
        # 使用非阻塞的方法，并发执行函数，每次传入不同的参数，起若干个进程。
        pool.apply_async(network_device_backup, args=(dev, cmd))
    # 关闭资源池，不再接受新的请求
    pool.close()
    # 阻塞主进程，等待资源池的所有子进程完成，再继续执行接下来的代码。
    pool.join()
    print('----全部任务执行完成----')


if __name__ == '__main__':
    batch_backup_by_pool()
