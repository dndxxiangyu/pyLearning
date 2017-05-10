#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 函数, 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相对于给函数起了一个别名
import math

a = abs
print(a(-10))

def my_abs(x):
    # if isinstance(x, int or float or complex):
    if isinstance(x, (int , float)):
        if x >= 0:
            return x
        else:
            return -x
    else:
        raise Exception('bad operand type for abs(): ', type(x))

# 空函数
def nop():
    pass

# 返回多个值，其实返回的是一个tuple，只是你可以用多个对应的值来意义对应
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny
point = move(1,2, 10, 60)
print(point)

# 1、位置参数：正常、一般的参数，如上
# 2、默认参数，类似实现了java中的重载。注意：默认参数不能是可变对象
def default(a = 10, b = 11):
    print(a, b)
default(b = 'ccc')

# 3、可变参数：传入的参数个数可变，0-任意
def default(*args):
    print(args, ';typeof args: ', *args)
    # print(type(*args))直接报错
default(11111, 22222)

# 4、关键字参数：0-n个含参数名的参数，在函数内部会组装成dict
def default(**kwargs):
    print(kwargs, 'typeof kwargs: ', *kwargs)
default(cc = 10, dd = 11)

# 5、命名关键字参数：限制关键字参数的名字,*后面的被视为命名关键字参数
def default(name, age, *, city, job='it'):
    print(name, age, city, job)
default('wxy', 12, job = 'it',city ='hangzhou')
default('wxy', 12, city ='hangzhou')

# 如果函数定义中已经有一个可变参数，那么后面跟着的命名关键字参数就不再需要 *
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
person('wxy', 12, city='hz', job='it')

# 参数组合：可以使用上面5种关键字组合，但参数的定义顺序必须是：
# 必选参数、默认参数、可变参数、命名关键字参数、关键字参数

#所以对于任意函数，都可以通过func(*args, **kw)的形式来调用他，无论他的参数是如何定义的。
