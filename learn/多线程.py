#!/usr/bin/env python3 
# -*- coding:utf-8 -*-

#多任务可以由多进程完成, 也可以由一个进程内的多个线程完成, 线程是程序的最基本的执行单元
#python提供了: 低级模块_thread, 和高级模块 _threading

#启动一个线程就是把一个函数传入并创建Thread实例, 然后调用start()开始执行
import time, threading

#默认有一个主线程, 这个函数很清晰
def loop():
	print('thread %s is running...' % threading.current_thread().name)
	n = 0
	while n < 5:
		n += 1
		print('thread %s >> %s' % (threading.current_thread().name, n)) #%s可以用作整型
		time.sleep(1)
	print('thread %s ended.' % threading.current_thread().name)
print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended' % threading.current_thread().name)




#Lock
# 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
import time, threading
balance = 0

# def change_it(n):
# 	global balance
# 	balance = balance + n
# 	balance = balance - n
# def run_thread(n):
# 	for i in range(100000):
# 		change_it(n)
# t1 = threading.Thread(target=run_thread, args=(5,))#后面是参数
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance) #balance不一定是0, 原因如下

# 一条语句在CPU执行时是若干条语句
# x = balance + n
# balance = x
# t1和t2交替执行, 可以顺序会乱



#所以需要上锁, 同时只能一个线程访问
lock = threading.Lock()

def change_it(n):
	global balance
	balance = balance + n
	balance = balance - n
def run_thread(n):
	for i in range(100000):
		lock.acquire() #先获取锁
		try:
			change_it(n) # 这里就可以安全的修改
		finally:
			lock.release() #释放锁
t1 = threading.Thread(target=run_thread, args=(5,))#后面是参数
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
# 当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。
# 获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。所以我们用try...finally来确保锁一定会被释放。
# 锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，坏处当然也很多，首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。



#了解
# 多核CPU

# 如果你不幸拥有一个多核CPU，你肯定在想，多核应该可以同时执行多个线程。

# 如果写一个死循环的话，会出现什么情况呢？

# 打开Mac OS X的Activity Monitor，或者Windows的Task Manager，都可以监控某个进程的CPU使用率。

# 我们可以监控到一个死循环线程会100%占用一个CPU。

# 如果有两个死循环线程，在多核CPU中，可以监控到会占用200%的CPU，也就是占用两个CPU核心。

# 要想把N核CPU的核心全部跑满，就必须启动N个死循环线程。

# 试试用Python写个死循环：

# import threading, multiprocessing

# def loop():
#     x = 0
#     while True:
#         x = x ^ 1

# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()
# 启动与CPU核心数量相同的N个线程，在4核CPU上可以监控到CPU占用率仅有102%，也就是仅使用了一核。

# 但是用C、C++或Java来改写相同的死循环，直接可以把全部核心跑满，4核就跑到400%，8核就跑到800%，为什么Python不行呢？

# 因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。

# GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的解释器。

# 所以，在Python中，可以使用多线程，但不要指望能有效利用多核。如果一定要通过多线程利用多核，那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。

# 不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。

# 小结

# 多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。

# Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。