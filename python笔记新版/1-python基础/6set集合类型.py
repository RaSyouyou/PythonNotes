#集合类型
'''
-set集合是一个 无序且元素不重复的 集合的数据类型
-set集合使用中括号或者set()函数
'''
#1.集合的定义
vars = {1,2,3,'a','b',True}
vars00 = {1,2,3,'a','b',True,1}#集合中重复的元素将算作为一个元素

vars01 = set('12345')#使用set()函数定义时需要传入字符串
vars02 = set('12344555')#set()函数中重复的元素将算作为一个元素
vars03 = set('')#set()函数可以创建空集合


print(vars,type(vars))
print(vars00)
print(vars01)
print(vars02)

a = input()
print(type(a))

s = 'strkakak'
for i in s:
    print(i)