# module test

# import test_5
# test_5.now()

# from test_5 import now
# now()

#其他模块中，下划线_ 和双__开头的函数或属性其实是可以访问的，但是不建议访问
import test_5
test_5._private1()
test_5.__private2()

if __name__ == '__main__':
    pass

# 安装第三方模块，是通过pip工具完成的
