'''
读取文件如下有三个办法
1.read([size]) 读取size个字符 并作为结果返回。如果没有size参数默认读取所有
2.readline() 读取一行内容作为结果返回 读取到文件末尾
3.readlines() 文本文件中 每一行作为一个字符串存入列表中，返回该列表

'''
#改写序列并写入文件
seq = ['第一名成绩为','第二名成绩为','第三名成绩为','第四名成绩为']

enu_seq = enumerate(seq)

print(seq)
print(enu_seq)
print(list(enu_seq))

rewrite_seq = [temp.rstrip() + ' #'+ str(index) for index , temp in enumerate(seq)]
print(rewrite_seq)