from jinja2 import PackageLoader, Environment, FileSystemLoader
import pandas as pd
import re

# 过滤器简单理解是可以对渲染进的变量进行二次加工的函数，比如格式化时间，或者是格式化端口（下例）
INTF_MAPPING = {
    'eth': 'Ethernet',
    'Eth': 'Ethernet',
}


def interface_name_filter(name):
    intf_re = re.compile('(.+?)(\d+[\d/]*)')
    match = intf_re.match(name)
    if match:
        intf_type = match.group(1)
        intf_no = match.group(2)
        intf_type = INTF_MAPPING.get(intf_type, intf_type)
        return f'{intf_type}{intf_no}'
    return name


if __name__ == '__main__':
    # 测试过滤器
    interface_name_filter('eth1/1')

    env = Environment(loader=FileSystemLoader('templates'))
    env.filters['interface_name_format'] = interface_name_filter

    # 通过文件路径获取模板对象
    template = env.get_template('cisco/ztp_4_filter.j2')
    # 渲染
    dataframe = pd.read_excel('interfaces.xlsx')
    interfaces = dataframe.to_dict(orient='records')
    text = template.render(hostname='netdevops', interfaces=interfaces)

    print(text)
