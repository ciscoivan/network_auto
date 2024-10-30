import re
e = 0
g = []
a = []
c = r'Ping failure！ \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'  #正则匹配ip地址
f = open("ping1.txt",'r',encoding='utf8')
for  line in f.readlines():
      a.append(line.strip())

for i in a:
  b = re.findall(c,i)
  if b == g:
      continue
  else:
      print(b)
      e = e+1
print("统计失败地址个数",e)


