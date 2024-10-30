import  re

with open('disp_arp.txt') as data:
    for line in data:
        print(line.strip())


line = '172.29.50.150   4c1f-ccb4-5157            I -  Vlanif41'
match = re.search('(?P<ip>\d+\.\d+\.\d+\.\d+) +(?P<mac>\w+-\w+-\w+) +.* (?P<port>\S+)', line)
print(match.group())
print(match.groupdict())

line = '                                          41'
match = re.search(' + (?P<vlan>\d+)$', line)
print(match.group())