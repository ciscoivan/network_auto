
class Course(object):
    def __init__(self,c_number,c_name,teacher=None):
        self.c_number = c_number
        self.c_name = c_name
        self.teacher = teacher

    def binding(self,teacher):
        if teacher == None:
            return 0
        else:
            self.teacher = teacher
            return {"课程名称":self.c_name,"教师名称": teacher.t_name}



def prepare_course():
    dict1= {"01":"网络爬虫","02":"数据分析","03":"人工只能","04":"机器学习","05":"云计算","07":"图像识别","08":"web开发"}
    list = []
    for key,value in dict1.items():
        course  = key,value
        list.append(course)
    return  list

if __name__ == "__main__":
    c = prepare_course()
    print(c[1])