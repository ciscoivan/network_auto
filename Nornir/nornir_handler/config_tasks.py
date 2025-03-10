# 需要安装pip install  nornir_table_inventory
from netdev_utils import CommonNetOps


def back  _config_task(task):
    net_connect = task.host.get_connection('netmiko', task.nornir.config)
    host_ops = CommonNetOps(conn_obj=net_connect)
    bk_file = host_ops.backup()
    return bk_file


if __name__ == '__main__':
    ...
