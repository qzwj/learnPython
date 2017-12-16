#!/usr/bin/env python3

print('-----------高级函数-----------')
#函数名字本身就就是一个变量, 可以给其他变量赋值, 也可以被替换
def test(a,b,f): #把函数作为参数
	return f(a) + f(b)
print('test(3,-3,abs) =', test(3,-3,abs))



print('-----------map,reduce-----------')
from functools import reduce

L = [1,2,3,4,5]
def f(x):
	return x * x
print('map(f, L) =', list(map(f, L)))

def normalize(name):
	if len(name) == 0:
		return ''
	else:
		return name[0].upper() + name[1:].lower()
str1 = ['LWJ', 'dQy', 'aah']
print(list(map(normalize, str1)))

def add(a,b):
	return a * 10 + b
print('reduce(add, L) =',reduce(add, L))

#字符串转浮点数
def str2float(s):

	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.' : '.'}[s]
	def fx(x, y):
		if y == '.':
			return x
		else:
			return x * 10 + y
	i = len(s) - s.find('.') - 1
	return reduce(fx, map(char2num, s)) * 0.1 ** i #0.1的i次方

print(str2float('123.456'))



print('-----------filter-----------')
def is_odd(x):
	if x % 2 == 1:
		return x
print('filter(is_odd, L)', list(filter(is_odd, L)))

def not_empty(s):
	return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, '   ', 'C'])))


#筛选出质数, 这种计算质数的方法是 埃式筛法, 从2开始的自然数排列, 取序列第一个数2, 它一定是质数,  把序列的2的倍数筛选掉得新的序列, 这个新序列的第一个数3一定是质数, 依次类推
def _odd_iter():
    n = 1
    while True:
        n = n + 2 #加2的原因是因为偶数除了2没有质数了, 2的情况在后面处理
        yield n

def _not_divisible(n): 
    return lambda x: x % n > 0 #返回一个匿名函数

def primes():
    yield 2 #  直接把2作为第一个质数
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

for n in primes():
    if n < 100:
        print(n)
    else:
        break


def is_palindrom(n):
	return str(n) == str(n)[::-1] #每隔-1取一个, 就是取这个字符串的反

print('1-100之间的回数 ===',list(filter(is_palindrom, range(1,100))))

print('-----------sort-----------')
#排序的sort()同样也是高级函数, 把比较的过程抽象出来了, 排序的关键也是映射的函数
L1 = [36, 5, -12, 9, 33]
print('L1 =', L1)
print('sorted(L1) =', sorted(L1))  #默认按值的大小排序的
print('sorted(L1, key=abs) =',sorted(L1, key=abs)) #按绝对值排序的
L2 = ['bob', 'about', 'Zoo', 'Credit']
print(L2)
print('sorted(L2) =', sorted(L2)) #默认按ascii码排序的
print('sorted(L2, key=str.lower) =',sorted(L2, key=str.lower)) #都转为一个格式进行比较, 不区分大小写
print('sorted(L2, key=str.lower, reverse=True) =',sorted(L2, key=str.lower, reverse=True))#反向排序

print(str(123)[::-1])


print('-----------返回函数-----------')
#普通函数求和, 直接计算出求和的结果
def calc_sum(*args):
	sum = 0
	for n in args:
		sum += n
	return sum
print('sum =', calc_sum(1,2,3,4))

#返回一个函数
def lazy_sum(*args):
	def sum():
		s = 0
		for n in args:
			s += n
		return s
	return sum
print('lazy_sum =', lazy_sum(1,2,3,4)())
f1 = lazy_sum(1,2,3,4)
f2 = lazy_sum(1,2,3,4)
print('f1 than f2 =', f1 == f2)


print('-----------闭包-----------')
#返回的函数  在定义的内部使用了局部变量, 所以当函数返回后, 局部变量还被引用着, 返回的函数没有立即被执行, 知道我们调用才会被执行

def count():
	fs = []
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs
for f in count():
	print(f()) #结果都为9, 说明返回函数没有立即执行, 当循环解释时, 返回函数引用外部的局部变量发生了改变, 导致list中所有返回函数的变量都发生了变化

#返回闭包记住 不要在返回函数中引用循环变量, 或者后续会发生变化的变量
#非要用循环变量
def count1():
	def f(j):
		def g():
			return j*j
		return g
	fs = []
	for i in range(1,4):
		fs.append(f(i))#f(i)立刻被执行, fs装的是 f函数返回的g函数
	return fs
for f in count1():
	print(f())

#计算器函数, 每次调用后增加1
def createCounter():
	n = 0
	def counter():
		nonlocal n #默认子函数只有访问权限, 这个可以自由修改
		n += 1
		return n
	return counter
counter = createCounter()
print('counter =', counter())
print('counter =', counter())
print('counter =', counter())



print('-----------匿名函数-----------')
#匿名函数 只能由一个表达式 lambda 形参: 返回值表达式
print('匿名函数 =',list(map(lambda x: x * x, range(1,5))))
#可以作为变量
f = lambda x: x * x * x
print('匿名函数作为变量 =', f(5))
#作为返回值
def build(x, y):
	return lambda: x*x + y*y
print('匿名函数作为返回值 =', build(2,3)())



print('-----------装饰器-----------')
import functools
def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('我是装饰器添加的 call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def now():
	print('2017-12-06')

now()

def test(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('我是装饰器添加的 %s %s():'  % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@test('test')
def old():
	print('我是测试的str')
old()


#在每个函数执行前后都加一个print打印
def addPrint(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('%s func excute before' % func.__name__)
		result = func(*args, **kw)
		print('%s func excute after' % func.__name__)
		return result
	return wrapper

@addPrint
def hello():
	print('Hello Python3')
	return 'success' #后添加的是不是应该 在这个success打印后面, 不会写
print(hello()) 
 

#偏函数 简化函数参数过多
#当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单

print('10进制的 12345 =', int('12345'))
print('8进制的 12345 =', int('12345', base=8))
print('16进制的 12345 =', int('12345', base=16))

def int2(x, base = 2):
	return int(x, base)
print('二进制的10101010 =',int2('10101010'))


int22 = functools.partial(int, base=2) #偏函数写法
print('二进制的10101010 =',int22('10101010'))
print('8进制的 12345 =', int22('12345', base=8))

#partial 接受 函数对象, *args, **kw
max2 = functools.partial(max, 8) #8作为可变参数传入了
print('max2(1,2,3,4) =', max2(1,2,3,4))

