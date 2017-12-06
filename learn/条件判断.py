#!/usr/bin/env python3
a = input('请输入你的年龄:')
age = int(a)
if age > 18:
    print('你已经成年了')
else: 
    print('你还未成年')

score = 77
if score < 60:
    print('你没有及格')
elif score < 80:
    print('成绩良好')
else:
    print('成绩优秀')

b = 'lwj'
if b:
    print('非空即为真,你的名字是:',b)
else:
    print('为空的情况')

