# 多重继承
class Animal(object):
    '''
    Animal doc
    '''

    pass


class Mammal(Animal):
    '''哺乳动物'''
    def run(self):
        '''mammal run'''
        print('i don\'t know weather can run')

    def fly(self):
        print('i don\'t know weather can fly')


class RunnableMixIn(object):
    def run(self):
        print('runnning............')


class FlyableMixIn(object):
    def fly(self):
        print("flying.........")


class Dog(Mammal, RunnableMixIn):
    pass


class Bat(Mammal, FlyableMixIn):
    pass


# MixIn：主线程都是单一继承下来的，如果要混入额外的功能的时候，就通过多重继承，为了更好的看出继承关系
# 我们把Runnable和Flyable改写为RunnableMixIn、FlyableMixIn

dog = Dog()
dog.run()
dog.fly()

# 注意：如果多重继承中两个子类都有run方法，则先调用继承的第一个类的方法。
animal = Mammal()
print(animal.__doc__)
print(animal.run.__doc__)
