import sqlite3 as sq
# Вариант 1
# так не рекомендуется работать:
# connect - устанавливает связь с БД, файл saper.db либо будет открыт, либо будет создан
# con = sq.connect('saper.db')
# создаем экземпляр класса Cursor, и в дальнейшем с ним работаем:
# cur = con.cursor()
# execute - принимает запрос к БД
# cur.execute('''
# ''')
# закрытие БД:
# cur.close()

# Вариант 2
# соединяться с БД лучше все-таки через менеджер контекста:
with sq.connect('saper.db') as con:
    cur = con.cursor()

# Удаление таблицы(IF EXISTS - если существует)
    # cur.execute("DROP TABLE IF EXISTS users")

# Создаем таблицу:
# IF NOT EXISTS - если таблица не создана, то создает ее
    # cur.execute("""CREATE TABLE IF NOT EXISTS users (
    #     user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     name TEXT NOT NULL,
    #     sex INTEGER NOT NULL DEFAULT 1,
    #     old INTEGER,
    #     score INTEGER NULL
    # )""")

# Заносим данные в таблицу:
# Первый способо:
    # cur.execute("INSERT INTO users VALUES(1, 'Михаил', 1, 19, 1000)")
    # cur.execute("INSERT INTO users VALUES (2, 'Vitaliy', 1, 43, 1000)")
    # cur.execute("INSERT INTO users VALUES (3, 'Lena', 2, 33, 200)")
# Второй способ:
    # cur.execute("INSERT INTO users (name, old, score) VALUES('Федор', 32, 200)")
    # cur.execute("INSERT INTO users (name, old, score) VALUES ('Oleg', 22, 400)")
    # cur.execute("INSERT INTO users(name, old) VALUES ('Denis', 38)")
# Заполнение через переменную:
    # data = [10, 'Mark', 1, 9, 1000]
    # cur.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?)", data)

# Вывод на экран используя fetchall():
#     cur.execute("SELECT name, old FROM users")
# Вывод всей выборки в виде списка кортежей:
    # result = cur.fetchall()
    # print(result)
# Вывод кортежей перебирая через цикл:
#     for result in cur:
#         print(result)
# Вывод на экран оборачивая переменную в list:
# Вывод с условием:
#     b = cur.execute("SELECT * FROM users WHERE score == 200")
#     print(list(b))
#     c = cur.execute("SELECT * FROM users WHERE score == 200 AND old == 33")
#     print(list(c))
#     d = cur.execute("SELECT * FROM users WHERE old IN (18,32) AND sex == 1")
#     print(list(d))
# fetchone() – возвращает первую запись
    # result = cur.fetchone()
# fetchmany(size) – возвращает число записей не более size
    # result2 = cur.fetchmany(2)
    # print(result)
    # print(result2)
# Объединение таблиц score и users по полям score.user_id = users.ROWID вывести поля name, sex, score.score
cur.execute('SELECT name, sex, score.score FROM score JOIN users ON score.user_id = users.ROWID;')
result = cur.fetchall()
print(result)

    