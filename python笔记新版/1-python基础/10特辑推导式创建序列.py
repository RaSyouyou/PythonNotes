print('==============1.列表推导式================')
print([x for x in range(1,5)])
print([x*2 for x in range(1,5)])
print([x*2 for x in range(1,20) if x%5==0])
#嵌套循环
cells = [(row,col)for row in range (1,10)for col in range(1,10)]
for cell in cells:
    print(cell)


print('==============2.字典推导式================')

my_text = 'Hi, i am gaben newell, i would like to take a moment to thank you for supporting PC gaming'
char_count ={c:my_text.count(c) for c in my_text}
print(char_count)
print('==============3.集合推导式================')
b = {x for x in range(1,100) if x %9 ==0}
print(b)
print('==============4.生成器推导式================')
gnt = (x for x in range(1,100)if x%9==0)
print(type(gnt))#生成器只能使用一次
print(tuple(gnt))
print(tuple(gnt))
for x in gnt:
    print(x)