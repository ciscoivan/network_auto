# coding:utf-8

import re

url = 'https://www.imooc.com/'

result = re.search('(\w{3}\.\w+\.\w+)', url)
if result != None:
    print(result)
    print(result.groups())
    print(url[8: 21])

email = 'dewei@imooc.com'
result = re.findall('([a-zA-Z0-9]+@\w+\.[a-z]{3})', email)
print(result)

result = re.findall('(.*@.*\..*)', email)
print(result, '通配符匹配')


html = ('<div class="s-top-nav" style="display:none;">'\
        '</div><div class="s-center-box"></div>')

result = re.findall('style="(.*?)"', html)
print(result)

result = re.findall('<div class="(.*?)"', html)
print(result)





