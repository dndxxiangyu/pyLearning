#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print("hello world")

# import keyword
# print(keyword.kwlist)

# 使用反斜杠来实现多行语句，result= 4
a = 1 + 1 + \
    1 + 1

print(a)

a = 1, 2, 3
print(a)
del a

# 输入输出
print()
# input(1111)

# if
a = 10
if a >= 10:
    print(a)
elif a == 11:
    print('age  =  11')
else:
    print(-a)

# list
classmates = ['michael', 'bob', 'tracy']
print(type(classmates))
print(classmates.count('bob'))
classmates.append('wxy')
classmates.insert(1, 'lc')
print(classmates)

# tuple, 内容是不能够改变的，不可以修改值
mates = ('michael', 'bob', 'tracy')
mates = (1,)

# for
print('test for \'for\'')
for name in classmates:
    print(name)

print("test for \'range\'")
for x in range(10):
    #可以看到x的范围为0 - 9
    print(x)

# dict,注意：因为dict根据key来计算value的存储位置，通过key的hash来计算value位置，
# 要保证hash的正确性，key就不能变，所以像list就不能作为key
print('\ntest for dict')
d = {'micial': 98, 'bob':75, 'tracy':85}
print(d['micial'])
#在使用key之前最好先判断一下key是否在dic中，micial in d
print(d.get('ccc'))

