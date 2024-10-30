import  sys
import  textfsm
from  tabulate import  tabulate


with open('vlantemplate') as f , open('vlanoutput_from_cli') as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    result = re_table.ParseText(output.read())
    print(result)
    print('\n\n')
    print(tabulate(result,headers=header))
