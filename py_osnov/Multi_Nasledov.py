class Goods:
    def __init__(self, name, weight, price):

# Преопределение __init__ (к __init__ класса Goods добавится __init__ класса MixinLog):
        super().__init__()
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price
    
    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")

class MixinLog:
    ID = 0
 
    def __init__(self):
        print("init MixinLog")
        self.ID += 1
        self.id = self.ID
 
    def save_sell_log(self):
        print(f"{self.id}: товар продан в 00:00 часов")

class NoteBook(Goods, MixinLog):
    pass

# Выведет цепочку обхода базовых классов:
print(NoteBook.__mro__)

n = NoteBook("Acer", 1.5, 30000)

n.print_info()
n.save_sell_log()
