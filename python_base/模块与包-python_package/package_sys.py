# coding:utf-8

import sys

command = sys.argv[1]
if command == 'modules':
    modules = sys.modules
    print(modules)
elif command == 'path':
    path = sys.path
    print(path)
elif command == 'encoding':
    code = sys.getdefaultencoding()
    print(code)
elif command == 'platform':
    print(sys.platform)
elif command == 'version':
    print(sys.version)
else:
    print('not command')


