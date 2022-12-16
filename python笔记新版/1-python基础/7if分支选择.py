


print('==================1.单分支选择================')

a = 3.4
if a < 5.6 :
    print(a)

'''
b = input("请输入一个小于10的数字：")
if int(b) < 10:#input 的内容可能是数字和字符串 所以要强制转换b的类型
    print('输入的数字是：',b)
'''


print('==================2.分支选择详解================')
#条件表达式中值为False的情况如下：
# False,0,0.0,空值None,空序列毒想（空列表 空元组 空集合 空字典 空字符串），空range对象，空迭代对象
#其他情况均为True 故python所有的合法表达式都可以看作事条件表达式，甚至包括函数调用的表达式

if 3 :
    print('ok')


b = []
if not b:
    print('sss')


c = 10
if c :
    print('output')

#在条件表达式中不可以事用= 赋值符号  在判断时使用 ==



print('==================3.双分支选择================')

d = 3
if d >= 5:
    print(d)
else:
    print('d is less than 5')

#三元运算符
n = 20
print(n if n<20 else'数字太大')



print('==================4.多分支选择================')

score = int(input("骰子点数:"))


if score<=3:
    output = '小'
elif score<6:
    output='大'

print(output)