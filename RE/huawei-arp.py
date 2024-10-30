from openpyxl import load_workbook
import  re


line = '172.29.50.150   4c1f-ccb4-5157            I -  Vlanif41'
match = re.search('(?P<ip>\d+\.\d+\.\d+\.\d+) +(?P<mac>\w+-\w+-\w+) +.* (?P<port>\S+)', line)
print(match.groups())
print(match.groupdict())
line = 'Vlanif1          192.168.11.11/24     up         up'
c = re.search('\w+\s+[\d.]+/\d+\s+\w+\s+\w+',line)

print(c.group())
print(c.group(0))

result = []

regex1 = r'(?P<ip>\d+\.\d+\.\d+\.\d+) +(?P<mac>\w+-\w+-\w+) +.* (?P<port>\S+)'
regex2 = r' + (?P<vlan>\d+)$'
with open('arp.txt') as data:
    for line in data:
        # 如果为vlan字段，则追加到result的最后一个元素，然后解析下一行。
        match = re.search(regex2, line)
        if match:
            result[-1].update((match.groupdict()))
            continue

        # 如果不为vlan字段，则正常查找arp表项。
        match = re.search(regex1, line)
        if match:
            result.append(match.groupdict())

print(result)
for i, each_arp_record in enumerate(result, 1):   # (result, 1)中的1让i可以从1开始，而非从默认的0开始。
    print(f'\ndetails of arp table {i}:')
    for key in each_arp_record:
        # f字符串中的{key:10}，:10表示key的长度占位10，这样打印可以等宽，漂亮些。
        print(key,each_arp_record[key])