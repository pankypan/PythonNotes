import datetime
import numbers

"""
只要实现了 __get__ / __set__ / __delete__ 三个方法任意一个，即实现属性描述符
"""


class IntField:
    # 数据描述符
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('int value need!')
        if value < 0:
            raise ValueError('positive value need!')
        self.value = value

    def __delete__(self, instance):
        pass


class NonDataIntField:
    def __get__(self, instance, owner):
        return self.sex_value


class User:
    def __init__(self):
        self.age = 0
    flag = 'user'
    age = IntField()
    sex = NonDataIntField()


'''
如果user是某个类的实例，那么user.age（以及等价的getattr(user,’age’)）
首先调用 __getattribute__ 。如果类定义了__getattr__方法，
那么在 __getattribute__ 抛出 AttributeError 的时候就会调用到 __getattr__，
而对于描述符(__get__）的调用，则是发生在__getattribute__内部的。
user = User(), 那么user.age 顺序如下：
（1）如果“age”是出现在User或其基类的__dict__中， 且 age 是 data descriptor， 那么调用其__get__方法, 否则
（2）如果“age”出现在 user的__dict__中， 那么直接返回 obj.__dict__[‘age’]， 否则
（3）如果“age”出现在User或其基类的__dict__中
（3.1）如果age是non-data descriptor，那么调用其__get__方法， 否则
（3.2）返回 __dict__[‘age’]
（4）如果User有__getattr__方法，调用__getattr__方法，否则
（5）抛出AttributeError
'''


if __name__ == "__main__":
    user = User()
    user.age = 27
    print(user.age)

    # user.age = '27'
    # user.age = -1
    print('User.__dict__:', User.__dict__)
    print('user.__dict__:', user.__dict__)
    print(user.age)
    print(user.age)

