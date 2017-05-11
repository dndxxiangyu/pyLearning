# 继承和多态

'''
python支持多继承，

'''


class Animal:
    def run(self):
        print('animal run')


class Dog(Animal):
    def run(self):
        print("dog run")


class Cat(Animal):
    def run(self):
        print('cat run')


class Man:
    def run(self):
        print('man run')


def run_twice(animal):
    animal.run()
    animal.run()


# 多态的好处：只需要接收animal基类行，不管是dog、cat。

# 静态语言和动态语言：
# 静态语言java：传入的对象必须是Animal类型或者其他的子类；
# 动态语言：不一定传入Animal类型，只需要保证传入的对象有一个run方法就可以

# 动态语言就是鸭子类型，不需要严格的继承体系，一个对象只要看起来像鸭子，那他就可以被看做是鸭子。
if __name__ == '__main__':
    dog = Dog()
    dog.run()
    cat = Cat()
    cat.run()
    man = Man()

