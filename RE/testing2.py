import  re

log3 = 'Sep 26 2021 23:11:02-08:00'

data1 = r'(\d\d:)\d\d:\d\d'

math = re.search(data1,log3)
print(math.group())
print(math.group(1))

log4 = 'MAC move detected, VlanId = 54, MacAddress = 0000-5e00-0136,'
data2 = r'\w\w\w\w-\w\w\w\w-\w\w\w\w'
math = re.search(data2,log4)
print(math.group())