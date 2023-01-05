class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def say(self):
        print(f"Привет, я {self.name}, мне {self.age}, вешу {self.weight} кг, а рост {self.height} см")

    def get_age(self):
        return self.age

    def index_body(self):
        return self.weight / (self.height ** 2)

    def index_body_description(self):  # (Антон)
        index_body = self.index_body()
        if index_body < 16:
            print('Dystrophic')
        elif index_body < 18.5:
            print('Deficit')
        elif index_body < 25:
            print('Normal')
        elif index_body < 30:
            print('Fat')
        elif index_body < 35:
            print('Very fat')
        elif index_body < 40:
            print('Extremely fat')
        elif index_body > 40:
            print('U got a problems, bruh. Come to see a doctor.')


oleg = Person("Олег", 34, 1.87, 79.6)

oleg.say()

print(oleg.get_age())

print(oleg.index_body())

oleg.index_body_description()


class Student(Person):  # Наследование от класса Person
    def __init__(self, name, age, height, weight, university):  # Переопределение конструктора Student
        super().__init__(name, age, height, weight)  # Вызов конструктора Person
        self.university = university  # Создание нового свойства

    def process_homework(self):  # Создание новой функции для Student
        print(f"{self.name} сейчас занят, выполняет домашнее задание")

    def say(self):  # Переопределили метод say из класса Person
        print(f"{self.name} сегодня поучился в {self.university} и устал")


roma = Student("Рома", 24, 1.85, 71.1, "РЭУ им.Г.В.Плеханова")

roma.say()

print(roma.get_age())

print(roma.index_body())

roma.index_body_description()

roma.process_homework()


# Создание уникального свойства
# roma.university = "РЭУ им. Г.В. Плеханова"
#
# print(roma.university)
#
# henry = Student("Генри", 18, 1.74, 85.0)
# print(henry.university)
#

class Employee(Person):
    def work(self):  # Создание новой функции
        print(f"я {self.name} и я усердно работаю")

    def say(self):  # Переопределение say
        print(f"{self.name}, возраст {self.age}")

    def freindship(self, person):
        print(f"{self.name} дружит с {person.name}")


denis = Employee("Денис", 28, 1.85, 89.9)

denis.work()

print(oleg)
print(roma)
print(denis)

denis.freindship(oleg)
denis.freindship(roma)


class Spec(Employee):
    def kval(self):
        print("Я имею квалификацию")


nikita = Spec("Никита", 38, 1.96, 95.6)

nikita.kval()

nikita.work()

nikita.say()

print(nikita.index_body())


class Working_student(Student, Employee):
    def __init__(self, name, age, height, weight, university, work_place):
        super().__init__(name, age, height, weight, university)
        self.work_place = work_place


anna = Working_student("Анна", 19, 1.71, 61.7, "МГУ", "Чип и технологии")

print(anna.university)
print(anna.work_place)

anna.say()  # Унаследование от класса Student (т.к. стоит первый при наследовании)

anna.work()

anna.process_homework()


# Protected
class Engine:
    def __init__(self, name, size, model):
        self.name = name  # Public доступ - откуда угодно
        self._size = size  # Protected доступ - class Engine, Car, main
        self.__model = model  # Private доступ - class Engine

    def get_model(self):
        return self.__model


class Car(Engine):
    def info(self):
        print(self.name)
        print(self._size)
        # print(self.__model)

    def __str__(self):  # Переопределение вывода при вызове объекта print(mazda)
        return f"{self.name}, длина {self._size[0]}, ширина {self._size[1]}, высота {self._size[2]}"


mazda = Car("mazda v4", [50, 50, 70], "TXZ-71")
mazda.info()
print(mazda.name)
print(mazda._size)
mazda._size = [60, 60, 70]
print(mazda._size)

print(mazda) # Вызывается __str__

print(mazda.get_model())


# print(mazda.__model)


# C# - Перегрузка методов
class Test:
    def say(self):  # say()         - say()
        pass

    def say(self, text):  # say(text)     - say(string)
        pass

    def say(self, digit):  # say(digit)   - say(integer)
        pass

    def say(self, age):  # say(age)       - say(integer)
        pass
