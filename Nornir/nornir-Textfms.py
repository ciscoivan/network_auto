from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
results = nr.run(netmiko_send_command, command_string='show  int summary',use_textfsm=True)
print_result(results)
