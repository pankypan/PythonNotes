# 类也是对象，type创建类的类
def create_class(name):
    if name == 'User':
        class User:
            def __str__(self):
                return 'User'

        return User
    elif name == 'Company':
        class Company:
            def __str__(self):
                return 'Company'

        return Company


# type动态创建类
# User = type("User", (), {})

def say(self):
    return "I am " + self.name


class BaseClass:
    def answer(self):
        return 'I am BaseClass'


# 什么是元类， 元类是创建类的类 对象<-class(对象)<-type
# python中类的实例化过程，会首先寻找metaclass，通过metaclass去创建 User类
# 去创建类对象，实例
class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        print('in metaclass __new__')
        return super().__new__(cls, *args, **kwargs)


class User(metaclass=MetaClass):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "User"


if __name__ == "__main__":
    # MyClass = create_class('User')
    # my_obj = MyClass()
    # print(type(my_obj))
    #
    # User2 = type("User2", (BaseClass,), {'name': 'panky', 'say': say})
    # my_obj = User2()
    # print(my_obj.say())
    # print(my_obj.answer())

    user = User('snoopy')
