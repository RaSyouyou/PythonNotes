#字符串详解

#1.字符串的编码
'''
   python3默认16位的unicode编码
   使用ord()函数可以办字符串转换成unicode码
   使用chr()函数可以吧十进制数字转换成对应的字符
'''



#2.引号嵌套与大字符串
s = 'aka "elden ring"'
print(s)
s = "aka 'elden ring'"
print(s)
#  s= "aka "elden ring "" 嵌套的引号必须不一样
s = '视频"套"套"套娃"娃"娃"'
print(s)
s= "视频'套'套'套娃'娃'娃'"
print(s)



resume = '''
name="陈天宇"\ningameid="ctyzzz"\npos="solo"
'''
print(resume)



#3.空字符串和字符长度
#python允许空字符串存在并且可以用len()函数调查字符串长度
str00='kksc看看谁长'
str01=''
print(len(str00))
print(len(str01))



#4.转义字符
'''
"\+特殊字符"可以表示那以实现的字符表示
\(在行尾时) = 续行符
\\ =反斜杠
\' =单引号
\" =双引号
\b =退格
\n =换行
\t =横向制表符
\r =回车
'''
str02 ='第一行\n第二行\n第三行'
print(str02)
str03= 'i\'m inevitable'
print(str03)



#3.字符串拼接和复制 拼接需要两边同类型
str04 = 'under'+'ground'
str05 = '3'+'4'
print(str04)
print(str05)
str06='欧拉'*4
print(str06)


#4.不换行打印
#python中的print()函数最后自带换行符。可在()中输入,end=''自定义尾部
print('aaaa',end='b')
print('bbb',end='')
print('cccc',end='\n')



#5.从控制台读取字符串
'''
myname = input("请输入名字:")
print(myname)
'''



#6.str()函数
pi=3.14
e=2.72
print(str(pi)+str(e))
li = [str(pi),str(e)]
''.join(li)
print(''.join(li))



#7.使用[]提取字符
str07='i\'m here to help'
print(len(str07))
print(str07[0],str07[1],str07[3],str07[4])#字符串可以用[]提取但不可以用[]更改



#8replace()
str07_1 = str07.replace("h","s")#将所有的h改为s,并保存为一个新的字符串，不修改原本字符串
str07_2 = str07.replace("h","wwww")#将所有的h改为wwwww
str07_3 = str07.replace("here","not here")#可以整段更改
str07_4 = str07.replace(str07[4],"wwww")#貌似不能更改特定某一个位置的字符串
print(str07_1,type(str07_1))
print(str07_2)
print(str07_3)
print(str07_4)
print(str07)#但是本身并不发生改变






#9slice切片和逆序
str08="ez4ence"
print(str08[2])
print(str08[1:6])#包头不包尾
print(str08[1:6:2])#可以添加步长
print(str08[2:])#
print(str08[:6])#
print('==================带负数切片===============')
print(str08[-3:])#倒数三个
print(str08[-7:-3])#倒数第七个到倒数第四个
print(str08[::-1])#倒序且步长为1
print(str08[::-2])#倒序且步长为2
#9.e 打印出ex文本中的所有s
ex = "sxt"*5
#9.1
print(ex[::3])
#9.2
for i in range(len(ex)-1):
    if ex[i] == 's':
        print(ex[i],end='')
print("\n")



#10.split()分割 与 join()合并
#10.1 split()
str09 = 'to be ,,,,,,, or not to be'
print(str09.split(),
      type(str09.split()))
     #split()可以基于指定分割符将字符串分割成多个子字符串(储存到列表中)。
     #如果不指定分割符，则默认为空白字符(换行符/空格/制表符)。
     #v.split(x) 其中v为分割对象 通常为文本 括号中的x 可以译作以x分割v
print(str09.split(','))
#10.2 join()
varl = ['s','c','cc']
print(''.join(varl))#join() 与split()正好相反，将分割的元素拼接起来，
                    # join()括号中只能又一个变量所以一般用于列表
                    #在大项目中.join()函数的程序运行时间速度快于+
print('*'.join(varl))#'x'.join(v)同上 译作 以x为媒介拼接v



#11字符串主流机制和字符串比较
#在以前的python中对于符合标识符规则的字符串会启用字符串驻留机制
#在现在的python中即使不符合标识符规则的字符串，只要值相同也会启用同样的地址保存。
x = 'w_33'
y = 'w_33'
print(x is y)

x1 = 'w33#$%^&'
y1 = 'w33#$%^&'
print(id(x1))
print(id(y1))
print(x1 is y1)

print()
print()


#12字符串常用方法汇总
#12.1
str12 = '''您会收到这封自动产生的邮件，是由于有人在125.80.187.47（CN）试图通过网页或
移动设备登录您的帐户，且提供了正确的帐户名称与密码。Steam 令牌验证码是完成登录所必需的
。没有人能够不访问这封电子邮件就访问您的帐户。
如果您未曾尝试登录，那么请更改您的 Steam 密码，并考虑更改您的电子邮件密码，以确保您的帐户
安全。'''
print(len(str12))
print(str12.startswith('您会'))#返回是否以该指定字符串开头的布尔值
print(str12.endswith('安全。'))#返回是否以该指定字符串结尾的布尔值
print(str12.find('帐户'))#返回该指定子字符串第一次出现的位置
print(str12.rfind('帐户'))#返回该指定子字符串最后一次出现的位置
print(str12.count('帐户'))#返回该指定子字符串的词频
print('  midlaner '.strip())#去掉首尾的指定子字符串
print('_mid_laner_'.strip('_'))
print('_mid_laner_'.lstrip('_'))#去掉首部的指定子字符串
print('_mid_laner_'.rstrip('_'))#去掉尾部的指定子字符串



#13字符串格式化format()基本用法
str13 = 'name:{0:5}，address:{1:5}'
s13_1 = str13.format('Sherlock Holmes','221B,Baker Street')
str13_2 ='曲目:{title},作者:{author}'
s13_2 = str13_2.format(author = '刘花',title ='好汉歌')
print(s13_1)
print(s13_2)
#13.1填充与对齐
str13_3 = "余额:{0:.2f}"
s13_3 = str13_3.format(3.14159)
print(s13_3)




#14可变字符串 在python中子字符串属于不可变对象 不支持原地修改
#如果需要修改其中的值，只能创建新的字符串对象。
#使用io.StringIO对象或arry模块。
import io
str14 = "Hello passenger, welcome to take our taxi"
sio = io.StringIO(str14)
print(sio.getvalue())
sio.seek(6)
sio.write('aaaaa')
#print(sio.seek(8))
#print(sio.write('aaaaa'))
print(sio.getvalue())


ss = 'aaaa'



print(ss)
print(ss[0])


