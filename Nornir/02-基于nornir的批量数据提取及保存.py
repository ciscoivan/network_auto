from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command
# 需要安装pip install  nornir_table_inventory
from nornir_handler.nornir_manager import get_nornir_onj_by_excel

from netdev_utils import CommonNetOps

def backup_config_task(task):
    net_connect = task.host.get_connection('netmiko', task.nornir.config)
    host_ops = CommonNetOps(conn_obj=net_connect)
    bk_file = host_ops.backup()
    print(bk_file)
    return bk_file


if __name__ == '__main__':
    nr = get_nornir_onj_by_excel('inventory2.xlsx')
    print(nr)
