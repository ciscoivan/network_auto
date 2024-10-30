# coding:utf-8

def upper(str_data):
    new_str = ''
    try:
        new_str = str_data.upper()
    except Exception as e:
        print('程序出错了:{}'.format(e))
    return new_str

result = upper(1)
print('result:', result)

def test():
    try:
        print('123')
        1 / 0
        print('hello')
    except ZeroDivisionError as e:
        print(e)


test()

def test1():
    try:
        print('hello')
        print(name)
    except (ZeroDivisionError, NameError) as e:
        print(e)
        print(type(e))
        print(dir(e))
test1()
