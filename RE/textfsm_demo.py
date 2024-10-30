import sys
import textfsm
import csv
from tabulate import tabulate
from pprint import pprint

with open('template.txt') as f , open('disp.txt', encoding='utf-8') as output:
    read_table = textfsm.TextFSM(f)
    header = read_table.header
    result = read_table.ParseText(output.read())
    #pprint(result)
    print(tabulate(result, headers=header))
    #print(read_table)
