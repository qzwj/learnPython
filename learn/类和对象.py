#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Student(object):
	pass

bart = Student()
bart.name = 'lwj'  #感觉有点类似js的对象
bart.age = 25
print('name =', bart.name, ',age =', bart.age)

#ming = Student()
#print('name =', ming.name) #上面对象的变量不影响下面的, 下面的对象仍然没有这个name变量

class Person(object):
	def __init__(self, name, age):
		self.name = name #self 是初始化好的空对象, 外面调用时可以省略, 可以直接给一个对象初始化有2个变量
		self.age = age
	def print_info(self):
		print('name =',self.name, ',age =', self.age)
	def get_grade(self):
		if self.age < 18:
			print('未成年')
		elif self.age < 30:
			print('青年')
		elif self.age < 50:
			print('壮年')
		else:
			print('老年')

hong = Person('xiaohong', 18)
hong.print_info()
hong.get_grade()