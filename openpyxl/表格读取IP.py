import paramiko
import time
from openpyxl import Workbook
from openpyxl import load_workbook as open



wb = open('simple_excel.xlsx', read_only=True)
ws1 = wb[wb.sheetnames[0]]

a = []
# 循环遍历行
for n in ws1.iter_rows(min_row=2,min_col=1, ):
    sep = {
        "device_type": n[0].value,
        "ip": n[1].value,
        "username": n[2].value,
        "password": n[3].value,
    }
    a.append(sep)




ws2 = wb[wb.sheetnames[1]]
command_list = []
for col in ws2['A2:A5']:
    for cell in col:
        command_list.append(cell.value)






for i in a:
     da = {
        "device_type": i["device_type"],
        "ip": i["ip"],
        "username": i["username"],
        "password": i["password"],
     }
     file_name =  da['ip']+'info.txt'
     print(file_name)
     conn = paramiko.SSHClient()
     conn.set_missing_host_key_policy(paramiko.AutoAddPolicy)
     conn.connect(hostname=da['ip'], username=da['username'], password=da['password'], look_for_keys=False, allow_agent=False)
     conn_new = conn.invoke_shell()
     conn_new.send("enable\n")
     time.sleep(1)
     conn_new.send("123.com\n")
     time.sleep(1)
     conn_new.send('term len 0\n')
     time.sleep(4)
     output1 = conn_new.recv(65535).decode('ASCII')
     print(output1)
     for command in command_list:
         conn_new.send(command)
         time.sleep(1)
         output2 = conn_new.recv(65535).decode('ASCII')
         print(output2)



     conn_new.close()




