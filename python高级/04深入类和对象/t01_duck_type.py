class Cat(object):
    def say(self):
        print("i am a cat")


class Dog(object):
    def say(self):
        print("i am a fish")


class Duck(object):
    def say(self):
        print("i am a duck")


animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()

dog = Dog()
a = ["bobby1", "bobby2"]
b = ["bobby2", "bobby"]
name_tuple = ["bobby3", "bobby4"]
name_set = set()
name_set.add("bobby5")
name_set.add("bobby6")
a.extend(name_set)
print(a)
