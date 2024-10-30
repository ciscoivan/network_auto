import re

if __name__ == '__main__':

    # 子串的提取 我们用"()"识别捕获串
    line = 'interface Ehternet1/5 is up , ok'
    intf_pattern = r'interface\s+Ehternet(\d+)/(\d+)\s+is\s+(\w+)'
    interface_match = re.match(intf_pattern, line)
    if interface_match:
        # 获取整体的匹配
        intf = interface_match.group()
        print('intf in group():', intf)

        # 同上，获取整体的匹配，提取整体的符合要求的字符串
        intf = interface_match.group(0)
        print('intf in group(0):', intf)

        # 获取指定index的子串 groups(index) 注意index不要越界
        intf = interface_match.group(1)
        print('intf slot in groups(1):', intf)

        status = interface_match.group(3)
        print('intf status in groups(3):', status)

        # 获取所有子串 groups()
        intf = interface_match.groups()
        print('intf in groups():', intf)

