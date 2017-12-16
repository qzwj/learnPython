#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 多任务执行, 单核cpu就是速度很快的轮询 表现的并行, 真正的并行需要多核cpu, 操作系统会自动把任务轮流调度到每个核心上执行
# 线程是最小的执行单元，而进程由至少一个线程组成。如何调度进程和线程，完全由操作系统决定，程序自己不能决定什么时候执行，执行多长时间。
# 多进程和多线程的程序涉及到同步、数据共享的问题，编写起来更复杂。

#多进程
import os 
# print('Process (%s) start...' % os.getpid())
# pid = os.fork() #linux/Unix系统才可以调用, 返回两次, 操作系统把当前进程(父进程) 复制了一份(子进程),然后分别返回, 子进程永远返回0, 父进程返回子进程的ID. 一个父进程可以fork很多子进程, 所以父进程要记录一下每个子进程的ID, 在子进程中只需要getppid()就可以拿到父进程的ID
# if pid == 0: #看打印结果可以看出返回了两次, 先返回父进程, 在返回子进程, os.getpid()拿到当前的进程ID 
# 	print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
# 	print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# 有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求



#multiprocessing 跨平台版本的多进程模块
# multiprocessing模块提供了一个Process类来代表一个进程对象



#在测试的时候突然发现上面的fork()可以让整个文件执行两次, 在理解为什么返回2次
print('---------multiprocessing---------') 
from multiprocessing import Process 
import os
# 子进程要执行的代码
def run_proc(name): 
	print('Run child process %s (%s)...' % (name, os.getpid()))

# 这个代码应该是自动执行的
if __name__ == '__main__':
	print('Parent process %s .' % os.getpid())
	p = Process(target=run_proc, args=('test',)) #创建子进程
	print('Child process will start')
	p.start() #开始执行子进程
	p.join() #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
	print('Child process end.')



#Pool 如果要启用大量子进程, 可以用进程池的方式批量创建子进程
print('---------Pool---------')
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
	print('Run task %s (%s)...' % (name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s runs %0.2f seconds.' % (name, (end-start)))

if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())
	p = Pool(4)
	for i in range(5):
		p.apply_async(long_time_task, args=(i,))#进程池开始循环执行子进程
	print('Waiting for all subprocess done...')
	p.close() # 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
	p.join() 
	print('All subprocess done.')
	# 请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。如果改成5, 都是一起按顺序执行的




#子进程(不知道干嘛用的目前)
# 很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出
#subprocess 模块可以让我们非常方便的启动一个子进程, 然后控制输入和输出
print('---------subprocess---------')

import subprocess
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)


#如果子进程还需要输入, 可以通过communicate()方法输入:
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
# 上面的代码相当于在命令行执行命令nslookup，然后手动输入：
# set q=mx
# python.org
# exit


#进程间的通信
#Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
# 我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据
from multiprocessing import Process, Queue
import os, time, random

#写数据
def write(q):
	print('Process to write: %s' % os.getpid())
	for value in ['A', 'B', 'C']:
		print('Put %s to queue ...' % value)
		q.put(value)
		time.sleep(random.random())

#读数据
def read(q):
	print('Process to read: %s' % os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue.' % value)

if __name__ == '__main__':
	#创建queue传入process
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))

	#启动子进程pw, 写入
	pw.start()

	#启动子进程pr, 读取
	pr.start()

	#等待pw结束
	pw.join()

	#pr 进程死循环, 无法等待结束, 只能强行终止
	pr.terminate()

# 以上每个进程基本都关联一个函数, 这个函数就是要执行的任务

