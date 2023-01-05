import psycopg2

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


if __name__ == '__main__':
    connect = connect_db()
    curs = connect.cursor()
    curs.close()
    connect.commit()
    connect.close()
    print(connect)

