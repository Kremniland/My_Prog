import psycopg2

connection = psycopg2.connect( # Подключение к БД Postgre
    database='python',  # Название БД
    user='postgres',  # Имя пользователя
    password='12345678',  # Пароль от пользователя
    host='localhost',  # Путь к БД (localhost) (127.0.0.1)
    port='5432'
)

print(connection)

# input('Впишите значение для продолжения')

curs = connection.cursor()

Q_createEmployee = """
CREATE TABLE IF NOT EXISTS employee (
    id SERIAL NOT NULL,
    firstname VARCHAR(50) NOT NULL,
    name VARCHAR(50) NOT NULL,
    salary INT NOT NULL
);
"""

Q_insertEmployee = """
INSERT INTO employee (firstname, name, salary) VALUES 
('Робертов', 'Алексей', 65000),
('Мантиева','Екатерина',68000);
"""

Q_selectEmployee = """
SELECT * FROM employee
"""

curs.execute(Q_selectEmployee)

# print("Вывод одной записи: ", curs.fetchone())
# print("Вывод одной записи: ", curs.fetchone())
# print("Вывод одной записи: ", curs.fetchone())

# print("Вывод N записей:", curs.fetchmany(2))

print("Вывод всех записей: ", curs.fetchall())

# name = input("Введите имя: ")
# firstname = input("Введите фамилию: ")
# salary = int(input("Введите оклад: "))

# curs.execute(
#     'INSERT INTO employee (firstname, name, salary) VALUES (%s,%s,%s)',
#     (firstname, name, salary)
#     # (variable,)
# )

curs.execute(Q_selectEmployee)
print("Вывод всех записей", curs.fetchall())

connection.commit()

curs.close()
connection.close()

print(connection)