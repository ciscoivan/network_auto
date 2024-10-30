import  textfsm
from tabulate import tabulate

with open('display _ospf_peer.template') as f , open('display_ospf_peer') as output:
    result = textfsm.TextFSM(f).ParseText(output.read())
    heder = textfsm.TextFSM(f).header
    print(tabulate(result,headers=heder))
