#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# 在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁。
# 但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦：

class Student(object):
	def __init__(self, name):
		self.name = name

def process_student(name):
	std = Student(name)
	do_task_1(std)
	do_task_2(std)

def do_task_1(std):
	do_subtask_1(std)
	do_subtask_1(std)

def do_task_2(std):
	do_subtask_2(std)
	do_subtask_2(std)

def do_subtask_1(std):
	print('do_subtask_1 = ', std.name)

def do_subtask_2(std):
	print('do_subtask_2 =', std.name)

process_student('lwj')
#像上面一层层的传递很麻烦,  用全局变量每个线程处理不同的Student对象, 也不可以

import threading

#尝试用dict存放所有的Student对象. 然后把thread自身作为key获得对应Student对象
global_dict = {}

def std_thread(name):
	std = Student(name)
	global_dict[threading.current_thread()] = std
	do_task_1()
	do_task_2()

def do_task_1(): #函数的重载 和上面的, 函数名一样, 参数不一样
	std = global_dict[threading.current_thread()] #没有开辟线程, 默认在主线程
	print('do_task_1.thread.name =', threading.current_thread().name)
	print('do_task_1 =',std.name)

def do_task_2():
	std = global_dict[threading.current_thread()]
	print('do_task_2.thread.name =', threading.current_thread().name)
	print('do_task_2 =',std.name)

std_thread('python')
#这种方式可行, 但是代码有点丑, 更简单的方式是下面的ThreadLocal, 不用查找dict, 自动帮我们做



#ThreadLocal
local_shool = threading.local()

def process_student():
	# 获取当前线程关联的student变量
	std = local_shool.student
	print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
	# 绑定ThreadLocal的student变量
	local_shool.student = name
	process_student()

t1 = threading.Thread(target = process_thread, args=('lwj',), name = 'Thread-1')
t2 = threading.Thread(target = process_thread, args=('ss',), name = 'Thread-2')
t1.start()
t2.start()
t1.join()
t2.join()
print('End')

# 全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。你可以把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。
# 可以理解为全局变量local_school是一个dict，不但可以用local_school.student，还可以绑定其他变量，如local_school.teacher等等。
# ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源


#一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。




