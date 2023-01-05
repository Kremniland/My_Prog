class Point:
    MAX_COORD = 100
    MIN_COORD = 0
 
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
# автоматически вызывается, когда идет считывание атрибута через экземпляр класса: 
    def __getattribute__(self, item):
        print("__getattribute__")
        return object.__getattribute__(self, item)
# явно запретим считывать такой атрибут из экземпляра класса:
    # def __getattribute__(self, item):
    #     if item == "_Point__x":
    #         raise ValueError("Private attribute")
    #     else:
    #         return object.__getattribute__(self, item)
# автоматически вызывается в момент присваивания атрибуту нового значения:
    def __setattr__(self, key, value):
        print("__setattr__")
        object.__setattr__(self, key, value)
    # запретим создание локального свойства с именем z:
    # def __setattr__(self, key, value):
    #         if key == 'z':
    #             raise AttributeError("недопустимое имя атрибута")
    #         else:
    #             object.__setattr__(self, key, value)
# автоматически вызывается, если идет обращение к несуществующему атрибуту:
    def __getattr__(self, item):
        print("__getattr__: " + item)
# при обращении к несуществующим атрибутам возвращается значение False, 
# а не генерируется исключение:
    # def __getattr__(self, item):
    #     return False
# вызывается в момент удаления какого-либо атрибута из экземпляра класса:
    def __delattr__(self, item):
        object.__delattr__(self, item)


pt1 = Point(1, 2)
print(pt1.MIN_COORD)