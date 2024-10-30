import re
result = []
regex1 = r'(?P<ip>\d+\.\d+\.\d+\.\d+) +(?P<mac>\w+-\w+-\w+) +.* (?P<port>\S+)'
regex2 = r' + (?P<vlan>\d+)$'
with open('disp_arp.txt') as data:
    for line in data:
        # 如果为vlan字段，则追加到result的最后一个元素，然后解析下一行。
        match = re.search(regex2, line)
        if match:
            result[-1].update(match.groupdict())
            continue
        # 如果不为vlan字段，则正常查找arp表项。
        match = re.search(regex1,line)
        if match:
            result.append(match.groupdict())
#print(result)
# 补齐上面没有解析出vlan的，让解析更规整，没这个需求的话可以注释掉这一段代码。
for each_arp_record in result:
     if 'vlan' not in each_arp_record.keys():
         each_arp_record.update(({'vlan': '-'}))
#print(f'{len(result)} records on arp table :')
#print(result)
# 把结果打印出来。
for i, each_arp_record in enumerate(result, 1):   # (result, 1)中的1让i可以从1开始，而非从默认的0开始。
    print(f'\ndetails of arp table {i}:')
    for key in each_arp_record:
        # f字符串中的{key:10}，:10表示key的长度占位10，这样打印可以等宽，漂亮些。
        print(f'{key:10} : {each_arp_record[key]:10}')