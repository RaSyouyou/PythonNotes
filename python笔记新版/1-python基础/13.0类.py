print('======================1.类的创建================')
class Student:#首字母大写  type
    #类属性
    company ='valvesoftware'
    count = 0 #创建类属性

    #类方法
    @classmethod#类方法只属于类对象用来操作类属性 类方法和静态方法中不能调用实例属性
    def leifangfa(cls):
        print(cls.company)
        print(cls.count)
    #静态方法
    @staticmethod
    def func01(a,b):
        return a+b


    #构造函数（构造函数通常用来初始化实例对象的实例属）
    def __init__(self,name,score): #self 必须位于第一个参数 #构造方法无返回值
        self.name = name  #实例属性
        self.score = score
        self.a = 'a启动'
        Student.count +=1 #这里要更改类属性 用类名.类属性 反正不能用global 不知道为什么
    #析构函数
    def __del__(self):#一般不用重写
        print('销毁对象：{0}'.format(self))

    #实例方法
    def report_score(self):
        print('{0}的分数是:{1}'.format(self.name,self.score))

#创建通过类创建对象
s1=Student('cty',98)#类名() 等于直接调用构造函数
                    #s1=Student()等于调用了 __init__() 和 __new__()方法
s1.report_score()
print(type(s1))
print(type(Student))#创建的Student类中的对象属于Student类别  Student本身属于type类（或者说模具类）
Student.report_score(s1)#解释器的调用实际是这样的
print(s1.a)
s2 = Student('maybe',100)
s2.report_score()
print(s2.a)

s1.leifangfa()


#dir()方法查询类属性
'''
print(dir(s1))
for i in range(len(dir(s2))):
    if 'n' in dir(s2)[i]:
        print(dir(s2)[i])
'''
#print(dir(s2))


print(Student.count)
print(s1.count)
print(s2.count)

