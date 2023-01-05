'''
Реализовать класс Телефон с паттерном Строителя (Builder)
У телефон есть такие компоненты как Аккумулятор, Экран, Процессор, Память, Микрофон.
Аккумулятор имеет атрибут Емкости.
Экран имеет атрибут Длина и ширина экрана, Тип экрана (TN, IPS, OLED и т.д.)
Процессор имеет атрибут Название процессора.
Память имеет атрибут Размер памяти.
Микрофон имеет атрибут Частотный диапазон.
С помощью работника собирается телефон из частей и создаётся объект Телефон.
Класс Телефон в себе содержит атрибут уникальный идентификатор (можно создать с помощью рандома), дата изготовления и цену.
Также телефон должен выводить всю информацию о себе и о компонентах из которых он состоит.
Работник в себе содержит атрибут ФИО.
'''

class Accumulator:
    def __init__(self, capacity):
        self.capacity = capacity


class Screen:
    def __init__(self, size, type_screen):
        self.size = size
        self.type_screen = type_screen


class Processor:
    def __init__(self, name):
        self.name = name


class Memory:
    def __init__(self, storage):
        self.storage = storage


class Microphone:
    def __init__(self, frequency):
        self.frequency = frequency


class Employee:
    def build_accumulator(self, capacity):
        raise NotImplementedError()

    def build_screen(self, size, type_screen):
        raise NotImplementedError()

    def build_processor(self, name):
        raise NotImplementedError()

    def build_memory(self, storage):
        raise NotImplementedError()

    def build_microphone(self, frequency):
        raise NotImplementedError()


class Telephone:
    def __init__(self, id, date_create, price, accumulator, screen, processor, memory, microphone):
        self.ID = id
        self.date_create = date_create  
        self.price = price  
        self.accumulator = accumulator  
        self.screen = screen  
        self.processor = processor  
        self.memory = memory  
        self.microphone = microphone 

    def __str__(self):
        return f"Емкость аккумулятора: {self.accumulator.capacity}" \
               f"\nРазмер и тип экрана: {self.screen.size} {self.screen.type_screen}" \
               f"\nНазвание процессора: {self.processor.name}" \
               f"\nРазмер памяти: {self.memory.storage}" \
               f"\nЧастотный диапазон микрофона: {self.microphone.frequency}"


class TelephoneEmployee(Employee):
    def __init__(self, FIO):
        self.FIO = FIO

    def build_accumulator(self, capacity):  # Метод создания аккумулятора
        return Accumulator(capacity)

    def build_screen(self, size, type_screen):  # Метод создания экрана
        return Screen(size, type_screen)

    def build_processor(self, name):    # Метод создания процессора
        return Processor(name)

    def build_memory(self, storage):    # Метод создания памяти
        return Memory(storage)

    def build_microphone(self, frequency):  # Метод создания микрофона
        return Microphone(frequency)
                                            # Метод создания телефона:
    def create_telephone(self, id, create_date, price, capacity, size, type_screen, name, storage, frequency):
        accumulator = self.build_accumulator(capacity)
        screen = self.build_screen(size, type_screen)
        processor = self.build_processor(name)
        memory = self.build_memory(storage)
        microphone = self.build_microphone(frequency)
        return Telephone(id, create_date, price, accumulator, screen, processor, memory, microphone)


Oleg = TelephoneEmployee("Робертов Олег Николаевич")

samsung = Oleg.create_telephone(72284, "10.10.2022", 14000,  
                                3400,  
                                [16, 8], "OLED",  
                                "Snapdragon 400",  
                                512,  
                                [14, 16000]  
                                )

print("Телефон:", samsung)
print("Аккумулятор:", samsung.accumulator)
print("Емкость аккумулятора:", samsung.accumulator.capacity)
print("Процессор:", samsung.processor)
print("Название процессора:", samsung.processor.name)

print(samsung.__dict__)
