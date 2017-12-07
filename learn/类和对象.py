#!/usr/bin/env python3
# -*- coding:utf-8 -*-

print('--------------类和对象-------------')
class Student(object): #object 继承object
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


print('--------------访问限制-------------')
class Car(object):
	def __init__(self, name, age):
		self.__name = name  #__name 隐藏外部使用的权限,  本质上是改为了 _Car__name, 但是不建议这么访问
		self.__age = age #__XX__ 这个是关键字变量, 外部可以访问
	def get_name(self):  # _XX 也是私有变量, 不建议随意访问
		return self.__name
	def set_name(self, name):
		self.__name = name
	def get_age(self):
		return self.__age
	def set_age(self, age):
		self.__age = age

car = Car('BMW', 1)
print('car.name =', car.get_name())
print('car.age =', car.get_age())



print('--------------继承, 多态-------------')

class Animal(object):
	def run(self):
		print('Animal is running ...')

class Dog(Animal):
	def run(self):
		print('Dog is running ...')

class Cat(Animal):
	def run(self):
		print('Cat is running ...')

class Timer(object):
	def run(self):
		print('Timer is running ...')

def run_twice(s):
	s.run()
	s.run()

run_twice(Animal()) #像鸭子模型
run_twice(Dog())
run_twice(Cat())
run_twice(Timer()) #类鸭子模型, 走起路来像鸭子, 没有继承指定的父类, 只是有了这个方法, 就可以执行
print(isinstance(Dog(), Animal))
print(isinstance(Timer(), Animal))



print('--------------获取对象信息-------------')
import types
# type()
print('type(123) =', type(123))
print('type(dog) =', type(Dog())) #判断 原生的类型, 不能判断父类
print('type(str) =', type('str'))
print('type(abc) =', type(abs)) #函数
print('type(run_twice) =', type(run_twice))
print(type(123) == int)
print(type('123') == type(123))
print(type(run_twice) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x*x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType )


#isinstance() 比较常用, 还可以判断子类
print(isinstance('123', str)) 
print(isinstance([1,2,3], (list,tuple)))
print(isinstance((1,2,3), (list,tuple)))


#dir() 获取一个对象所有的属性和方法, 不记得的方法的时候可以看一下

print(dir([]))

#getattr() setattr() hasattr()
class MyObject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x
obj = MyObject()
if hasattr(obj, 'x'):
	print('obj 有属性 x')
if hasattr(obj, 'y'):
	print('obj 有属性 y')
else:
	setattr(obj, 'y', 20)

print(getattr(obj, 'y'))
print(obj.y) 
# 试图获取不存在的 属性会报错, 所以这个用在我们不知道对象有什么属性的时候, 知道了就直接用


def readImage(fp):
	if hasattr(fp, 'read'):
		return readData(fp)
	return None
#假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。
#请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。


print('--------------实例属性和类属性-------------')

class Image(object):
	path = '/User/wjl/Desktop/1.png' #类属性

image = Image()
print(image.path)
image.path = '123' #新增加一个同名实例属性, 优先级高
print(image.path) 
del image.path
print(image.path)