class Employee:

    __company = 'valvesoftware'
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def __work(self):
        print('workwork!')
        print('偷偷告诉你这个b年龄是：{0}'.format(self.__age))#私有属性在类中私有的方法是可以被访问的
        print(self.__company)

e = Employee('cty',25)
print(e.name)
#print(e.age)#age私有后无法正常访问
print(e._Employee__age)#属性私有后 转为 _类名__属性

#print(e.work())
e._Employee__work()
print(e._Employee__company)

print('========property==============')

class Emp:
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self,salary):
        if 1000<salary<50000:
            self.__salary = salary
        else:
            print('输入错误')



emp1 = Emp('sccc',30000)
print(emp1.get_salary())
emp1.set_salary(-2000)
print(emp1.get_salary())
print('========property==============')
#@property装饰器的用法


class Emp2:
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary

    @property#加入后只能访问不能改值 用方法访问私有属性 再把方法当成属性使用
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,salary):
        if 1000<salary<50000:
            self.__salary = salary
        else:
            print('输入错误')

emp2 = Emp2('zhou',12000)

print(emp2.salary)
emp2.salary = 11500
print(emp2.salary)
print(emp2._Emp2__salary)
