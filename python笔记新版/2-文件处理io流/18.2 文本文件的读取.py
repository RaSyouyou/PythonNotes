'''
读取文件如下有三个办法
1.read([size]) 读取size个字符 并作为结果返回。如果没有size参数默认读取所有
2.readline() 读取一行内容作为结果返回 读取到文件末尾
3.readlines() 文本文件中 每一行作为一个字符串存入列表中，返回该列表

'''

with open(r'read.txt','r') as f:
    str = f.read(10)
    print(str)
    list = f.readlines()

print(list)


