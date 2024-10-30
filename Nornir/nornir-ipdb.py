"""学习如何使用ipdb来对基于JSON格式、有序的回显内容数据（使用ntc-templates模板后输出的数据格式）做验证，以便我们从中过滤，提取我们需要的内容和数据。"""
import ipdb
from  nornir import  InitNornir
from nornir_netmiko import  netmiko_send_command
from nornir_utils.plugins.functions import  print_result


nr = InitNornir(config_file="config.yaml")
output = nr.run(netmiko_send_command, command_string='show ip int br', use_textfsm=True)
print_result(output)
print(output)
ipdb.set_trace()

#print(output['ro1'].result[0]['intf'])
#output['ro1'].result