#!/usr/bin/env python3

#切片
print('------------切片-------------')
L=['lwj', 'dqy', 'test', 'aha', 'good', 'morning']
print(L)
print('取前三个:',L[0:3]) #不包括3, 即0,1,2
print('取前三个:',L[:3]) #可以省略0, 如果第一个是0的话
print('从1开始到2结束:',L[1:3])
print('从倒数第二个开始:',L[-2:])
print('从倒数第二个到倒数第一个:',L[-2:-1])
print('倒数第一个元素:',L[-1]) #倒数第一个元素

L2=list(range(100)) 
print(L2)
print('取前10个:',L2[:10])
print('取后10个:',L2[-10:])
print('前11-20个数:',L2[10:20])
print('前10个数,每两个取一个:', L2[:10:2])
print('所有数,每5个取一个:',L2[::5])
print('所有数,复制一个list:', L2[:])


#字符串也可以看做一种list, 每个元素就是一个字符
str1 = 'abcdefg'
print(len(str1))
print(str1)
print(str1[:3])
print(str1[1:3])
print(str1[::3])
print(str1[:-1])


#递归加切片写一个去除字符串首尾的空格
def trim(s):
	if(len(s) == 0 or (s[0]) != ' ' and s[-1] != ' '):
		return s #只有首尾都不为空才会有输出
	elif s[0] == ' ': #首部为空, 继续递归从下一位开始
		return trim(s[1:])
	else: #首部不为空, 就是尾部为空了, 去掉最后一位
		return trim(s[:-1])

test = '  hel lo '
print(test)
print(trim(test))


print('------------迭代-------------')
#迭代, 只要是迭代对象都可以遍历
d = {'a' : 1, 'b' : 2, 'c' : 3}
for key in d: #默认遍历key
	print(key)

for key, value in d.items():
	print(key, '=', value)

for ch in 'ABC': #遍历字符串
	print(ch)

for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)

for x, y in [(1,2), (2,3), (3,4)]:
	print(x, y)


print('------------列表生成-------------')
#列表生成
print('list(range(1,11)从1开始到10结束:)',list(range(1,10)))
#生成 [1*1, 2*2, 3*3] 循环太麻烦
print([x * x for x in range(1,11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])
c = {'x' : 'A', 'y' : 'B', 'z' : 'C'}
print([k + '=' + v for k, v in c.items()])
print([s.upper() for s in L])
L3 = ['Hello', 'World', 18, 'Apple', None]
print([x.lower() for x in L3 if isinstance(x, str)])



print('------------生成器-------------')
L4 = [x * x for x in range(1,10)]
print('L4 =', L4)
g = (x * x for x in range(1,10))
print('g =', g)
print('next(g) =', next(g))
print('next(g) =', next(g))
#list和generator的区别就是后者可以next(), 一个个的获取, 也可以遍历
for s in g: #从next的指针开始
	print('generator的子元素:',s)

#斐波拉契数列
# def fib(max):
# 	n,a,b = 0, 0, 1
# 	while n < max:
# 		print(b)
# 		a, b = b, a+b
# 		n += 1
# 	print('done') 
# fib(6)

def fib2(max): 
	n,a,b = 0, 0, 1
	while n < max:
		yield b #到这里停止并且打印, 有这个的函数已经可以是 gengrator
		a, b = b, a+b
		n = n + 1
for s in fib2(6):
	print(s)

#杨辉三角
def triangles(n):
	L = [1]
	# big = []
	while len(L) < n+1:
		yield L
		# big.append(L[:])
		L.append(0)
		L = [L[i-1]+L[i] for i in range(len(L))]
	# return big
for angle in triangles(8):
	print(angle)


print('------------迭代器-------------')
#作用于for循环的数据类型有一下几种:
#一类集合类型: 如list, tuple, dict, set, str
#一类generator, 包括生成器和带yield的generator function
#这些可以直接作用于for循环的对象称为可迭代对象: Iterable
#可以使用isinstance() 判断一个对象是否是Iterable对象
from collections import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))
# 而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
# 可以使用isinstance()判断一个对象是否是Iterator对象：
from collections import Iterator
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
#为什么list,dict, str等数据类型不是Iterator, 因为Python的Iterator对象表示一个数据流, Iterator对象可以被next()函数调用并不断返回下一个数据, 直到没有数据抛出错误, 但我们却不能提前直到序列的长度,只能不断通过next()函数实现按需计算下一个数据,所以Iterator的计算是惰性的, 只有在需要数据返回下一个数据时才会计算,所以Iterator甚至可以表示一个无限大的数据流,例如全体自然数. 而list永远不可能存储全体自然数的

#小结
#凡是可以作用于for循环的对象都是Iteratable类型:
#凡是可用作用于next()函数的对象都是Iterator类型, 它们表示一个惰性计算的序列
#集合类型如list,dict,str等是Iterable, 不是Iterator,可以通过Iter()函数获取一个Iterator对象
#Python的for循环本质上就是通过不断调用next()函数实现的
for x in [1,2,3,4,5]:
	pass

it = iter([1,2,3,4,5])
while True:
	try:
		x = next(it)
	except StopIteration:
		break
	

