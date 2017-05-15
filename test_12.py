# 定制类
class Test:
    name = "student"

    def get(self):
        print(Test.name)


test = Test()
test.get()


class Student(object):

    def __init__(self,  *test_tuple):
        self.test_tuple = test_tuple
        self.start_num = 0

    def __str__(self):
        '''定义该方法以后，使得该类可以print返回的内容'''
        return 'Student object (tuple: %s)' % str(self.test_tuple)

    __repr__ = __str__

    def __iter__(self):
        '''表示该类可以被用于 for...in...循环，类似list或tuple，然后for会不断的拿该迭代对象的__next__方法拿到循环的下一个值'''
        #  表示 iterable
        return self

    def __next__(self):
        length = len(self.test_tuple)
        if self.start_num < length:
            temp = self.test_tuple[self.start_num]
            self.start_num = self.start_num + 1
            return temp
        else:
            # 一定要是stopiteration
            raise StopIteration()

    def __getitem__(self, item):
        '''通过index来获取[0]'''
        # 如果item是int则直接这样就可以了
        # 如果item是切片对象，这需要判断
        if isinstance(item, int):
            return self.test_tuple[item]
        elif isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            l = []
            for x in self.test_tuple:
                if x >= start:
                    l.append(x)
            return l
    def __getattr__(self, item):
        '''
        定义该方法后，调用类的方法或属性时，如果查找比如student.name，没有name属性，则会立马报错
        如果定义了改法，则如果对象中没有该属性，则会直接调用该方法来进行查找
        AttributeError: 'Student' object has no attribute 'name'
        也可以直接返回一个函数
        很适合restful风格
        '''
        if 'name' == item:
            return 'wxy'
        print(item)
        print(type(item))
    def __call__(self, *args, **kwargs):
        '''
        定义该方法以后，就可以直接对该实例类似函数式的调用
        '''
        print('call: ', args, kwargs)
class my_list(object):
    def __init__(self,):
        pass
if __name__ == '__main__':
    student = Student(1, 2, 3, 4, 5)
    print(student)

    for x in student:
        print(x)

    print(student[1])
    print(student[::])
    # 先定义了name以后，就不会在走getattr方法了，因为该实例已经有name属性了
    # student.name = 10
    print(student.name)
    student()
    print(callable(student))
