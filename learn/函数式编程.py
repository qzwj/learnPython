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

def _not_divisible(n): #这里还不是很理解 这个lambda
    return lambda x: x % n > 0

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
