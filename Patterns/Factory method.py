class Can:  # Абстрактный класс Баночка
    def open(self):
        raise NotImplementedError


class VendingMachine:  # Абстрактный класс Автомат по выдаче газировке
    def choose_can(self, number):
        raise NotImplementedError()


class CocaCola(Can):
    def open(self):
        print("пшшшшшшш")


class Pepsi(Can):
    def open(self):
        print("пссссссссссссссс")


class MyVending(VendingMachine):
    def choose_can(self, text):
        if text == "CocaCola":
            return CocaCola()
        elif text == "Pepsi":
            return Pepsi()


vend = MyVending()
my_can = vend.choose_can("Pepsi")
print(my_can)
my_can.open()

my_can_2 = vend.choose_can("Pepsi")

print(id(my_can))
print(my_can)

print(id(my_can_2))
print(my_can_2)