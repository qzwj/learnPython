#!/usr/bin/env python3
#位置参数,也是必须参数
# def power(x):
#     return x*x

# print(power(5))
# print(power(6))

#可以重载
# def power(x, n):
#     sum = 1
#     while n > 0:
#         sum *= x
#         n-=1
#     return sum
# print(power(2,3))
# print(power(2,4))

#默认参数, 必须放在后面(变化小), 必选参数放在前面(变化大)
def power(x, n=2):
    s = 1
    while n > 0:
        s *= x
        n-=1
    return s
print(power(2))
print(power(2,4))

def enroll(name, gender, age=25, city='苏州'):
    print(name, gender, age, city)
enroll('lwj', '男')
enroll('dqy', '女', city='吴江') #不使用默认的参数, 就这样显示的改变

# def add_end(L=[]): #如下面解释的那样, 如果我们直接使用默认的L, 多次调用会出现重复, 因为这个默认的都是指向同一个地址
#     L.append('End')
#     print(L)
#     return L
# add_end([1,2,3])
# add_end()
# add_end() 
#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

#所以要注意, 定义默认参数必须指向不可变对象
def add_end(L=None):
    if L is None:
        L=[]
    L.append('End')
    print(L)
    return L
add_end()
add_end()


#可变参数
def calc(numbers):
    sum = 0
    for num in numbers:
        sum = sum + num * num
    print(sum)
    return sum
calc([1,2,3,4,5]) #调用需要组装list或者purple,比较麻烦

def calc(*numbers): 
    sum = 0
    for num in numbers:
        sum = sum + num * num
    print(sum)
    return sum
calc(1,2,3)
calc()
list = [1,2,3]
calc(*list)


#关键字参数
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
# def person(name, age, **kw):
#     print('name:',name, 'age:',age, 'kw:',kw)
# person('lwj', 25)
# person('lwj', 25, city='suzhou', job='it')
# #也可以先组装一个dict, 然后直接传入
# dic = {'city':'wujiang', 'job':'guanli'}
# person('dqy', 24, **dic) #注意kw获得的dict是dic的一份拷贝, 不会影响到外面的dic


# #命名关键字参数
# def person1(name, age, **kw):
#     if 'city' in kw:
#         pass
#     if 'job' in kw:
#         pass
#     print('name:',name, 'age:',age, 'other:',kw)
# person1('test', 25, city='ss', color='red') #调用者仍然可以传入不受限制的关键字


# def person(name, age, *, city, job):
#     print(name, age, city, job)
# person('lwj', 25, city='suzhou', job='it')
# person('lwj', 25, city='suzhou') 不能缺省

# def person(name, age, *, city='suzhou', job): #可以有默认值
#     print(name, age, city, job)
# person('lwj', 25, job='iOS')

def person(name, age, *args, city, job): #可变参数, 可以省略*
    print(name, age, args, city, job)

person('lwj', 25, 'red', 'dqy', city='suzhou', job='it')


#参数组合
def f1(a, b, c=0, *args, **kw):
    print('a =',a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =',a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
 
f1(1,2)
f1(1,2, c = 3)
f1(1,2,5,'a','b')
f1(1,2,5,'a','b', x=20)
f2(1,2,d=99,ext=None, x=99)
#我们可以通过tuple和dict调用函数
args = (1,2,5,4)
kw={'d' : 99, 'x':'#'}
f1(*args, **kw)

args2 = (1,2,3)
kw2 = {'d' : 88, 'x':'#', 'y':'@'}
f2(*args2, **kw2)



