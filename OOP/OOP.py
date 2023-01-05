"""
digit = 75  # Динамическая типизация (Python)
# Integer digit = 81.5  # Статическая типизация
# String text = "ABC 890"  # Статическая типизация

# Строгая типизация (Python)
print(5 + 6)  # int с int
# print(5 + "abc") # int с string
print(5 + 8.6)  # int с float
print("Python" * 6)  # int с string (исключение)
# Не строгая типизация
# print(72 + "OOP") # int с string - 72OOP
# 2 + "2" = "22"
# 2 + "2" = 4

print(type(digit))
"""


class Car:  # Класс [Чертеж]
    def __init__(self, color_out, price, weight):  # Конструктор [Установка начальных свойств]
        self.color = color_out  # self.color - свойство color для объекта car,
        # color_out - посредник для передачи данных
        # public color
        self.price = price  # public price

        self.__weight = weight  # private weight - скрывает переменную weight

    def display(self):  # Метод [Способ взаимодействие с объектом]
        print("Hello, i'm a Car")

    def display_par(self, text):  # Метод [Способ взаимодействие с объектом]
        print("Hello,", text)

    def display_all(self):  # Метод [Способ взаимодействие с объектом]
        print("Цвет:", self.color)
        print("Цена:", self.price)

    def default_color(self):  # Метод [Способ взаимодействие с объектом]
        self.color = "Металлический"

    def get_weight(self):  # get - получить значение
        return self.__weight

    def set_weight(self, new_weight):  # set - задать значение
        self.__weight = new_weight


toyota = Car("Серый", 1000000, 1.5)  # Создание экземпляра класса (Объект)
# [Конкретный материальный объект, с которым можем поработать]
bmv = Car("Черный", 5000000, 1.76)  # Создание экземпляра класса (Объект)

print("Toyota")
toyota.display_all()

print("BMV")
bmv.display_all()

print("Вывод свойств Toyota")
print(toyota.color)
print(toyota.price)

toyota.price = 2000000

toyota.display_all()

print("Изменение цвета")
toyota.default_color()  # Вызов метода по смене цвета
bmv.default_color()  # Вызов метода по смене цвета

print("Toyota")
toyota.display_all()  # Атрибут color изменился на металлический

print("BMV")
bmv.display_all()  # Атрибут color изменился на металлический

print("Toyota Вес:", toyota.get_weight())  # Получение значения приватного атрибута
print("BMV Вес:", bmv.get_weight())  # Получение значения приватного атрибута

toyota.set_weight(1.65)  # Установка нового значение weight

print("Toyota Вес:", toyota.get_weight())  # Получение нового значения приватного атрибута


# C (Без инкапсуляции)
class Home:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def size(self, a, b):
        return a * b


zavod = Home(20, 30)

house = Home(5, 10)

print(zavod.size(zavod.a, zavod.b)) # Сами подставляем значения

print(zavod.size(house.a, zavod.b))


# Python (С инкапсуляцией) реализуется через переменную self. self - хранит конкретный объект

class Home_inc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def size(self):
        return self.a * self.b


zavod = Home_inc(20, 30)

house = Home_inc(5, 10)

print(zavod.size())  # значение возьмет метод size через переменную self

print(house.size())


# print(type(toyota))  # Вывод типа объекта
# print(type(bmv))  # Вывод типа объекта
#
# print(id(toyota))
# print(id(bmv))
#
# print(toyota)
# print(bmv)
#
# toyota.display()  # Вызов метода
# bmv.display()  # Вызов метода
#
# toyota.display_par("Toyota")  # Вызов метода
# bmv.display_par("BMV")  # Вызов метода
