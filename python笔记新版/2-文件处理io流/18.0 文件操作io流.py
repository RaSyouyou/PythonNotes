'''
1.文本文件：
    文本文件储存的是“字符”文本，默认为unicode字符集。可以使用记事本打开。
但是如word文档编辑的文件不是文本文件
2.二进制文件
    二进制文件把数据内容用“字节”进行存储，无法用记事本打开。必须用专用的
软件解码。常见的有 .mp4 .mp3 .jpg .doc

程序给解释器 解释器通过操作系统写入硬盘
'''
f = open(r'b.txt','w')#如果出现乱码要调整编码
#w 如果文件存在则重写新内容
#a 如果文件不纯在则创建，如果文件存在则在末尾增加内容
#r 读取
#b 二进制模式
#t 文本模式
#+ 更新磁盘文件
f.write('未经审视的人生是不值得过的')
f.close #一定要关闭流

try:
    f = open(f"exception_test.txt",'a')
    str = 'system is GO'
    f.write(str)
except BaseException as e:
    print(e)
finally:
    f.close()