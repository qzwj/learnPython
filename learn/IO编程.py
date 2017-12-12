#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#计算需要cpu, 数据的交换需要 磁盘和网络等, 这些需要用到IO
#请求网页,输出,  网页打开,输入

#input 输入, 流入数据, 反馈数据
#output 输出, 流出数据,请求数据
#cpu和内存的速度太快, 外设的输入输出太慢, 导致了不匹配, 所有有同步和异步之分. 
#同步设计简单, 异步复杂(回调, 轮询等)

# try:
# 	f = open('../test.txt', 'r') #r表示读取
# 	print(f.read())
# finally:
# 	if f:
# 		f.close() #一定要关闭文件

#with语句可以简化上面的写法
with open('../test.txt', 'r') as f:
	print(f.read(1))  #read(size) 读取多少个字节的内容
	print(f.readline())
	# print(f.readlines())
	for line in f.readlines():
		print(line.strip()) #去掉结尾的'\n'


#file-like Object
#像open函数返回的这个有read()方法的对象, 在Python中都叫file-like object, 除了这个,还有字节流, 网络流, 自定义流等,不要求继承, 只要像鸭子, 有这个read()方法就可以
#StringIO 就是在内存中创建的file-like Object, 常用作临时缓冲


#二进制
# with open('../test.jpg', 'rb') as fb: #rb是二进制
# 	print(fb.read())


#字符编码, 或者有错误可以忽略
# with open('../test.txt', 'r', encoding='utf-8', errors='ignore') as f1:
# 	print(f1.read())


#写文件
# with open('../w_test.txt', 'w') as fw: #w表示写
# 	fw.write('hello, write')





#StringIO 是在内存中读写str
#很多的时候, 数据读写不一定是文件, 也可以是在内存中读写

from io import StringIO
#写
f1 = StringIO()
f1.write('hello')
f1.write('  ')
f1.write('wolrd!')
print(f1.getvalue())

#读
# f2 = StringIO('Hello!\nHi!\nGoodbye!')
# while True:
# 	s = f2.readline()
# 	if s == '':
# 		break
# 	print(s.strip())

#BytesIO 操作二进制
from io import BytesIO
f3 = BytesIO()
f3.write('中文'.encode('utf-8')) #写入的是bytes
print(f3.getvalue())

f4 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f4.read()
# f4.seek(0) #移动位置
print(f4.tell()) #tell看位置
print(f4.getvalue())


#操作文件和目录
import os 
print(os.name) #系统的类型
print(os.uname()) #获取系统的详细信息



# #环境变量
# print(os.environ) #系统定义的环境变量,全部在其中
# print(os.environ.get('PATH')) #获取环境变量中的值
print(os.environ.get('x', 'default'))


#操作目录
print(os.path.abspath('.')) #查看当前目录的绝对路径

#拼接连个路径,跨操作系统
path = os.path.join('/Users/wjl/Desktop/github/learnPython/learn', 'testdir')
print(path)
os.mkdir('./testdir') #创建目录 我在这个地方都是用的相对路径
os.rmdir('./testdir') #删除目录

#拆分路径
path1 = os.path.split('../test.txt') #得到目录和文件名的tuple
print(path1)
print(os.path.splitext('../test.txt')) #得到文件名 和扩展名
# os.rename('../test.txt', '../test1.txt') #重命名
# os.remove('../test.txt')  #删除文件

#文件复制不是由系统系统调用, 可以用上面的流完成,很多代码
#shutil模块提供了copyfile()可以看做os的补充

#列出当前目录的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
#列出所有的py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
print(os.listdir('./'))

# for p in os.listdir('.'):
# 	print(p) //路径


def foundFile(s, path = '.'):
    for p in os.listdir(path):
        tmp = os.path.join(os.path.abspath(path), p)
        if os.path.isfile(tmp):
            if os.path.splitext(p)[0].find(s) != -1:
                print(os.path.join(os.path.abspath(path),p))
        if os.path.isdir(tmp):
            foundFile(s,tmp)
foundFile('io')





