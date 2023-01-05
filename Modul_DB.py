import psycopg2

# Подключение к БД
def connect_db():
    try:
        connection = psycopg2.connect(  # Подключение к БД Postgre
            database='python',  # Название БД
            user='postgres',  # Имя пользователя
            password='12345678',  # Пароль
            host='localhost',  # или (127.0.0.1)
            port='5432'
        )
    except psycopg2.OperationalError as e:
        print(f'Подключиться к базе данных не удалось\n{e}')
    except Exception as e:
        print(f'Что-то пошло не так\n{e}')
    else:
        print('Вы успешно подключились к базе данных')
        # connection.close()
    return connection

# Проверка входа по логину и паролю:
def reg_input(log: str, pas: str)->str:
    try:
        con = connect_db()
        cur = con.cursor()
        cur.execute('SELECT login, pasword, administrate, exsist FROM register')
    except Exception:
        print('ERROR')
        cur.close()
        con.close()
    else:
        for l, p, a, e in cur.fetchall():
            if log.lower() == l.lower() and pas == p and e:
                if a == True:
                    registr = 'Admin'  # Если админ
                    break
                elif a == None:
                    registr = 'User'    # Если пользователь
                    break
            else:
                registr = 'Error'        # Если вход не выполнен
        cur.close()
        con.close()
    return registr

# Регистрация:
def registration(first_name: str, patronymic: str, last_name: str, login: str, pasword: str)->None:
    try:
        con = connect_db()
        cur = con.cursor()
        cur.execute('INSERT INTO register (first_name, patronymic, last_name, login, pasword) VALUES (%s,%s,%s,%s,%s)',
        (first_name, patronymic, last_name, login, pasword))
    except Exception:
        print('ERROR')
        cur.close()
        con.rollback()
        con.close
    else:
        cur.close()
        con.commit()
        con.close()

# Получение данных из базы телефонов:
def telephone():
    try:
        con = connect_db()
        cur = con.cursor()
        cur.execute('SELECT * FROM telephone')
    except Exception:
        print('ERROR')
        cur.close()
        con.close()
    else:
        list_phone = cur.fetchall()
        cur.close()
        con.close()
        return list_phone


if __name__ == '__main__':
    lst = [('Model', 'Size memory', 'Size RAM', 'processor')]
    for i in telephone():
        lst.append(i)
    print(lst)
# Вход по логину и паролю:
    # print(reg_input('Admin','1234'))
# -------------------------------------------------------------------------------------------
# Регистрация нового пользователя:
    # con = connect_db()
    # cur = con.cursor()
    # first_name = 'Elena'
    # patronymic = 'Petrova'
    # last_name = 'Semenovna'
    # login = 'User_4'
    # pasword = '1234'
    # registration(first_name, patronymic, last_name, login, pasword)
# -------------------------------------------------------------------------------------------------
# Новая запись в БД через execute:
    # con = connect_db()
    # cur = con.cursor()
    # cur.execute('INSERT INTO register (first_name, patronymic, last_name, login, pasword) VALUES (%s,%s,%s,%s,%s)',
    # (first_name, patronymic, last_name, login, pasword))
    # cur.execute('SELECT * FROM register')
    # print(cur.fetchall())
    # con.commit()
#--------------------------------------------------------------------------------------------------------