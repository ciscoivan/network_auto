# coding:utf-8

project = {'id': 1, 'project_name': 'ipad', 'price': 2200, 'count': 30}

project_title = list(project.keys())
print(project_title)
print(type(project_title))

print(project_title[0])
print(project_title[3])
print(project_title[2: 6])
project_title.append('user')
print(project_title)
