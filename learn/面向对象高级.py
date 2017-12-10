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


print('---------------------property---------------------')

class Car(object):
	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, value):
		self._name = value

	@property
	def age(self):
		return self._age

	@age.setter
	def age(self, value):
		# if value > 8:
		# 	raise ValueError('此车已可以报废')
		# elif value < 0:
		# 	raise ValueError('玩具车,遥控车')
		self._age = value

car = Car()
car.name = 'aodi'
car.age = 10
print(car.name)



print('---------------------多重继承---------------------')
class Animal(object):
	pass
#哺育
class Mammal(Animal):
	pass
class Bird(Animal):
	pass
class RunableMixIn(object):
	pass
class FlyableMixIn(object):
	pass
class Dog(Mammal, RunableMixIn): #同时继承多个父类, 实现方法
	pass


print('---------------------定制类---------------------')
class Job(object):
	def __init__(self, name):
		self.name = name
	def __str__(self): #类似 java的toString和 oc的description
		return 'Job object (name : %s)' % self.name
	__repr__ = __str__ #repr和str的代码是一致的, repr是开发调试的,直接输入变量, 不用print就可以打印变量的信息
job = Job('IT')
print(job)


# __iter__() 为该类定制for..in循环, 该方法返回一个迭代对象,  __next__()方法拿到循环的下一个值
# __getitem__ 上面的虽然和list有点像, 但是不能取下标, 实现这个定制就可以
class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1
	def __iter__(self):
		return self #实例本身就是迭代对象
	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 100000:
			raise StopIteration()
		return self.a
	def __getitem__(self, n):
		if isinstance(n, int): #n是索引, 就是取下标
			a, b = 1, 1
			for x in range(n):
				a, b = b, a+b
			return a
		elif isinstance(n, slice): #n 是切片对象
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a+b
			return L

for n in Fib():
	print(n)
f = Fib()
print(f[0])
print(f[0:5])
print(f[:10])

#上面的也没有对负数进行处理, 所以, 要正确实现一个__getitem__() 还是需要做很多工作的
# 此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
# 总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口




# __getattr__ 正常情况下, 当我们调用类的方法或属性时, 如果不存在, 就会报错.

class Dog(object):
	def __init__(self):
		self.name = 'ak'
	def __getattr__(self, attr):
		if attr == 'age':
			return 2
		elif attr == 'food':
			return lambda : 'meat' #返回函数也是可以的
		return AttributeError('\'Dog\' object has no attribute \'%s\'' % attr)
d1 = Dog()
print(d1.name)
print(d1.age)
print(d1.like) #默认没有定义就是None, 如果没有定义上面的AttributeError
print(d1.food())

# 这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
# 这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。
class Chain(object):
	def __init__(self, path=''):
		self._path = path
	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))
	def __str__(self):
		return self._path
	__repr__ = __str__

print(Chain().status.user.timeline.list) #链式调用, 很厉害, 找不到属性就到getattr方法
# print(Chain().users('michael').repos)



# __call__ ,实现了这个方法, 可以调用对象本身, 像调用函数那样
class Animal(object):
	def __init__(self, name):
		self.name = name
	def __call__(self):
		print('my name is %s.' % self.name)
a = Animal('xiao')
a()

#这样我们容易混淆变量是函数还是对象, 因为他们都可以调用 能被调用的就是一个Callable对象
print(callable(Student()))
print(callable(Animal('ss')))
print(callable(max))
print(callable([1,2,3]))
print(callable(None))
print(callable('str'))



# 实现这样的效果 Chain().users('michael').repos 输出/users/:user/repos
class Chain1(object):
	def __init__(self, path=''):
		self._path = path
	def __getattr__(self, path):
		return Chain1('%s/%s' % (self._path, path))
	def __str__(self):
		return self._path
	__repr__ = __str__
	def __call__(self, *c):
		s = ''
		for i in c:
			s += ':' + i
		return self.__getattr__(s)
print( Chain1().users('michael').repos )


#枚举
from enum import Enum, unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员
print(Month.Jan)
print(Month.Jan.value)
for name, member in Month.__members__.items():
	print(name, '=>', member, ',', member.value)


#如果要更精准的控制枚举类型, 可以从Enum派生出自定义类

@unique #这个装饰器可以检查保证没有重复值
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

print(Weekday.Mon)
print(Weekday.Mon.name)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(Weekday(2))


#type 使用type来创建类
def fn(self, name='world'): 
	print('Hello, %s' % name)

Hello = type('Hello', (object, ), dict(hello=fn)) #创建Hello class
h = Hello()
h.hello()

# 1.class的名称；
# 2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。

