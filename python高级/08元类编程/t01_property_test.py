import datetime


class User:
    def __init__(self, name, birthday: datetime.date):
        self.name = name
        self.birthday = birthday
        self._age = 0

    @property
    def age(self):
        return datetime.datetime.now().year - self.birthday.year

    @age.setter
    def age(self, value):
        self._age = value


if __name__ == '__main__':
    user = User('suki', datetime.date(1993, 9, 15))
    user.age = 24
    print(user.age)
    print(user._age)
