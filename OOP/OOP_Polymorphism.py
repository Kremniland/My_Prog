print("Hello polymorphism")
print(782 + 82.3)
print(72)

# C#
def some_func(int digit,string text): # 1 сигнатура (int,string)
    pass

def some_func(int digit): # 2 сигнатура (int)
    pass

def some_func(string text): # 3 сигнатура (string)
    pass

def some_func(float number): # 4 сигнатура (float)
    pass

def some_func(int num): # 5 сигнатура (int) # Ошибка из-за совпадения со 2 сигнатурой
    pass

# Polymorphism

class Person:
    pass

class Student(Person):
    pass

class Employee(Person):
    def poly_stud(self, student): # сигнатура (student)
        pass

    def poly_volu(self, volunteer): # сигнатура (volunteer)
        pass

    def poly(self, person): # сигнатура (person) Полиморфизм
        pass

class Volunteer(Person):
    pass

per = Person()
stud = Student()
emp = Employee()
volu = Volunteer()

emp.poly_stud(stud) # Код выполнится успешно
emp.poly_stud(per) # Код выполнится с ошибкой

emp.poly_volu(volu) # Код выполнится успешно
emp.poly_volu(stud) # Код выполнится с ошибкой

emp.poly(per) # Код выполнится успешно
emp.poly(stud) # Код выполнится успешно
emp.poly(emp) # Код выполнится успешно
emp.poly(volu) # Код выполнится успешно
