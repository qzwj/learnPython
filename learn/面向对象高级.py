#!/usr/bin/env python3
# -*- coding:utf-8 -*-

print('---------------------普通的---------------------')

class Student(object):
    def set_color(self, color):
    	self.color = color
    #pass 类定义了方法和变量就不能用pass了


s = Student()
s.name = 'lwj'

def set_age(self, age):
	self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s) #给实例绑定方法, 但是只能这个实例使用
s.set_age(25)
print(s.age)

def set_score(self, score):
	self.score = score
Student.set_score = set_score

s.set_score(199)
print('score =', s.score)
s.set_score(99)
print('score =', s.score)
#通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现
s.set_color('red')
print('color =', s.color)
s.set_color('blue')
print('color =', s.color)

print('---------------------slots---------------------')
class Person(object):
	# pass
	__slots__ = ('name', 'age') #只允许这个类添加tuple里的属性

ming = Person()
ming.name = 'ming'
ming.age = 18
# ming.red = 'red' #报错
print('name =', ming.name)

# 子类如果同样要限制变量, 也要定义 slots, 如果只定义子类, 不定义父类, 也不会起作用
class Man(Person):
	__slots__ = ('job')
	pass

m1 = Man()
m1.job = 'it'
print(m1.job)



