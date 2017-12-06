#!/usr/bin/env python3
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85, 'lwj' : 18}
print(d['Bob']) #如果这样直接获取, 获取不到会报错
print(d['Michael'])
print(d['lwj'])
v1 = d.get('ss')
v2 = d.get('aa', -2)
d.pop('lwj')
print(d)
print('v1 = ', v1)
print('v2 = ', v2)
s = set([1,2,3,4,3,2,1])
print(s)
s.add(11)
s.remove(1)
print(s)

s1 = set([0,2,3,4,5,6,7,8])
print(s & s1)
print(s | s1)

#list可以放不同的元素, 也可以放list
list=['apple','lwj','sss','dqy']
print(list)
list.append('love')
list.insert(1, 'good')
list.pop() #删除末尾的
list.pop(0)
list.insert(0, 1)
print(list)
print('list.length = ',len(list))
list.insert(1,[0,2,3,4])
print(list)
print('list[1][1] = ', list[1][1])


#purple一旦定义,元素的指向不能变, 如果元素是list,list自身的内容可以变, 指向不能变
p1 = (1,2,3)
print(p1)
p1 = (2,) #定义一个purple, 要在后面加, 区分和()的区别
print(p1)
p1 = (2, list)
print(p1)
list.insert(0, 'purple')
print(p1)
