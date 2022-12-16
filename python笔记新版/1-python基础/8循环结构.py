print('===================1.while循环==================')

num = 0
while num<= 10:
    print(num)
    num +=1 #至少应该包括改变条件的表达式的语句，是的循环趋于结束。否则就会变成死循环


#计算1-100数字的累加和

num = 1
sum = 0
while num<=100:
    sum = sum + num
    num +=1

print(sum)


print('===================2.for循环==================')
#for循环通常用于可迭代对象的遍历
#可迭代对象
#1 序列（字符串 列表 元组）
#2字典
#3迭代器对象
#4生成器函数


for i in (10,20,30):
    print(i*30)

for i in ('abcdefg'):
    print(i)


d= {'title':'dota2',
    'time played':6110,
    'synchronization':True,
    'aaaa':333,
    2.33:'键名甚至可以是浮点类型'
    }

for i in d:
    print(i)

for i in d.keys(): #遍历所有的keys
    print(i)

for i in d.values():
    print(i)

for i in d.items():
    print(i)

#range 对象帮助创建数字序列
#打印1-100之间的加和
s = 0
for i in range(1,101):
    s += i
print(s)

#打印1-100之间偶数的加和
se = 0
for i in range(2,101,2):
    se += i
print(se)
#打印1-100之间奇数的加和
so = 0
for i in range(1,101,2):
    so += i
print(so)

sum = 0
sum_odd=0
sum_even=0

for i in range(101):
    sum +=i
    if i % 2 ==0:
        sum_even += i
    else:
        sum_odd +=i
print('总价和为：{0}，奇数加和为{1}，偶数加和为{2}'.format(sum,sum_odd,sum_even))



print('===================2.嵌套循环==================')
for x in range(5):
    for y in range(5):
        print(x,end='\t')
    print()

#九九乘法表

for x in range(1,10):
    for y in range(1,x+1):
        print(y,'x',x,'=',x*y,end='\t')
    print()

#使用列表和字典储存表格的数据
#遍历和查询练习（打印工资高于一万五的数据）
r1 =dict(name='noone',age=22,salary=30000,city='beijinger')
r2 =dict(name='notwo',age=25,salary=20000,city='shanghai')
r3 =dict(name='nothree',age=18,salary=10000,city='chengdu')
r4 =dict(name='sumail',age=44,salary=60000,city='shenzhen')
tb=[r1,r2,r3,r4]

for x in tb:#查找名字里有no的人
    if 'no' in x.get('name'):
        print(x.get('name'))

for x in tb:#查找工资大于15000的人
    if float(x.get('salary'))>15000:
        print(x)
'''
print('==================3.break语句==================')
while True:
    a = input('请输入一个字符（输入Q或者q结束）:')
    if a.upper()=='Q':
        print('循环结束，退出')
        break#break立即结束该循环

    else:
        print(a)

print('==================4.continue语句==================')

empNum =0
salarySum = 0
salarys =[]

while True :
    s = input('input salarys(press "q"or "Q"to quit):')
    if s.upper=='Q':
        print('录入完成')
        break
    empNum+=1
    salarys.append(float(s))
    salarySum += float(s)

print(empNum)
print(salarySum)
print(salarys)

'''
print('==================5.zip()并行迭代=================')
names=('noone','notwo','nothree','sumail')
ages=(22,18,23,25)
jobs=('mid','off','carry',)

for n,a,j in zip(names,ages,jobs):
    print('{0}--{1}--{2}'.format(n,a,j))



