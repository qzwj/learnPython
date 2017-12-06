#!/usr/bin/env python3

list=range(101)#生成一个整数序列,一共101个从0开始到100
sum = 0
for num in list:
    sum += num
print('sum = ', sum)

sum = 0
index = 0
while index <= 100:
    sum += index
    index += 1
print('sum = ', sum)


#break和contine和其他语言类似

#学到现在发现, 不用{}, 喜欢用:
