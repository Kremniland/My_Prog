# Пример @classmethod и @staticmethod:

class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if Vector.validate(x) and Vector.validate(y): # обращаемся к методу класса через Vector,
                                                      # но можем через self
            self.x = x
            self.y = y
        # print(Vector.norm2(self.x, self.y))       # вызов статик метода, бращаемся через Vector
        print(self.norm2(self.x, self.y))           # вызов статик метода в классе,через self

    @staticmethod # Здесь нет никаких скрытых параметров
    def norm2(x, y):
        return x*x + y*y

v = Vector(10, 20)
print(v.norm2) # вызов статик метода объектом класса
res = Vector.validate(5) # вызов метода validate(), не создавая никаких объектов
print(res)
res = Vector.norm2(5, 6) # вызов статик метода вне класса
print(res)
