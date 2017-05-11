# 实例属性和对象属性

class Student:
    name = 'Student'


# 当定义了一个了属性后，这个属性虽然归类所有，但类的所欲实例都可以访问这个类属性
student = Student()
print(student.name)

# 由于实例属性优先级比类属性高，所以会屏蔽掉类的name属性
# 但是类属性并未消失，使用Student.name仍然可以访问
student.name = 'Teacher'
print(student.name)
print(Student.name)

from types import MethodType


def set_age(self, age):
    self.age = age


# 给实例绑定一个方法，该方法只对该实例起作用
student.set_age = MethodType(set_age, student)
student.set_age(10)
print(student.age)

# 给class绑定方法，这样所有实例都可以调用该方法
def set_score(a, score):
    print(a)
def test():
    print('test')
Student.set_score = set_score
Student.test = test
student = Student()
student.set_score(111)
# student.test()
student.test = test
student.test()