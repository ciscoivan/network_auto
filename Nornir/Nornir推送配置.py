from nornir import InitNornir
from nornir_netmiko import  netmiko_send_command,netmiko_send_config
from nornir_utils.plugins.functions import print_result,print_title

nr = InitNornir(config_file="config.yaml")


def config(cisco):
    cisco.run(task=netmiko_send_config, config_file='sendconfig/commands.cfg')
    cisco.run(task=netmiko_send_command, command_string='show ip int br')


print_title('正在部署中')
results = nr.run(task=config)

print_result(results)