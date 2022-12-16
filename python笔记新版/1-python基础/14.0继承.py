#python支持多继承
#成员继承：子类继承了父类出了构造方法之外的所有成员
#所有类继承Object类
# class off(sup1[sup2])

class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age  #继承中的私有属性

    def say_age(self):
        print('这个b今年{0}岁'.format(self.__age))#方法可以访问私有的属性

    def nameIntro(self):
        print('我是{0}'.format(self.name))


class Student(Person):

    def __init__(self,name,age,score):
        Person.__init__(self,name,age)#必须显示的调用父类初始化方法 不然解释器不会调用
                                      #参数数量必须和父类一致
        self.score = score#score是自己的属性所以需要定义

    def nameIntro(self,a):
        '''方法重写对父类方法进行修改'''
        print('参数a已经被传入，其值为{0}'.format(a))
        print('吾乃{0}'.format(self.name))


print(Student.mro())#类名.mro()函数查看该类对象继承了哪些类，顺序是继承列表从左至右
s = Student('GGNOOB',18,60)
print(s.name)
#print(s.age) 由于age属性是私有的 所以无法直接访问
print(s._Person__age)
s.say_age()#直接继承了父类除构造方法外的所有实例方法
s.nameIntro(3)

p = Person('Dingzhen',25)
p.nameIntro()

#

