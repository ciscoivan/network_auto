import  re
a ='0200-4c4f-4f50 1 - - Eth0/0/10 dynamic 0/-'

reuslt = re.findall('\S+\s\d+\s+\S+\s+\S+\sEth\S+',a)
print(reuslt)