# 序列化
# 和java的serialization一样，pyhton使用pickling

import pickle

d = dict(name='bob', age=20, score=88)
print(pickle.dumps(d))

f = open('d:/text1.txt', 'wb')
print(f)
pickle.dump(d, f)
f.close()

f = open('d:/text1.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)

# json
import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name;
        self.age = age;
        self.score = score


def student2dict(std):
    return {'name': std.name, 'age': std.age, 'score': std.score}


s = Student('wxy', 20, 100)
print(s.__dict__)
print(json.dumps(s, default=student2dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))
