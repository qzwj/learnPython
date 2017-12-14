#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 请注意，当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用，但是，在分布式多进程环境下，添加任务到Queue不可以直接对原始的task_queue进行操作，那样就绕过了QueueManager的封装，必须通过manager.get_task_queue()获得的Queue接口添加。
# 然后，在另一台机器上启动任务进程（本机上启动也可以）：

import time ,sys, queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager
class QueueManager(BaseManager):
	pass

# 由于这个QueueManager是从网络上获取Queue, 所以注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器, 也就是运行task_master.py的机器
server_addr = '127.0.0.1'
# server_addr = '192.168.1.148'
print('Connect to server %s...' % server_addr)

# 端口和验证码要注意和task_master.py的机器保持一致
manager = QueueManager(address = (server_addr, 5000), authkey=b'abc')
# 从网络连接
manager.connect()

# 获取Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

# 从task队列取任务. 并把结果写入result队列
for i in range(10):
	try:
		n = task.get(timeout=1)
		print('run task %d * %d...' % (n, n))
		r = '%d * %d = %d' % (n, n, n*n)
		time.sleep(1)
		result.put(r)
	except Queue.Empty:
		print('task queue is empty.')

# 结束
print('worker exit')