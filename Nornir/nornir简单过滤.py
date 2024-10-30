"""from nornir import InitNornir
nr = InitNornir(config_file='config.yaml')
print(nr.inventory.hosts)
print(nr.inventory.groups)
nr.inventory.hosts['sw1'].platform
nr.inventory.groups['cisco_group1'].platform
filter()的用法比F()更简单，它其中的参数即为我们hosts.yaml里面data下面的键名，这里我们过滤出4个交换机里面位置在Building 1里的交换机，也就是SW1和SW2，然后打印出它们输入show ip arp命令后的回显内容。
"""
from nornir  import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result


nr = InitNornir(config_file="config.yaml")
targets = nr.filter(building='1')
results = targets.run(netmiko_send_command, command_string='sh ip arp ')

print_result(results)

"""
这里你也可以用level来过滤，写成targets = nr.filter(level='1')或者targets = nr.filter(level='2')，这个就留给大家自行去尝试。
"""