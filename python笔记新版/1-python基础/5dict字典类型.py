#字典类型
'''
-字典是键值对的数据储存方式，其中键必须是数字活字符串类型，值可以式任意类型
-键与值之间用“：”链接 多个键值组之间用“，”连结
-键名不可改变故：1）可哈希运算的对象：整数，浮点，字符串，元组可作为键名
                2）列表，字典，集合这些可变对象不作为键名
-键名不能重复，值可以重复。若有键名重复，则会出现值的覆盖
-键值对中 键值皆不能为空,但可以为空值
'''
print('==================1.字典的定义================')
#通过{}创建字典
dict11 = {'title':'dota2',
        'time played':6110,
        'synchronization':True,
        'aaaa':333,
        2.33:'键名甚至可以是浮点类型'
        }

dict12 ={
         'title':'csgo',
         'title':'dota2',
         'title':'dark souls3',
         'title':'civilization',
         'title':'wallpaper engine',
        }#若有键名重复，则会出现值的覆盖

#使用dict()函数定义字典
dict13 = dict(name = 'sherlock holmes', address= '221B BakerStreet')
dict14 = dict([('name','sherlock holmes'), ('address  ','221B BakerStreet')])

#通过zip()创建字典对象
k = ['title','synchronization','time played']
v = ['dota2',True,6110]
print('11111',type(zip(k,v)))
dict15 = dict(zip(k,v))

#通过dict.fromkeys()方法创建字典
dict16 = dict.fromkeys(['first','second'])



print('==================2.字典的访问================')
print(dict11['title'])
print(dict11[2.33])
print(dict11['synchronization'])
print(dict12 ['title'])#若有键名重复，则会出现值的覆盖
print(dict15)
print(dict16)
print(dict11['title'])
'''
如果用dict[]的方式查询不存在的键名则会报错
print(dict11['script'])
Traceback (most recent call last):
  File "L:/python笔记/5dict字典类型.py", line 50, in <module>
    print(dict11['script'])
KeyError: 'script'
'''

#dict.get()方法访问
print(dict11.get('title'))
print(dict11.get('script'))# 用dict.get()方法依然可以获取返回值，且在访问不存在的键时会返回None不会报错

#dict.keys() dict.values() dict.items() 分别访问键，值,键值对(返回分别放在列表里)
print(dict11.keys())
print(dict11.values())
print(dict11.items())

#字典长度 和查询是否在字典里
print(len(dict11))
print('title' in dict11)
print('script' in dict11)



print('==================3.字典的添加与删改================')
dict11['telephone'] = '46-230-333'#添加
dict11['time played'] = '6233h'#同名键会覆盖值
print(dict11)
dict31 = {'name' : 's1mple','team' : 'navi' ,'age' : 23, 'nation' : 'Ukraine','gender':True,}
dict32 = {'team' : 'navi' ,'gender':True,'job':'csgo pro gammer',}
dict31.update(dict32)#写前面的主体也就是被覆盖的字典
#dict32.update(dict31)
print(dict31)
#print(dict32)

#删除与转换
#del()函数删除
del(dict31['team'],dict31['job'])
print(dict31)

#pop()方法将键所对应的值删除 并返回该值
k = dict31.pop('name')
print(dict31)
print(k)

#clear()方法删除所有信息
dict31.clear()
print(dict31)
dict32.clear()
print(dict32)



print('==================4.字典的序列解包================')
dict41={
    'name':'Pontiff_Sulyvhan',
    'nation':'Irithyll of the Boreal Valley',
    'gender':True
}

#默认解包会得到键名
x,y,z, =  dict41
print(x,'',y,'',z)

#通过values()方法解包会得到值
a,b,c = dict41.values()
print(a,'',b,'',c)

#通过items()获取键值对元组
q,o,p = dict41.items()
print(q,'',o,'',p)
print(q[0],'',o[0],'',p[1])



print('==================5.复杂表格数据存储================')
r1 = {'name':'Ashen_One','age':24 ,'salary':699,'city':'Lothric Castle',}
r2 = {'name':'Ashen_Two','age':21 ,'salary':666,'city':'Irithyll of the Boreal Valley',}
r3 = {'name':'Ashen_Three','age':69 ,'salary':233,'city':'Profaned Capital',}
r4 = {'name':'Ashen_Four','age':43 ,'salary':0,'city':'Cathedral Of the Deep',}

tb=[r1,r2,r3,r4]

print(tb[1].get('city'))
#打印所有城市
for i in range(len(tb)):
    print(tb[i].get('city'),end='\t')

print( )

#打印整个表格
t1,t2,t3,t4 = tb[1]
print(t1,t2,t3,t4)
for i in range(len(tb)):
    a,b,c,d = tb[i].values()
    print(a,b,c,d,)




rt = {(1,2,3):'Ashen_Four','age':43 ,'salary':0,'city':'Cathedral Of the Deep',}
print(rt[(1,2,3)])

