#数据类型
'''
1）python 中提供一个type()函数 用来查看变量数据类型
'''

#1.字符串类型
#1)基本字符串
user_name = 'gabe newell'
platform = 'steam'

print(user_name)
print(type(platform))
res = type(platform)
print(res)

#2)大字符串
article ='''
这是一篇很长的文章
'''
print(article)
print(type(article))

#3)引号嵌套
s = 'aka "elden ring"'
print(s)
s = "aka 'elden ring'"
print(s)
#  s= "aka "elden ring "" 嵌套的引号必须不一样
s = '视频"套"套"套娃"娃"娃"'
print(s)
s= "视频'套'套'套娃'娃'娃'"
print(s)



#2.数字类型
#1)int整数类型
integer00 = 430
integer01 = -430
print(integer00,type(integer00),integer01,type(integer01))
#2进制 16进制表示法
integer02 = b'00110101' #byte
integer03 = 0x10
print(integer02,type(integer02),integer03,type(integer03))
#2)float浮点类型
float00 = 2.7182
float01 = - 3.1415
print(float00,type(float00),float01,type(float01))
#3)复数类型
complex00 =  5+3j
print(complex00,type(complex00))

#3.boolean布尔类型
bool00 = True # python 中布尔类型值首字母大写
bool01 = False

