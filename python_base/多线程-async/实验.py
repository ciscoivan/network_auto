import re


def had_number(data):
    result = re.findall('\d',data)
    print(result)
    if len(result) !=0:
        return True
    else:
        return False
def remove_number(data):
    result = re.findall('\D',data)
    print(result)
    return ''.join(result)

def statswith(sub,data):
    _sub = '\A%s' % sub
    result = re.findall(_sub,data)
    if len(result) != 0:
        return True
    return  False

def endswith(sub, data):
    _sub = '%s\Z' % sub
    print(_sub)
    result = re.findall(_sub, data)
    print(result)
    if len(result) != 0:
        return True
    else:
        return False


if __name__ == '__main__' :
    data = 'www.ciso.com am54156'
    result = had_number(data=data)
    print(result)
    result = remove_number(data=data)
    print(result)
    data = 'hello cisco i am liyang. \'s old'
    print(data)
    print(re.findall('\W',data))
    result = statswith('hel',data=data)
    print(result)