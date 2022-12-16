
class Person:
    def __init__(self,name):
        self.name = name

    def __str__(self): #相当于重写了对象在计算机内的名字 本来他的名字是<__main__.Person object at 0x0000016FA6049400>
        return '名字是{0}'.format(self.name)


p = Person('ame')

print(p)