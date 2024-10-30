from nornir import InitNornir
from nornir_netmiko import netmiko_save_config, netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result
from nornir.core.filter import F

nr = InitNornir(config_file='config.yaml')
group1 = nr.filter(F(groups__contains='cisco_group1'))
group2 = nr.filter(F(groups__contains='huawei_group4'))

cisco_result = group1.run(netmiko_send_command, command_string='show ip int bri')
huawei_result1  = group2.run(netmiko_send_config, config_commands=['int loo0','ip address 8.8.8.8/32'])
huawei_result = group2.run(netmiko_save_config, cmd='save', confirm=True, confirm_response='y') # 华为交互式保存的解法

print_result(cisco_result)
print_result(huawei_result)