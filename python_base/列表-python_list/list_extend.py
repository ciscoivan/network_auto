# coding:utf-8

manhua = []
history = []
code = []

new_manhua = ('a', 'b', 'c')
new_history = ('中国历史', '日本历史', '韩国历史')
new_code = ('python', 'django', 'flask')

manhua.extend(new_manhua)
history.extend(new_history)
code.extend(new_code)

print(manhua, history, code)

history.extend(manhua)
del manhua
print(history)

test = []
test.extend(True)
print(test)
