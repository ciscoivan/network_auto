import re
from pprint import pprint
#集中正则表达式
filename = r'display_ospf_peer.txt'
result = {}

regex = (' Router ID: (?P<neighbor_id>\S+)\s+Address: (?P<neighbor_int_ip>\S+)'
         '|   DR: (?P<dr>\S+)  BDR: (?P<bdr>\S+)'
         '|   Neighbor is up for (?P<upfor>\S+)')


#'|或者的关系'

with open(filename) as f:
    for line in f:
        match = re.search(regex,line)
        if match:
            #print(match.groupdict()['neighbor_id'])
            if match.groupdict()['neighbor_id']:
               neighbor_id = match.groupdict()['neighbor_id']  #捕获邻居的neighbor_id
               result[neighbor_id] = {}

               for each in match.groupdict(): #处理同行的其他捕获信息如果neighbort_ini_ip
                   if match.groupdict()[each] and each != 'neighbor_id':
                      #print(each)
                      result[neighbor_id][each] = match.groupdict()[each] #取字典的值value

            else:

                #print(match.groupdict())
                for each in match.groupdict():
                    if match.groupdict()[each]:
                        #print(each)
                        result[neighbor_id][each] = match.groupdict()[each]#取字典的值value


print(result)
print('\n\n')
pprint(result)