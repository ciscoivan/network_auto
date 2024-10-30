
class Person: #定义一个类对象
    """
      doc 文档字符串
    """
    x = 123 #类属性，类变量
    y = 'abc'
    def eat(self): #函数 方法  eat也是类属性指向函数
        print('fuck',__class__.__name__)


c = Person
print(c)
print(c.y)
print(c.__doc__)

d =  Person()  #实例化
print(d)
