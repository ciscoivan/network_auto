import sys
import textfsm
from tabulate import tabulate

with open('ip_routing_template') as f , open('ip_routing_output_from_cli') as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    result = re_table.ParseText(output.read())
    print(tabulate(result, headers=header))