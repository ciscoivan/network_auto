from nornir import  InitNornir
from  nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
#ro4 = nr.filter(filter_func=lambda host: host.name=='ro4')
routers = ['ro1','ro2','ro3']
ro1_ro3=nr.filter(filter_func=lambda host: host.name in routers)
result = ro1_ro3.run(netmiko_send_command,command_string='show ip arp')
print_result(result)

"""
同样的原理，如果你想使用IP地址来过滤，只需要将代码稍作修改如下即可：
switches = ['192.168.2.11', '192.168.2.12', '192.168.2.13']
sw1_sw2_sw3 = nr.filter(filter_func=lambda host: host.hostname in switches)
"""