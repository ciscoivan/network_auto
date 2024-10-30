import sys
import  textfsm
from tabulate import  tabulate

with open('display_ip_int_br.template') as f , open('display_interface_ip_br') as output:
   result = textfsm.TextFSM(f).ParseText(output.read())
   print(tabulate(result))

