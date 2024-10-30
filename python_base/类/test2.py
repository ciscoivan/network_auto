class Person():
    def __init__(self,name,age):
        self.name = name #实例属性
        self.age = age

    def showme(self):
        print("{}is {} years lod".format(self.name,self.age))

tom = Person('tom',20)
jerry = Person('jerry',30)

tom.showme() #实例。方法
jerry.showme()