#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#调试程序, 可以打印print, 生成环境很麻烦, 很懂垃圾信息
#断言, 类似print, 虽然可以-O 关闭
#logging 日志打印比较好, 可以直接通过配置,输出到文件里, 我们可以自己查找
# 分为四种, info, debug, warnning, error

def foo(s):
	n = int(s)
	assert n != 0, 'n is zero!'
	return 10 /n
def main():
	foo('0')

main()

import logging
# logging.basicConfig(level=logging.INFO) #不配置这个, 不会显示, 因为有4种
s = '0'
n = int(s)
logging.info('n = %d' %n)
print(10 / n)

#另外还有pdb单步调试, pdb.set_trace()直接定位错误地点和一些三方IDE