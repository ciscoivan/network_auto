from openpyxl import load_workbook as open
# 类示例化
wb = open('simple_excel.xlsx', read_only=True)

# 第一个工作表对象
ws1 = wb[wb.sheetnames[0]]
a = []
# 循环遍历行
for n in ws1.iter_rows(min_row=2,  min_col=1, ):
    sep = {
        "device_type": n[0].value,
        "ip": n[1].value,
        "username": n[2].value,
        "password": n[3].value,
    }
    a.append(sep)

print(sep)

for i in a:
     da = {
        "device_type": i["device_type"],
        "ip": i["ip"],
        "username": i["username"],
        "password": i["password"],
         }

     print(da)

ws2 = wb[wb.sheetnames[1]]
command_list = []
for col in ws2['A2:A5']:
    for cell in col:
        command_list.append(cell.value)

print(command_list)