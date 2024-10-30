import re
result = []
lin2 = 'Internet  192.168.100.10          0   0050.56bc.f302  ARPA   Vlan100'
ccc = r'(?P<protocol>\w+) +(?P<ip>\d+\.\d+\.\d+\.\d+) + (?P<time>\d+|-) +(?P<mac>\w+\.\w+\.\w+) +(?P<type>\w+) +(?P<port>\w+)'
e = re.search(ccc,lin2)
print(e.groupdict())

with open('carp.txt') as data:
    for line in data:

        match = re.search(ccc, line)
        if match:
            result.append(match.groupdict())
print(result)
for i, arp_record in enumerate(result, 1):
      print(f'\ncisco arp table {i}:')
      for key in arp_record:
        print(key,arp_record[key])