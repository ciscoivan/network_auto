import xlrd

execl = xlrd.open_workbook('1_study.xlsx')
print(execl)

book = execl.sheet_by_name('学生手册')
print(book)

book = execl.sheet_by_index(0)
print(book.name)


print(book.nrows) #行
print(book.ncols) #列

for i in book.get_rows(): #读取每行的内容
    for g in i:
        print(g.value)

for i in book.get_rows(): #读取每行的内容
    contant = []  #定义空的列表
    for j in i :  #循环去vale的值写入列表
        contant.append(j.value)
    print(contant)