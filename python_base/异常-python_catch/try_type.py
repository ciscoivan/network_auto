# coding:utf-8

class Test(object):
    pass

t = Test()
try:
    t.name
except AttributeError as e:
    print(e)

d = {'name': '小慕'}
try:
    d['age']
except KeyError as e:
    print('没有对应的键：', e)

l = [1, 2, 3]
try:
    l[5]
except IndexError as e:
    print(e)

name = 'dewei'
try:
    int(name)
except ValueError as e:
    print(e)

def test(a):
    return a

try:
    test()
except TypeError as e:
    print(e)






