# 使用元类


'''
type可以查看一个类型或者变量的类型
Hello是一个class，它的类型是：type

type()函数既可以返回一个对象的类型，也可以创建出新的类型，

python解释器遇到class定义时，也是直接调用type()函数来创建出class的
'''


class Hello1(object):
    def hello(self, name='world'):
        print('hello, %s' % name)


def fn(self, name="world"):
    print('hello, %s' % name)


print(type(Hello1))  # type

# 类名为Hello，继承object，绑定函数把fn绑定到hello上
Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
h.hello()

# 使用type来创建类以外，如果要控制类的创建行为，还要使用metaclass：元类
# 当我们定义了类以后，就可以根据这个类创建出实例，所以先定义类，然后创建类实例
# 如果想创建出类，就必须根据metaclass创建出类，所以：先定义metaclass，然后在创建类
# 总的来说：先定义metaclass， 就可以创建类， 最后创建类实例。



'''
类也是对象：只要使用了关键字class，python解释器在执行的时候就会创建一个对象
下面代码将在内存中创建一个对象，名字就是ObjectCreator， 这个对象自身拥有创建对象(类实例)的能力
但ObjectCreator的本质是一个对象，可以对它做：

元来就是用来创建类这种对象的东西
type是Python的內建元类，所以我们可以自己创建元类
__new__: cls：当前准备创建的类的对象，name：类的名称，bases：类继承的父类集合，attrs：类的方法集合
metaclass表示在创建ObjectCreator时要通过ListMetaclass.__new__方法来创建

'''


class ListMetaclass(type):

    # def __new__(cls, *args, **kwargs):
    #     print("create class, ", cls, cls.__name__, args, kwargs)
    #     return type.__new__(cls, args, kwargs)
    # def __new__(cls, *args, **kwargs):
    #     kwargs['add'] = lambda self, value: self.append(value)
    #     print('cls: ', cls, "\nargs: ", args, '\nkwargs:', kwargs)
    #     return type.__new__(cls, args[0], args[1], {args[2], kwargs})
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        print('cls: ', cls, "\nname: ", name, '\nbases:', bases, '\nattrs: ', attrs)
        return type.__new__(cls, name, bases, attrs)
class ObjectCreator(list, metaclass=ListMetaclass):
    pass

objectCreator = ObjectCreator()
objectCreator.add(10)
print(ObjectCreator)
print(type(ObjectCreator))
