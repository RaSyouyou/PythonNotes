#list列表类型
#0序章
#列表：用于储存任意数目，任意类型的数据集合
#特点1：列表大小可变，根据需要随时增加或缩小
#1.列表的创建
print('=========1.列表的创建========')
#列表用来表示一系列数据，例如: 需要记录一组数字或其他数据,使用，分隔数据
varlist = [192,168,0,1,'对的对的对的']
print(varlist,type(varlist))

#创建空的列表对象
list01 = []

#使用list()创建列表:可以将任何可迭代的数据转化成列表
list11 = list()
list12 = list('d o t a')
print(list12)



print('==========2.使用range()创建整数列表==========')
#range()可以帮助我们方便创建整数列表 range(start,end,step)
list21 = list(range(10))
print(list21)
list22 = list(range(3,20,2))
print(list22)
list23 = list(range(20,3,-1))
print(list23)
list21 = list(range(-12,-3,))
print(list21)
list21 = list(range(-12,5,2))
print(list21)
list21 = list(range(1,-20,-2))
print(list21)



print('=========3.循环创建列表===============')
list31 = [x*2 for x in range(5)]
print(list31)
list32 =  [x for x in range(100) if x%9 == 0]
print(list32)



print('=========4.列表的添加========')
#列表通过下标查询列表中的元素
#list.append()方法在后方添加一个元素
list41 = [20,40]
print(list41)
print(id(list41))
list41.append(80)
print(list41)
print(id(list41))#由于是append是原地扩展所以改变后地址不变

#加法操作
list42 = [2,4,6]
print(list42)
print(id(list42))
list42 = list42 + [8,10]
print(list42)
print(id(list42))#加法操作后拼接的列表相当于新建了一个对象故地址发生改变

#list.extend()可在后方添加一个列表
#extend添加得是列表中的元素而非列表对象本身
list43 = [100,200]
print(list43)
print(id(list43))
list43.extend([300,400,500])
print(list43)
print(id(list43))#与append不同，添加不止一个元素。但是也属于原地扩张故地址不变

#insert()插入元素
list44 = [1,2,3,4]
print(id(list44))
list44.insert(2,"插入部分")
print(list44)
print(id(list44))

#乘法扩展
list45 = ['ak',47]
list45 = list45*3
print(list45)



print('=========5.列表的删除===============')
#del list[]
list51 = [1,3,5,7,9]
print(id(list51))
del list51[2]
print(list51)
print(id(list51))#其本质是依次拷贝

#pop() pop()删除并返回指定位置元素，默认位最后一个
list52 = [2,4,6,8,10]
print(list52)
list53 = list52.pop()
print(list53)
print(list52)
list52.pop()
print(list52)
list52.pop(0)
print(list52)

#remove() 方法删除首次出现的指定元素 若是不存在则抛出异常
list54=['aaa','bbb','sss']
list54.remove('sss')
print(list54)

print('=========6列表的访问===============')
#查询元素与索引
list61 = ['sss',24,34,'aa','sss']
print(list61[2])
print(list61.index(24))
print(len(list61))
print(list61.count('sss'))
print('a' in list61)
print('aa' in list61)




print('=========7列表的切割========')
list74=['maybe','fy','yang','redpanda','paparazzi','chalice','ame','xnova','cty','super','emo',]
print(list74[2])
print(list74[1:6])#包头不包尾
print(list74[1:6:2])#可以添加步长
print(list74[2:])#
print(list74[:6])#
print('==================带负数切片===============')
print(list74[-3:])#倒数三个
print(list74[-7:-3])#倒数第七个到倒数第四个
print(list74[::-1])#倒序且步长为1
print(list74[::-2])#倒序且步长为2



print('=========8列表的排序========')
list81= [20,10,30,40,-50]
print(id(list81))
list81.sort()#升序排列
print(list81)
print(id(list81))
list81.sort(reverse=True)#降序排列
print(list81)
print(id(list81))

#随机打乱
import random
random.shuffle(list81)
print(list81)
print(id(list81))

#逆序排列
list82 = reversed(list81)



print('=========9二位列表==========')
list91 = [
    ['maybe',28000,'mid'],
    ['fy',19000,'support'],
    ['cty',24000,'mid'],
    ['ame',24000,'carry']
]

print(list91)

for r in range(4):
    for c in range(3):
        print(list91[r][c],end="\t")
    print()

