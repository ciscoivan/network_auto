import pandas

#读取表格使用read_excel方法
pdr = pandas.read_excel('123.xls', sheet_name='Sheet1')

resdic={}
for index,row in pdr.iterrows():
	s = {'IP地址':row['ip'],'账号名':row['用户名'],'密码':row['密码']}
	resdic[row['ip']]=s

print(resdic)

#写表格使用到DataFrame方法
df = pandas.DataFrame(columns=['IP地址','账号名','密码'])
pdWriter = pandas.ExcelWriter('输出文件.xls')

for key,val in resdic.items():
	df=df.append(val,ignore_index=True)

#使用to_excel方法将数据写入到表格
df.to_excel(pdWriter,index=None)

#保存
pdWriter.save()