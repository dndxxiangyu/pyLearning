# 面向对象
class Student(object):
    def __init__(self, name, score, father="wgw", mother="jgz"):
        self.name = name
        self.score = score
        self.__father = father
        self._mother = mother

    def print_score(self):
        print('%s, %s' % (self.name, self.score))
    def __test(self):
        print('private test method')

def other_method():
    print("other_ method")
def other_method1():
    print("other_ method")


'''
可以自由的给一个实例变量绑定属性：
bart.name = "bart simpson"
bart.age = 17

类起到的是模板的作用，所以在创建实例的时候把一些人为必须绑定的属性写入init方法中

__init__特殊方法：
第一个方法永远是self，所以可以把各种属性绑定到self上，就是绑定到创建对象的本身上去

python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然是同一个类型的不同实例，但拥有的变量和方法都可能不同

'''

# 访问限制：外部代码可以通过直接调用实例变量的方法来操作数据，但是外部代码还可以直接修改一个实例的属性，或者添加不存在的属性
# 如果内部属性不被外部访问，可以把属性的名称前加上两个下划线__， 在python中，实例的变量名如果以__开头，就变成了一个私有变量，只有内部可以访问，外部不能访问
# 不能直接访问的原因是由于python解释器把__father 解释成了_Student__father.

# _单个下划线的实例变量外部是可以访问的，按照约定：一般把它看成私有变量，不要随意访问，即使可以访问

student1 = Student('wxy',100,'wgy')
# print(student1.__father)

# 不推荐这么干，因为不同的解释器可能会把他改成不同的变量名。
print(student1._Student__father)
print(student1._mother)

student1.__father = "father"
# 该变量其实和上面的变量不是同一个变量，这个不需要解释器进行修改变量名称
print(student1.__father)
student1._Student__test()
#student1.__test()

if __name__ == '__main__':
    Student.other_method = other_method
    Student.other_method()
    print(Student)
    student = Student('wxy', 100)
    student.print_score()
    # 其实通过Student或者student进行调用函数，同一个函数对应的参数个数是不一样的，下面的会报错，因为类方法没有参数
    # student.other_method()
    student.father = "wgy"
    print(student.father)
    student.other_method = other_method1
    student.other_method()
    print(hasattr(student, '_Student__father'))
    print(hasattr(student, 'other_method'))