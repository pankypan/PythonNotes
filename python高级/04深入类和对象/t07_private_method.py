from datetime import date


class User:
    def __init__(self, birthday):
        self.__birthday = birthday

    def get_age(self):
        # 返回年龄
        return 2018 - self.__birthday.year


if __name__ == "__main__":
    user = User(date(1990, 2, 1))
    print(user._Student__birthday)
    print(user.get_age())
