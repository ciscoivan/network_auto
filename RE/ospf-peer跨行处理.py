import re
from  pprint import pprint

filename = r'display_ospf_peer.txt'
result = {}
with open(filename) as f:
    for line in f:
        if line.startswith(' Router ID: '):
            neighbor = re.search(' Router ID: (\S+)\s+Address: (\S+)',line)
            neighbor_id = neighbor.group(1)
            neighbor_ip = neighbor.group(2)
            result[neighbor_id] = {}
            result[neighbor_id]['neighbor_int_ip'] = neighbor_ip
        elif line.startswith('   DR: '):
             dr_bdr = re.search('   DR: (\S+)  BDR: (\S+)',line)
             dr = dr_bdr.group(1)
             result[neighbor_id]['dr'] = dr
             bdr = dr_bdr.group(2)
             result[neighbor_id]['bdr'] = bdr
        elif line.startswith('   Neighbor is up for '):
             upfor = re.search('   Neighbor is up for (\S+)',line).group(1)
             result[neighbor_id]['upfor'] = upfor
print(result)
print('\n\n')
pprint(result)