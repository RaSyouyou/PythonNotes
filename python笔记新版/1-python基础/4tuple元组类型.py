#tuple元组类型
#在定义多个数据时可以使用元组类型
#与列表不同元组中的元素不可以被改变
print('==============1.元组的定义=============')
#小括号创建
tuple11 = (1,2,3,'a','bilibili')
print(tuple11)
tuple12 = (20,)#元组如果只有一个元素，需要在后面加逗号
print(type(tuple12))

#tuple()函数创建
tuple13 =  tuple('ab c')
tuple14 =  tuple(range(3))
tuple15 =  tuple([2,3,4])
print(tuple13)
print(tuple14)
print(tuple15)

#tuple的元素不可以被改变，但是tuple中的可改变对象中的对象可以被改变，
ttest = (1,2,3,[5,6])
print(ttest)
print(id(ttest[3]))
print(id(ttest[3][1]))
print('更改后')
ttest[3][0] = [3,1,4,1,4]
print(ttest)
print(id(ttest[3]))
print(id(ttest[3][1]))




print('==============2.元素的访问============')
#tuple[]访问元素
tuple21 = ('ez',4,'ence')
print(tuple21[1])
print(tuple21[0])
#tuple21[2]= 33 元组元素不可被改变 TypeError: 'tuple' object does not support item assignment



print('==============3.元组的切割和排序============')
tuple31 = ('abcdefghijklmnopqrstuvwxyz')
print(tuple31[3:10])

#排序
tuple32 = tuple([42,52,222,3,1,0])
print(tuple32)
print(sorted(tuple32))#1. tuple 没有list的list.sort()方法 只能用内置函数sorted(tupleObj)排序
                      #2. 使用sorted函数无论传入的对象均返回列表对象




print('==============4.zip压缩=======================')
list41 =[1,23,41]
list42 =[0,4,2]
list43 =[0,0,3]

zip41 = zip(list41,list42,list43)
print(zip41)
print(list(zip41))



print('===============5.生成器创建元组==================')
tuple51 = (x*2 for x in range (5))
print(tuple51)
print(tuple(tuple51))
print(tuple(tuple51))#只能访问一次 再次需要时要再生成一次
tuple52 = (x*3 for x in range (5))
print(tuple52.__next__())
print(tuple52.__next__())
print(tuple52.__next__())
print(tuple52.__next__())
print(tuple52.__next__())
'''
print(tuple52.__next__())
Traceback (most recent call last):
  File "L:/python笔记/4tuple元组类型.py", line 65, in <module>
    print(tuple52.__next__())
StopIteration
'''






