import xlsxwriter
import xlrd

#exec = xlsxwriter.Workbook('write.xlsx')
#book = exec.add_worksheet('study')

#titel = ['姓名','性别','年轮','成绩','等级']

#for index,data in enumerate(titel): #0行的写入
  #  book.write(0,index,data)
#exec.close()

def read():
    result = []
    excel = xlrd.open_workbook('1_study.xlsx')
    book = excel.sheet_by_name('学生手册')
    for i in book.get_rows():
        content = []
        for j in i :
            content.append(j.value)
        result.append(content)
    return  result

def write(content):
    exec = xlsxwriter.Workbook('write.xlsx')
    book = exec.add_worksheet('study')
    for index ,data in enumerate(content):
        for sub_index , sub_data in enumerate(data):
            book.write(index,sub_index,sub_data)
    exec.close()



if __name__ == '__main__':
    result = read()
    print(result)
    write(result)