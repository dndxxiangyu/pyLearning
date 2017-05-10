#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 装饰器decorator：接收一个函数作为参数，并返回一个函数
def log(func):
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print("2017-05-10")

now()

#两个测试方法，无意义
def _private1():
    print("private_1")
def __private2():
    print("private_2")