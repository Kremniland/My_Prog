class Transport:
    def __init__(self, engine: str, mass: int, size: list, count_wheel: int, type_wheel: str):
        # Установка типов данных (: str)
        self.engine = engine
        self.mass = mass
        self.size = size
        self.count_wheel = count_wheel
        self.type_wheel = type_wheel

    def start_engine(self):
        print("Запуск двигателя")
        print(self.engine, "запущен")

    def stop_engine(self):
        print("Остановка двигателя")
        print(self.engine, "заглушен")

    def get_size(self) -> list:  # Возвращаемый тип данных list
        return self.size


class Car(Transport):
    pass


class Truck(Transport):
    pass


class Plane(Transport):
    pass


car_nissan = Car("V6", 1950, [2, 1.5, 1.6], 4, "Городские")

truck_man = Truck("V12", 4760, [5, 1.8, 2.7], 6, "Грузовые")

plane_boeing = Plane("Авиационный", 10760, [19, 10, 6], 24, "Посадочные")

# AutoService c полиморфизмом
class AutoServicePoly:
    def TO(self, transport: Transport):  # апкаст до родительского класса
        print("Проводится проверка ", transport)
        

IVAN_autoservice = AutoServicePoly()

IVAN_autoservice.TO(car_nissan)  # Код выполнен успешно
IVAN_autoservice.TO(truck_man)  # Код выполнен успешно
IVAN_autoservice.TO(plane_boeing)  # Код выполнен успешно