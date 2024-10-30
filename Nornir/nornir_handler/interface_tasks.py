# 需要安装pip install  nornir_table_inventory
from netdev_utils import CommonNetOps


def interfaces_colllect_task(task):
    net_connect = task.host.get_connection('netmiko', task.nornir.config)
    host_ops = CommonNetOps(conn_obj=net_connect)
    interfaces = host_ops.get_interfaces()
    return interfaces



if __name__ == '__ma  __':
    ...
