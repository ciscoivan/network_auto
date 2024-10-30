from jinja2 import PackageLoader, Environment,FileSystemLoader
import pandas as pd
# env = Environment(loader=PackageLoader('python_project', 'templates'))  # 创建一个包加载器对象

if __name__ == '__main__':
    # 创建一个FileSystemLoader的文件加载器对象，参数searchpath，可以是一个，也可以是多个路径的字符串
    # 创建一个jinja2的核心组件Environment， 可以认为是一个加载了指定配置的jinja2引擎
    # 请大家参考同级目录templates内的ztp.j2模板，它将两个基本配置进行了组合
    env = Environment(loader=FileSystemLoader('templates'))

    # 通过文件路径获取模板对象
    template = env.get_template('cisco/ztp.j2')
    # 渲染
    dataframe = pd.read_excel('interfaces.xlsx')
    interfaces = dataframe.to_dict(orient='records')
    text = template.render(hostname='netdevops',interfaces=interfaces)

    print(text)