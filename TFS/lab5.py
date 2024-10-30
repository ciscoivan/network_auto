import sys
import textfsm
from tabulate import tabulate


with open('template2') as f, open('re/output_from_cli') as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    result = re_table.ParseText(output.read())
    print(tabulate(result, headers=header))
    print(result)
    #print(result[1][2])
