#使用filter()配合F()来做高级过滤然后在F的前面加上一个波浪号~对其进行取非来过滤cisco_group2下的SW3和SW4
from nornir import  InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from  nornir.core.filter import F

nr = InitNornir(config_file="config.yaml")
group1 = nr.filter(F(groups__contains="cisco_group1"))
group2 = nr.filter(~F(groups__ontains="cisco_group1"))
result= group1.run(netmiko_send_command,command_string='sh ip int brief')
#result= group2.run(netmiko_send_command,command_string='sh ip int brief')

print_result(result)

"""这时你肯定会问：怎么取消过滤，一次性将4台交换机的show ip int brief全部打印出来呢？答案很简单，只需要将group1.run()或group2.run()替换成nr.run()就行了
results = nr.run(netmiko_send_command, command_string='sh ip int brief')
 print_result(results)"""