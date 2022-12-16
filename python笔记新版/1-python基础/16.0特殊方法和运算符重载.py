#Python的运算符实际上是通过调用对象的特殊方法来实现的

a = 20
b = 30
c = a+b
d = a.__add__(b)#每一个运算符都对应一个方法
print('c=',c)
print('d=',d)


class Person:
    def __init__(self,name,age):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Person):
            return '{0}--{1}'.format(self.name, other.name)
        else:
            return 'not the same type, can not add'

    def __mul__(self, other):
        if isinstance(other,int):
            return self.name*other
        else:
            return 'not the same type, can not add'
p1 = Person('cty',25)
p2 = Person('ame',24)

x = p1 + p2
print(x)

y = p1 *3
print(y)