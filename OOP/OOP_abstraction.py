from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def eat(self):
        print("Кушает пищу")

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def voice(self, text):
        pass


# animal = Animal()
# animal.info()
# animal.eat()


class Dog(Animal):
    def info(self):
        print(self.name, "\n", self.mass)

    def voice(self, text):
        print("woof-woof", text)


henry = Dog("Henry", 7)

henry.info()
henry.voice("woof")
henry.eat()


class Cat(Animal):
    def info(self):
        print(self.name)

    def voice(self, text):
        print("prrrr", text)


lucy = Cat("Lucy", 4)

lucy.info()
lucy.voice("moew")
lucy.eat()

class IAnimal(ABC):
    @abstractmethod
    def voice(self, text):
        pass

    @abstractmethod
    def say(self):
        pass

class Fox(IAnimal):
    def voice(self,text):
        print(text)

    def say(self):
        print("wewewe")