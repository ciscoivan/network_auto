# coding:utf-8

default_dict = {'a': None, 'b': 1, 'c': 0, 'd': ''}

print('a' in default_dict)
print(bool(default_dict['a']))
print(bool(default_dict.get('a')))
print(bool(default_dict.get('b')))
print('f' in default_dict)
print('f' not in default_dict)


