import  re

int_line  = 'Route Port,The Maximum Transmit Unit is 1500'
math = re.search('The Maximum Transmit',int_line)

print(math.group())
log = 'Sep 26 2021 23:11:02-08:00 Layer3Switch-1 L2IFPPI/4/MFLPVLANALARM:OID 1.3.6.1.4.1.2011.5.25.160.3.7 MAC move detected, VlanId = 54, MacAddress = 0000-5e00-0136, Original-Port = GE0/0/1, Flapping port = GE0/0/2. Please check the network accessed to flapping port.'
log2 = 'VlanId = 54, MacAddress = 0000-5e00-0136, Original-Port = GE0/0/1, Flapping port = GE0/0/2. '

re_template = r'VlanId = (\d+), MacAddress = (\S+), Original-Port = (\S+), Flapping port = (\S+)\.'
match = re.search(re_template,log2)
print(match.group())
print(match.group(0))
print(match.group(1))
print(match.group(2))
print(match.group(3))
print(match.group(4))
print(match.groups())
