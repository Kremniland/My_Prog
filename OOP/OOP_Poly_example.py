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


class Motocycle(Transport):
    pass


car_nissan = Car("V6", 1950, [2, 1.5, 1.6], 4, "Городские")
print(car_nissan)
print(car_nissan.engine)

truck_man = Truck("V12", 4760, [5, 1.8, 2.7], 6, "Грузовые")

plane_boeing = Plane("Авиационный", 10760, [19, 10, 6], 24, "Посадочные")

print(car_nissan is Transport)
print(truck_man is Transport)
print(plane_boeing is Transport)


# AutoService без полиморфизма
class AutoService:
    def TO_car(self, car: Car):
        print("Проводится проверка машины ", car)
        if car.count_wheel == 4:
            print("Проверка прошла успешно")
        else:
            print("Проверка не пройдена")

    def TO_truck(self, truck: Truck):
        print("Проводится проверка машины ", truck)
        if truck.type_wheel == "Грузовые":
            print("Проверка прошла успешно")
        else:
            print("Проверка не пройдена")


COG = AutoService()

COG.TO_car(car_nissan)  # Код выполнен успешно

COG.TO_truck(truck_man)  # Код выполнен успешно

COG.TO_truck(plane_boeing)  # Код выполнен с ошибкой


# AutoService c полиморфизмом
class AutoServicePoly:
    def TO(self, transport: Transport):  # апкаст до родительского класса
        print("Проводится проверка ", transport)
        if transport.mass >= 1000:
            print("Проверка массы пройдена")
        else:
            print("Проверка массы не пройдена")
        if transport is Car: # C# - проверка типа данных
            print("Это машина")


IVAN_autoservice = AutoServicePoly()

IVAN_autoservice.TO(car_nissan)  # Код выполнен успешно
IVAN_autoservice.TO(truck_man)  # Код выполнен успешно
IVAN_autoservice.TO(plane_boeing)  # Код выполнен успешно

moto_honda = Motocycle("Двухтактный", 710, [1, 0.7, 0.9], 2, "Гоночные")

IVAN_autoservice.TO(moto_honda)  # Код выполнен успешно
