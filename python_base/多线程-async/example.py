# coding:utf-8

class Student(object):
    def __init__(self, sno, name, course=[]):
        self.sno = sno
        self.name = name
        if course is not None:
            self.course = course

    def course_detail(self):
        return "Name：{}, Selected:{}".format(self.name, self.course)

    def add_course(self, course_info):
        self.course.append(course_info)


class Teacher(object):
    def __init__(self, tno, name, mp):
        self.tno = tno
        self.name = name
        self.mp = mp


class Course(object):
    def __init__(self, cno, name, teacher=None):
        self.cno = cno
        self.name = name
        self.teacher = teacher

    def binding(self, teacher):
        if teacher is not None:
            self.teacher = teacher
            return {"课程名称": self.name, "教师名称": self.teacher.name}
        else:
            return ""