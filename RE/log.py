import re

regex = (r'VlanId = (\d+), '
         r'MacAddress = \S+, '
         r'Original-Port = (\S+), '
         r'Flapping port = (\S+)\.')

ports = set()

with open('log') as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            vlan = match.group(1)
            ports.add(match.group(2))
            ports.add(match.group(3))
print(ports)
print('Loop between ports {} in VLAN {}'.format(', '.join(ports), vlan))

"""
import re

regex = (r'.*VlanId = (\d+), '
         r'MacAddress = \S+, '
         r'Original-Port = (\S+), '
         r'Flapping port = (\S+)\.')

ports = set()

with open('log.txt') as f:
    result = re.findall(regex,f.read())
    for vlan,port1,port2 in result:
        ports.add(port1)
        ports.add(port2)
    
print('Loop between ports {} in VLAN {}'.format(', '.join(ports), vlan))



import re

regex = (r'.*VlanId = (\d+), '
         r'MacAddress = \S+, '
         r'Original-Port = (\S+), '
         r'Flapping port = (\S+)\.')

ports = set()

with open('log.txt') as f:
    for each_match in re.finditer(regex, f.read()):
        vlan = each_match.group(1)
        ports.add(each_match.group(2))
        ports.add(each_match.group(3))

print('Loop between ports {} in VLAN {}'.format(', '.join(ports), vlan))
"""