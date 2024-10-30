"""（1）Nornir结合Textfsm，找出hosts.yaml设备中的trunk和access端口。（复习lab10内容）

（2）Nornir用description命令将trunk口，描述配置为：Trunk Port (Nornir)。

（3）Nornir用description命令将access口，描述配置为：Access Port to VLAN xxx (Nornir)。xxx为VLAN号。"""
from nornir import InitNornir
from nornir_netmiko import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result
from nornir.core.filter import F

nr = InitNornir(config_file="config.yaml")

group3 = nr.filter(F(groups__contains="cisco_group3"))

output = group3.run(netmiko_send_command, command_string='sh interface switchport', use_textfsm=True)
#print_result(output)

for switch in output.keys():
    for i in range(3):
        trunk_cmd = ['interface ' + output[switch].result[i]['interface'], 'description Trunk Port (Nornir)']
        access_cmd = ['interface ' + output[switch].result[i]['interface'], 'description Access Port to VLAN ' +
                      output[switch].result[i]['access_vlan'] + ' (Nornir)']
        if 'trunk' in output[switch].result[i]['mode']:
            group3.run(netmiko_send_config, config_commands=trunk_cmd)
        elif 'access' in output[switch].result[i]['mode']:
            group3.run(netmiko_send_config, config_commands=access_cmd)

results = group3.run(netmiko_send_command, command_string='sh interface description')
print_result(results)