#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = 'A'
b = '中'
ord(a) #转为unicode编码
ord(b)
c = chr(77) #把unicode转为字符
d = chr(25991)
print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)



#python的字符编码在内存中是unicode,在网络上传输,或者保存到磁盘需要转为bytes的格式
str = 'ABC'
str1 = '中国'
bstr = str.encode('ascii')
bstr1 = str1.encode('utf-8')
print('str to bytes = ', bstr)
print('str1 to bytes = ', bstr1)
bbstr = bstr.decode('ascii')
bbstr1 = bstr1.decode('utf-8')
print('bytes bstr to str = ', bbstr)
print('bytes bbstr1 to str = ', bbstr1)
print('bstr1字节长度length = ', len(bstr1))
print('bbstr1字符长度lenght = ', len(bbstr1))


#多行字符串
#!/usr/bin/env python3
print(r'''wo\n
shi
shui
a''')
print('上面的是多行字符串的输出,为了好看')
print('在多行字符串中前面的符号前加r,可以忽略字符串中换行符')

#字符串的格式化
e = 'hello, %s' %'world'
print(e)
e1 = 'Hi, %s, you have $%d' %('lwj', 200000)
print(e1)
print('%2d-%03d' % (3, 1))
print('%.2f' % 3.1415926)
print('Age: %s. Gender: %s' % (25, True)) #不确定用什么都可以用%s
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)) #format没有前者简洁


ss = 'lwj'
sss = ss.replace('l', 'L')
print(sss)

