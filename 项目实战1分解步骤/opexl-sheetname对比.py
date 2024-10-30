import  openxel
from  openxel import load_workbook

wb = load_workbook('dev-info.xlsx')
wb2 =wb.worksheets[0]
print(wb2)
ws1 = wb[wb.sheetnames[0]]
print(ws1)