#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 高阶函数：把函数作为参数传入其他函数，这就是高阶函数
from functools import reduce


def add(x, y, f = abs):
    return f(x) + f(y)
print(add(1,2,abs))

# map/reduce
def f(x):
    return x * x
#必须传入两个参数，产生的结果再和下一个参数做累计计算
r = map(f, (1,2,3,4,5))
print(r)
print(list(r))

r = reduce(add, [1,2,3,4,5,6])
print(r)

def is_odd(n):
    return n % 2 == 1
# filter
a = filter(is_odd, [1,2,3,4,5,6])
print(list(a))

print(sorted([1,2,3,4,-5], key = abs))


# 函数返回是一个函数：可以作为懒加载
def lazy_sum(*args):
    def sum():
        ax = 0
        for x in args:
            ax = ax + x
        return ax
    return sum
f = lazy_sum(1,2,3,4,5)
f()#只有在这的时候才会去真正执行sum内部的流程

# 匿名函数：
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
