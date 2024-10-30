import traceback
from multiprocessing import Pool

import pandas as pd
from netmiko import ConnectHandler

# 各device_type对应的配置备份命令
INFO_COLLECT_INFOS = {
    'huawei': [{'name': 'version',
                'cmd': 'display version',
                'textfsm_file': 'huawei_version.textfsm'},
               {'name': 'interface_brief',
                'cmd': 'display interface brief',
                'textfsm_file': 'huawei_interface_brief.textfsm'}
               ],
    'cisco_ios': [{'name': 'version',
                   'cmd': 'show version',
                   'textfsm_file': 'ciso_ios_version.textfsm'}],
}


def get_batch_collect_dev_infos(filename='inventory.xlsx'):
    '''
    读取 Excel 表格加载网络设备基本信息和其配置备份的命令，设备登录信息的列表
    :param filename: 表格名称，默认值是 inventory.xlsx
    :return: 设备登录信息（字典）列表
    '''
    df = pd.read_excel(filename)
    devs = df.to_dict(orient='records')
    return devs


def network_device_info_collect(dev):
    """
    登录设备执行配置备份的命令，并将设备回显的配置写入一个 <设备IP>.txt 的文件中，编码格式 utf8
    :param dev: 设备的基础信息，字典类型，key 与创建 netmiko 所需的参数对应
    :return: None 不返回，只打印
    """
    try:
        with ConnectHandler(**dev) as conn:
            # 通过设备的device_type匹配要执行的配置备份命令
            collections = INFO_COLLECT_INFOS[dev['device_type']]
            writer = pd.ExcelWriter('{}.xlsx'.format(dev['host']))
            for collection in collections:
                cmd = collection['cmd']
                name = collection['name']
                textfsm_file = collection['textfsm_file']
                data = conn.send_command(command_string=cmd,
                                         use_textfsm=True,
                                         textfsm_template=textfsm_file)
                if isinstance(data, list):
                    df = pd.DataFrame(data)
                    df.to_excel(writer, sheet_name=name, index=False)
                    print('{}的{}巡检项巡检成功'.format(dev['host'], name))
                else:
                    print('{}的{}巡检项内容为空，请确认执行的命令和对应解析模板无误'.format(dev['host'], name))
            writer._save()
    except:
        print('{}的巡检项出现异常，请联系开发人员,错误堆栈如下：\n{}'.format(dev['host'], traceback.format_exc()))


def batch_info_collect(inventory_file='inventory.xlsx'):
    print("----批量信息巡检开始----")

    # 创建进程池，进程数不宜过大，可以设置为CPU数量的整数倍
    pool = Pool(4)
    # 读取设备信息
    dev_infos = get_batch_collect_dev_infos(inventory_file)
    # 循环读取设备信息，放入进程池进行并行执行
    for dev_info in dev_infos:
        # 使用非阻塞的方法，并发执行函数，每次传入不同的参数，起若干个进程。
        pool.apply_async(network_device_info_collect, args=(dev_info,))
    # 关闭资源池，不再接受新的请求
    pool.close()
    # 阻塞主进程，等待资源池的所有子进程完成，再继续执行接下来的代码。
    pool.join()
    print('----全部任务执行完成----')


if __name__ == '__main__':
    batch_info_collect()
