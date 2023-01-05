import psycopg2

# Возвращает подключение к БД
def connect_db():
    try:
        connection = psycopg2.connect(
            database='python',  # Название БД
            user='postgres',  # Имя пользователя
            password='12345678',  # Пароль от пользователя
            host='localhost',  # Путь к БД (localhost) (127.0.0.1)
            port='5432'
        )
    except psycopg2.OperationalError as e:
        print(f'Что то пошло не так  {e}')
    except Exception as e:
        print(f'ERROR ! {e}')
    return connection

# Принимает подключение к БД
def select_db(connect):
    curs = connect.cursor()
    curs.execute('SELECT * FROM employee')
    print(curs.fetchall())
    curs.close()


if __name__ == '__main__':
# Получение подключения к БД из ф-ии:
    connect = connect_db()
# Передача подключения к БД в ф-ию:
    select_db(connect)

    connect.commit()
    connect.close()

