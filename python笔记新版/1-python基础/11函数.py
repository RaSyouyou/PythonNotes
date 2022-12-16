print('=================1.函数的定义与调用==================')

def func01():
    print('*'*10)
    print('@'*10)

func01()


print('=================2.形参与实参==================')

def printMax(a,b):
    if a>b:
        print(a,'is greater')
    else:
        print(b,'is greater')

printMax(12,31)

#参数的传递(可变对象)
#python中所有的赋值操作都是引用的赋值
b=[10,20]
def f(m):
    print('m:',id(m))
    m.append(30)

f(b)
print('b:',id(b))
print(b)

#参数的传递(不可变对象)
axx= 100

print('axx:',id(axx))
def f1(n):
    print('n:',id(n))
    n= n+200
    print('n:',id(n))
    print(n)
f1(axx)
print('axx:',id(axx))



print('=================3.返回值==================')
#返回一个值
def my_avg(a,b):
    print(a,b)
    return (a+b)/2

print(my_avg(2,3))

#停止函数的执行

def func02():
    print('aaaa')
    print('bbbbb')
    return
    print('ccccc')

func02()#即使没有返回值也会停止
c =  func02()
print(c)


#函数体可直接执行且有return的函数
def func03(a):
    print('如果有语句，语句也会执行')
    return a


print(func03(2))

container = func03(3) #赋值时 也算调用了一次函数 所以回执行函数中的函数体
print(container)#但是在打印变量container只是接受了函数return的值所以只会打印return的值


print('=================4.内存分析==================')
def func04():
    print('sxtsxt')

func04()
k = func04
k()#wow!

print('=================5.变量的作用域==================')

a = 3
def func5():
    b = 4
    print(b*10)
    a=3000000000000000

func5()
print(a)#局部变量在函数中 与全局变量独立 局部变量只在函数体中有效 且函数体内无法直接调用全局变量

a1 = 3
def func5():
    b = 4
    print(b*10)
    global a1#如果需要调用全局变量需要global关键字
    a1 = 30000000000000


func5()
print(a1)



print('=================6.默认值参数，命名参数，可变参数=================')
#默认值参数：给参数赋值时可以不给默认值参数赋值。但是默认值参数一定写在后面，且被赋值时被覆盖
def moren(a,b,c=10,d=20):
    print(a,b,c,d)

moren(1,2)
moren(1,2,3)
moren(1,d=5,b=3)#在两个位置参数之间的命名参数后可以不按照位置一一对应，。


#可变参数
#*param 将多个参数收集到一个元组当中
#**param 将多个参数收集到一个字典当中
#可变参数在没有强制命名的操作下只能写在最后面
def kebian(a,b,*c):
    print(a,b,c)

kebian(1,2,1,2,3)


def kebian2(a,b,*c,d,e):
    print(a,b,c,d,e)

kebian2(1,2,1,2,3,e=100,d=10)


print('=================6.lambda表达式和匿名函数=================')
#定义简单函数 且默认表达式返回结果
#funcName=lambda p1,p2,p3 : formula   相当于
#def funcName(p1,p2,p3):
#    return formula
fx = lambda a,b,c:a+b+c
print(fx)
print(fx(2,3,4))

gx =[lambda a:a*2,lambda b:b*3 , lambda c:c*4]
print(gx[0](2),gx[1](4))



print('==================7.eval()函数=========================')
s = 'print("abcdefg")'
sv = 'print'
eval(s)
eval(sv)





print('==================8.递归调用=========================')
def reg01(n):
    print('reg01:',n)
    if n == 0:
        print('over')
    else:
        reg01(n-1)
    print('reg01**',n)

reg01(5)

#算阶乘

def factorial(n):
    if n ==1:
        return 1
    else:
        return n*factorial(n-1)

outcome=factorial(5)
print(outcome)


print('==================9.嵌套函数与nonlocal关键字=========================')


def outer():
    print('outer is go!')
    b=10

    def inner01():
        print('inner01 is go!')
        b = 20
        print('inner b:',b)

    inner01()
    print('outer b:',b)

outer()

print('-------------------------------')


def outer():
    print('outer is go!')
    b=10

    def inner01():
        print('inner01 is go!')
        nonlocal b
        b = 20
        print('inner b:',b)

    inner01()
    print('outer b:',b)

outer()



