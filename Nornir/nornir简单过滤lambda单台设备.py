from nornir import  InitNornir
from  nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
ro4 = nr.filter(filter_func=lambda host: host.name=='ro4')
result = ro4.run(netmiko_send_command,command_string='show ip arp')
print_result(result)

"""如果在生产网络环境下你记不住设备在host.yaml中对应的设备名称，但是你知道该设备的IP地址，那么在这里你也可以用sw4 = nr.filter(filter_func=lambda host: host.hostname=='192.168.2.14')，以IP地址来过滤该设备，这里就不演示了。
"""