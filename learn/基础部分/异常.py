#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#try except finally

try:
	print('try....')
	r = 10 / 0 #可能会出现异常的地方, 如果出现错误, 后面的就不会执行了, 开始执行except
	print('result:', r)
except ZeroDivisionError as e: #try语句里没有错误发生, 这个except就不会执行
	print('except:', e)
finally:
	print('finally...') #不管怎么样都会执行

print('END')

#所有的错误都是类, 继承自BaseException

def foo(s):
	return 10 / int(s)
def bar(s):
	return foo(s) * 2
def main(): #跨层级调用, main里捕获到里bar()的错误,就可以直接处理, 所以我们不需要在每个可能出错的地方去捕获错误, 只需要在核实的地方去捕获错误, 可以减少些try, except,finally等

	try:
		bar('0')
	except Exception as e:
		print('Error:', e) #打印输出错误的日志, 打印完了后会正常执行程序
		# logging.exception(e)
	finally:
		print('finally...')
main()

#如果我们没有处理错误, 错误会一层一层的打印出, 我们要可以根据这个调用栈去找到真正源头的错误


#抛出错误
class FooError(ValueError):
	pass
def fos(s):
	n = int(s)
	if n == 0:
		raise FooError('invalid value: %s' % s) #抛出错误, 尽量选用自带的错误类型
	return 10 / n
fos('0')

#捕获错误并且抛出错误
#捕获错误只是为了看错误的信息,跟踪错误, 我们自己处理不了可以交给上面去处理
# def foo(s):
#     n = int(s)
#     if n==0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n

# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise
# bar()