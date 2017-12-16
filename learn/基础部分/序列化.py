#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

# d = dict(name = 'Bob', age = 20, score = 88)

d = dict(name='Bob', age=20, score=88)
print(d['name'])
print(d.get('name'))

import pickle

# pickle.dumps(d) #序列化为二进制
f = open('../dump.txt', 'wb')
pickle.dump(d, f) #写进一个文件
f.close()

f = open('../dump.txt', 'rb')
print(pickle.load(f)) #读取序列化的文件
f.close()



#JSON 编码是utf-8
#如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
#JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下

import json 
print(json.dumps(d)) #序列化为一个为str, 内容就是标准的json

json_str = '{"name": "Bob", "age": 20, "score": 88}'
print(json.loads(json_str)) #把json字符串反序列化为对象


#JSON进阶
#class类对象的json
class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age 
		self.score = score

	def student2dict(std): #类方法 序列化
		return {
			'name' : std.name,
			'age' : std.age,
			'score' : std.score
		}
	def dict2student(d): #反序列化
		return Student(d['name'], d['age'], d['score'])
	
s = Student('lwj', 24, 60)
f1=open('../json_test.txt', 'w')
json.dump(s, f1, default=Student.student2dict)
f1.close()

str1 = json.dumps(s, default=Student.student2dict)
#偷懒方法, 每个类都默认有__dict__这个
str2 = json.dumps(s, default=lambda obj: obj.__dict__) 
print(str1)
print('str2 =',str2)
s1 = json.loads(str1, object_hook=Student.dict2student)
print(s1)

# 接口典范, 需要怎么样的格式, 就可以传入配置
obj = dict(name='小明', age=20)
s1 = json.dumps(obj, ensure_ascii=True)
print(s1)

