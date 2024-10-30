# coding:utf-8

def test1():
    try:
        1 / 0
    except Exception as e:
        print(e)
    finally:
        return 'finally'

result = test1()
print(result)

def test2():
    try:
        1 / 0
    except Exception as e:
        print('111')
        return e
    finally:
        print('finally')

print('-----')
result = test2()
print(result)

def test3():
    try:
        print('try test 11')
        return 'try'
    except Exception as e:
        print('e')
    finally:
        print('finally test')

print('------')
result = test3()
print(result)

def test4():
    try:
        1 / 0
    except Exception as e:
        print('1')
        return e
    finally:
        print('2')
        return 'finally'

print('-----')
result = test4()
print(result)

def test5():
    try:
        print('1try')
        return 'try'
    except Exception as e:
        print('e')
    finally:
        print('2finally')
        return 'finally'

print('=====')
result = test5()
print(result)


def test6():
    try:
        print('try1')
        1 / 0
        print('try3')
    finally:
        return 'i am finally'

print('------')
result = test6()
print(result)