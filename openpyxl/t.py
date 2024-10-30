from jinja2 import FileSystemLoader, Environment
from openpyxl import load_workbook
from datetime import datetime
import os

wb = load_workbook('write.xlsx')
ws1 = wb[wb.sheetnames[0]]

rows_list = []

for row in ws1.rows:
    row_list = []
    for i in row:
        row_list.append(i.value)

    rows_list.append(row_list)
print(rows_list)
result = []

for i in range(len(rows_list) - 1):
    row_dict = {}
    for j in range(len(rows_list[0])):
         #print(rows_list[0])
         row_dict[rows_list[0][j]] = rows_list[i + 1][j]
         print(row_dict)