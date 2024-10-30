import  openpyxl

wb = openpyxl.load_workbook("cosco.xlsx")
#得到表单的名字有哪些sheet,sheet2
#print(wb.sheetnames)


#创建一个表单
#mysheet = wb.create_sheet('ivan')
#print(mysheet)

#便利表单头
#for sheet in wb:
#    print(sheet.title)

ws = wb.active
#print(ws)
#print(ws['A3'].value)
c = ws['A1']
print('Row{}.Column{} is {}'.format(c.row,c.column,c.value))

print(ws.cell(row=2,column=3).value)