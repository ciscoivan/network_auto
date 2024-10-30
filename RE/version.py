import  re
line = 'VRP (R) software, Version 5.110 (S5700 V200R001C00)'
match =re.search('Version\s(\d.\d+)',line)
print(match.group(1))
#print(match)


line3 = '''Interface                         IP Address/Mask      Physical   Protocol  
LoopBack0                         8.8.8.8/24           up         up(s)     
MEth0/0/1                         unassigned           down       down      
NULL0                             unassigned           up         up(s)     
Vlanif1                           10.1.1.2/24          up         up  
  '''

host = re.search(r'(\d{1,3})\.\d{1,3}\.\d{1,3}\.\d{1,3}',line3)
print(host.group(1))

line4 = 'CPU utilization for five seconds: 1%: one minute: 1%: five minutes: 1%.'
matc = re.search('five\sminutes:\s(\d+%)',line4)
print(matc.group(1))

line5 = '''  Memory utilization statistics at 2022-05-14 10:39:08+00:00
 System Total Memory Is: 790626304 bytes
 Total Memory Used Is: 109466080 bytes
 Memory Using Percentage Is: 13%
'''
mem = re.search('Memory Using Percentage Is:\s(\d+%)',line5)
print(mem.group())