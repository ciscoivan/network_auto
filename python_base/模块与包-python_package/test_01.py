# coding:utf-8

import re

str_data = 'hello xiaomu, this is a good day!'
result = re.search('h([a-zA-Z])s', str_data)
print(result.groups())
