'''
1.尽量见少循环内部不必要的计算
2.嵌套循环中，尽量减少内层循环的计算，尽可能向外提
3.局部变量查询较快，尽量使用局部变量
4.链接字符串 尽量使用join()而不是+
5.列表进行元素插入和删除，尽量再尾部操作
'''

import time

start = time.time()

for i in range(1000):
    result = []
    for m in range(10000):
        result.append(i*1000+m*100)

end = time.time()
print('耗时{0}'.format((end-start)))

print('==========================================')

start1 = time.time()
for i in range (1000):
    result = []
    c= i *1000
    for m in range(10000):
        result.append(c+m*100)

end1 = time.time()
print('耗时{0}'.format((end1-start1)))
