class Point:
# Создаем приватный класс метод __check_value, доступа из вне к нему нет:
    @classmethod
    def __check_value (cls, x):
        return type(x) in (int, float)
# Инициализируем __x и __y и через метод __check_value 
# проверяем на правильность ввода только цифры:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
 
        if self.__check_value (x) and self.__check_value (y):
            self.__x = x
            self.__y = y
# менятет локальные свойства __x и __y экземпляра класса и через метод __check_value 
# проверяем на правильность ввода только цифры:
    def set_coord(self, x, y):
        if self.__check_value (x) and self.__check_value (y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")
# возвращает локальные свойства __x и __y экземпляра класса:
    def get_сoord(self):
        return self.__x, self.__y


pt = Point(5, 5)
print(pt.set_coord(3, 4)) # Меняем __x и__y
print(pt.get_сoord())