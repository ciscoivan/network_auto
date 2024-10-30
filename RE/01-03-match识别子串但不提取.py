import re

if __name__ == '__main__':

    # 括号有时候有优先级的作用，比如多个或的的情况，我们需要用括号圈出来，枚举类型，只是为了识别，不想捕获
    # 对于只想识别，但是不捕获的子串，我们可以"?:"在头部实现以上
    line = 'interface Ehternet1/5 is up'
    intf_pattern = r'interface\s+Ehternet(?P<slot>\d+)/(?:\d+)'
    interface_match = re.match(intf_pattern, line)
    if interface_match:

        intf = interface_match.group(1)
        print('intf slot in groups(1):', intf)
        intf = interface_match.group('slot')
        print('intf in group(\'slot\'):', intf)

        # 获取所有子串 groups() 会发现只有一个子串
        intf = interface_match.groups()
        print('intf in groups():', intf)

        # 获取所有子串的字典

        intf = interface_match.groupdict()
        print('intf in groupdict():', intf)
