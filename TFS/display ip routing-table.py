import textfsm
from tabulate import tabulate

with open('display ip routing-table.template') as f, open('display ip routing-table') as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    result = re_table.ParseText(output.read())
    print(tabulate(result, headers=header))