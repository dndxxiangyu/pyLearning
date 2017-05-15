# 错误处理
'''
程序发生了错误，如果约定错误码，则函数本身会因为返回的正常结果和错误码混在一起，调用者必须使用大量的代码来判断是否出错
一旦出错，还要一级一级上报，知道某个函数可以处理该错误，
除非使用try
'''
try:
    print('try....')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except: ', e)
else:
    # 没有exception发生的时候才会执行else语句
    print('no exception occur')
finally:
    print('finally....')

'''
try exception：可以跨越多层调用
不需要再每个可能出错的地方都去捕获错误，只要在合适的层次去捕获错误就可以了。
'''
import logging


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        print("Error", e)
        logging.exception(e)
    finally:
        print("finally")


main()


class FoolError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FoolError('invalid value:%s' % s)
    return 10 / n

