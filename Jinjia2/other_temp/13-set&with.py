import jinja2
from jinja2 import PackageLoader, Environment,FileSystemLoader
env = Environment(loader=FileSystemLoader(''))
if __name__ == '__main__':
    """:
    在模板中, 可以使用set语句来定义变量
    {% set 变量名= 值 %} 定义的变量, 后面的代码都能够使用, 相当于python中的全局变量
    此变量值不会被覆盖
    """

    template = env.get_template('set.j2')
    # 渲染
    text = template.render()

    print(text)

    """
    with语句定义的变量只能够在 with语句块中使用, 一旦超过了代码块就不能使用
    endwith与其搭配 划定边界 边界内的变量不会被覆盖
    """
    template = env.get_template('with.j2')
    text = template.render()

    print(text)
