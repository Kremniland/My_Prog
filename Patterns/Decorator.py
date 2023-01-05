class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print("Привет, я", self.name, ". Возраст:", self.age)

    def shout(self):
        print("AAAAAAAAAAA")


class Axe:
    def __init__(self, person):
        self.person = person

    def __getattr__(self, item):
        return getattr(self.person, item)

    def work(self):
        print("Рублю деревья и имя мне ", self.person.name)


john = Person("Джон", 29)
john.say()
# john.work()

AxeMan = Axe(john)
AxeMan.work()
AxeMan.say()
AxeMan.shout()