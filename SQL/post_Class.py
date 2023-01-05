import psycopg2

class PostgreSqll:
    def __init__(self) -> None:
        self.connect = psycopg2.connect(  # Подключение к БД Postgre
            database='python',  # Название БД
            user='postgres',  # Имя пользователя
            password='12345678',  # Пароль от пользователя
            host='localhost',  # Путь к БД (localhost) (127.0.0.1)
            port='5432'
        )

    def receiving_data(self, string: str) -> str:
        self.cur = self.connect.cursor()
        self.cur.execute(string)
        return self.cur.fetchall()


if __name__ == '__main__':
    con = PostgreSqll()
    print(type(con))
    data = con.receiving_data('SELECT * FROM employee')
    print(data)