class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old
 
    def set_old(self, old):
        self.__old = old
        
# Создаем объект property (при считывании данных вызывает get_old а при выводе set_old):
    old = property(get_old, set_old)


p = Person('Сергей', 20)

p.old = 35
print(p.old, p.__dict__)