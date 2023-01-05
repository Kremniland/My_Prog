class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old
 # Перед геттером (обратите внимание, именно перед геттером, а не сеттером или делитером) 
 # рописывается декоратор:
    @property
    def old(self):
        return self.__old
 
    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old


p = Person('Виталий', 20)
# Вызов сеттера:
print(p.old)
# Вызов геттера:
p.old = 35
print(p.old)
# Вызов делитера:
del p.old
