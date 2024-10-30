# coding:utf-8

students = [
    {'name': 'dewei', 'age': 33, 'sex': '男', 'id': 1, 'top': '174'},
    {'name': '小慕', 'age': 10, 'sex': '男', 'id': 2, 'top': '175'}
]

xiaoyun = {
    'name': 'xiaoyun',
    'age': 18,
    'sex': '女',
    'id': 3,
    'top': '160'
}

students.insert(0, xiaoyun)
print(students)

xiaogao = {
    'name': 'xiaogao',
    'age': 18,
    'sex': '男',
    'id': 4,
    'top': '188'
}
students.insert(3, None)
students.insert(4, None)
students.insert(5, None)

students.insert(6, xiaogao)
print(students)

xiaoming = {
    'name': 'xiaoming',
    'age': 19,
    'sex': '男',
    'id': 5,
    'top': '178'
}

students.insert(3, xiaoming)
print(students)
