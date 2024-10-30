from openpyxl import Workbook

# 类实例化
wb = Workbook()

ws1 = wb.active
ws1.title = 'cisco'
data = [
    ["device_name", "device_ip", "vendor", "model", "sn", "os", "version", "update_time"],
    ['switch-01', "192.168.1.1", "cisco", 'WS-C3560G-24TS', "FOC00000000", "cisco_ios", "12.2(50)SE5", "1 weeks, 1 minutes" ],
    ['switch-02', "192.168.1.2", "cisco", 'WS-C3560G-24TS', "FOC00000000", "cisco_ios", "12.2(50)SE5", "1 weeks, 1 minutes" ],
    ['switch-03', "192.168.1.3", "cisco", 'WS-C3560G-24TS', "FOC00000000", "cisco_ios", "12.2(50)SE5", "1 weeks, 1 minutes" ],
        ]
for row in data:
    print(row)
    ws1.append(row)


wb.save('simple_excel.xlsx')