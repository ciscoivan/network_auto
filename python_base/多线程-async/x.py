from example import Course, Teacher, Student


def introduction(str):
    print("************************{}************************".format(str))


def prepare_course():
    course_dict = {
        "01": "网络爬虫",
        "02": "数据分析",
        "03": "人工智能",
        "04": "机器学习",
        "05": "云计算",
        "06": "大数据",
        "07": "图像识别",
        "08": "Web开发"
    }

    course_list = []

    for k, v in course_dict.items():
        course = Course(cno=k, name=v)
        # course_list.append({course.cno: course.name})
        course_list.append(course)

    return course_list


def create_teacher():
    teacher_name = ["杨教师", "贾教师", "谢福顺", "周勤", "黄国发", "李旭", "王朋", "张亮"]
    tno = ["T" + str(tno) for tno in range(8, 0, -1)]
    mp = [str(mp) for mp in range(13301122008, 13301122000, -1)]
    teacher = []

    while tno:
        t = Teacher(tno=tno.pop(), name=teacher_name.pop(), mp=mp.pop())
        # teacher.append([t.tno, t.name, t.mp])
        teacher.append(t)

    return teacher


def course_to_teacher():
    c_to_t = []
    Is_course = prepare_course()
    Is_teacher = create_teacher()
    Is_teacher.reverse()

    for each in Is_course:
        index_ = Is_course.index(each)
        teacher_name = Is_teacher[index_]
        result = each.binding(teacher=teacher_name)

        c_to_t.append(result)

    return c_to_t


def create_student():
    student_name = ["小亮", "小明", "李红", "小丽", "Jone", "小彤", "小K", "慕慕"]
    student_name.reverse()
    sno = [sno for sno in range(1008, 999, -1)]
    student = []

    for _student_name in student_name:
        Is_student = Student(sno=sno.pop(), name=_student_name)
        # student.append({Is_student.sno: Is_student.name})
        student.append(Is_student)

    return student


if __name__ == "__main__":
    course_to_teacher()
    create_student()
    introduction("慕课学院（1）班学生信息")
    result = course_to_teacher()
    result.reverse()

    for each in create_student():
        # each.add_course(course_info=result_c.pop())
        print(f"name:{each.name},s_number:{each.sno}")

    introduction("慕课学院（1）班选课结果")

    for each in create_student():
        each.add_course(course_info=result.pop())
        print(each.course_detail())