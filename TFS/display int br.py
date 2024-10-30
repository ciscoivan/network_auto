import textfsm
from tabulate import tabulate

with open('display_interface_brief.template') as f, open('display_interface_brief') as output:
     reuslt = textfsm.TextFSM(f).ParseText(output.read())
     hed = textfsm.TextFSM(f).header
     print(tabulate(reuslt,headers=hed))