import re

if __name__ == '__main__':

    # 子串的提取 我们用"()"识别捕获串  形如(?P<变量名称>pattern)
    line = 'interface Ehternet1/5 is up'
    intf_pattern = r'interface\s+Ehternet(?P<slot>\d+)/(?P<index>\d+)'
    interface_match = re.match(intf_pattern, line)
    if interface_match:

        intf = interface_match.group(1)
        print('intf slot in groups(1):', intf)
        intf = interface_match.group(2)
        print('intf index in groups(1):', intf)
        intf = interface_match.group('slot')
        print('intf in group(\'slot\'):', intf)

        # 获取所有子串 groups()
        intf = interface_match.groups()
        print('intf in groups():', intf)

        # 获取所有子串的字典
        intf = interface_match.groupdict()
        print('intf in groupdict():', intf)
