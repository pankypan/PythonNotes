# __getattr__, __getattribute__
# __getattr__ 就是在查找不到属性的时候调用

import datetime


class User:
    def __init__(self, name, birthday: datetime.date):
        self.name = name
        self.birthday = birthday
        self._age = 0

    @property
    def age(self):
        return datetime.datetime.now().year - self.birthday.year

    def __getattr__(self, item):
        return f"Can't find {item}"

    # def __getattribute__(self, item):
    #     print(item)
    #     return item


if __name__ == '__main__':
    user = User('suki', datetime.date(1993, 9, 15))
    print(user.address)
    print(user.cookie)
