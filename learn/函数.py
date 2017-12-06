#!/usr/bin/env python3
def hello():
    print('hello func')
hello()

def wj_abs(a):
    if a < 0:
        return -a
    else:
        return a

c = wj_abs(-5)
print(c)

def getPoint(a, b):
    a = a-1
    b = b+1
    return a,b
#本质上就是返回一个purple
d = getPoint(2,3)
print(d)


