import sys
import textfsm
from tabulate import tabulate


with open('display_int_br_template') as f , open('display_int_br_output_from_cli') as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    result = re_table.ParseText(output.read())
    print(result)
    print(tabulate(result,headers=header))