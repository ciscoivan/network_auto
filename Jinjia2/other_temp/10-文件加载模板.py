from jinja2 import PackageLoader, Environment,FileSystemLoader

# env = Environment(loader=PackageLoader('python_project', 'templates'))  # 创建一个包加载器对象

if __name__ == '__main__':
    # 创建一个FileSystemLoader的文件加载器对象，参数searchpath，可以是一个，也可以是多个路径的字符串
    # 创建一个jinja2的核心组件Environment， 可以认为是一个加载了指定配置的jinja2引擎
    env = Environment(loader=FileSystemLoader('templates'))

    # 通过文件路径获取模板对象
    template = env.get_template('cisco/hostname.j2')
    # 渲染
    text = template.render(hostname='netdevops')

    print(text)