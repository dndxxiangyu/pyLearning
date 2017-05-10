#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python的高级特性

# 切片
L = ['michael', 'sarah', 'tracy', 'bob', 'jack']
# 索引重0开始，到索引为3但不包括3
print(L[0:3])
print(L[:3])
# 索引从1开始，到索引为3单不包括3
print(L[1:3])
print(L[-3::2])
# 从0开始到末尾，且间隔2取一次值
print(L[0::2])

# 迭代，即可以使用for循环，这种遍历为迭代：iterable
# 判断类型是否可以使用for循环，首先：isinstance('abc', Iterable)


# 列表生成式：
print(list(range(1, 10)))
print([x * x for x in range(10)])
print([x * x for x in range(10) if x % 2 == 0])
print([m + n for m in 'abc' for n in 'xyz'])

# 生成器：列表容量有限，可以创建不完整的list，从而节约空间，一边循环已经计算的机制
# 创建一个generator,generator可以通过next来得到下一个值，一般直接使用for循环来调用
g = (x * x for x in range(10))


# 创建一个generator：函数中添加yield
def fib(max):
    print('now execute fib')
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
f = fib(6)
print(f)#generator

# Iterator表示可以执行next方法，而[] ()之类的都不是Iterator迭代器
# 转换过后就可以变成Iterator
it = iter([1,2,3,3,4,])
print(it)


