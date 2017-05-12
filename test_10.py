# use the decorator of property
# property：负责把一个getter方法变成属性，
# property本身优惠创建另外一个装饰器@score1.setter,负责把一个setter方法变成属性赋值

class Student(object):
    @property
    def score1(self):
        return self.__score

    @score1.setter
    def score(self, value):
        print('score: ', value)
        self.__score = value

def test(self, test):
    print(self, test)

Student.test = test
student = Student()
student.score = 10         #调用的是score方法
print(student.score) # 调用的是score1方法，获取属性
student.test('ccc')
