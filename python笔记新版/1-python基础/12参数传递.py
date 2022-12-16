print('=================1.参数传递=================')

def printMax(a,b):
    if a>b:
        print(a,'is greater')
    else:
        print(b,'is greater')

printMax(12,31)

#参数的传递(可变对象)
#python中所有的赋值操作都是引用的赋值 所有参数的传递 都是引用传递不是值传递
b=[10,20]
def f(m):
    print('m:',id(m))
    m.append(30)

f(b)
print('b:',id(b))
print(b)

#参数的传递(不可变对象)
axx= 100
def f1(n):
    print('n',id(n))
    n= n+200
    print('n',id(n))
    print(n)
f1(axx)
print('axx:',id(axx))


#深浅拷贝
print('================2.浅拷贝========================')
#浅拷贝：不拷贝子对象的内容，只是拷贝对象的引用
import copy
a =[10,20,[5,6]]
b=copy.copy(a)
c =[10,20,[5,6]]

print('a:',a)
print('b:',b)
print('a:',id(a))
print('b:',id(b))
print('c:',id(c))

print('a0:',id(a[0]))
print('b0:',id(b[0]))
print('c0:',id(c[0]))

print('a1:',id(a[1]))
print('b1:',id(b[1]))
print('c1:',id(c[1]))

print('a2:',id(a[2]))
print('b2:',id(b[2]))
print('c2:',id(c[2]))

print('a20:',id(a[2][0]))
print('b20:',id(b[2][0]))
print('c20:',id(c[2][0]))

b.append(30)
b[2].append(7)
print('浅拷贝。。。')

print('a:',a)
print('b:',b)
#深拷贝：会连子对象的内存也会全部拷贝一份，对子对象的修改不会影响源对象

print('================3.深拷贝========================')

a =[10,20,[5,6]]
b=copy.deepcopy(a)

print('a:',a)
print('b:',b)
print('a:',id(a))
print('b:',id(b))
print('a:',id(a[2]))
print('b:',id(b[2]))

b.append(30)
b[2].append(7)
print('深拷贝。。。')

print('a:',a)
print('b:',b)


x0 = 54
y0 = 54
z0 = copy.deepcopy(x0)
print(id(x0),'\n',id(y0),'\n',id(z0))

x1 = [5,[1,2]]
y1 = [5,[1,2]]
z1 = copy.deepcopy(x1)

print(id(x1),'\n',id(y1),'\n',id(z1))

