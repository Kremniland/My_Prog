import psycopg2
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title('Подключение к БД')
root.geometry('500x400+1000+200')

frame_main = tk.LabelFrame(root, text='Строка подключения')
frame_main.pack()

dbname = tk.StringVar()
user = tk.StringVar()
password = tk.StringVar()
host = tk.StringVar()
port = tk.StringVar()

con_el = [  # Вывод (label), переменная (entry), значение по умолчанию (entry)
    ('БД', dbname, 'python'),
    ('Пользователь', user, 'postgres'),
    ('Пароль', password, ''),
    ('Хост', host, 'localhost'),
    ('Порт', port, '5432'),
]

font_size = "Calibri 24"

for item in con_el:
    frame = tk.Frame(frame_main)
    frame.pack(side='top')

    # 1 - способ
    # tk.Label(frame, text=item[0], font=font_size).pack(side='left')
    # if item[1] != password:
    #     tk.Entry(frame, textvariable=item[1], font=font_size).pack(side='left')
    # else:
    #     tk.Entry(frame, show='*', textvariable=item[1], font=font_size).pack(side='left')

    # 2 - способ
    tk.Label(frame, text=item[0], font=font_size).pack(side='left')
    entry = tk.Entry(frame, textvariable=item[1], font=font_size)

    if item[1] == password:
        entry.config(show='*')

    entry.pack(side='left')

    item[1].set(item[2])

connection = None


def connect_to_postgre():
    global connection
    try:
        connection = psycopg2.connect(
            database=dbname.get(),
            host=host.get(),
            port=port.get(),
            user=user.get(),
            password=password.get()
        )
    except psycopg2.OperationalError as e:
        messagebox.showerror(message=f'Подключиться к базе данных не удалось\n{e}')
    except Exception as e:
        messagebox.showerror(message=f'Что-то пошло не так\n{e}')
    else:
        messagebox.showinfo(message=f'Вы успешно подключились к базе данных')
        # connection.close()
        return connection


tk.Button(frame_main, text='Подключение к БД', font=font_size, command=connect_to_postgre).pack()

frame_second = tk.LabelFrame(root, text="SQL запрос")
frame_second.pack()

SQL_query = tk.StringVar()

tk.Entry(frame_second, font=font_size, textvariable=SQL_query).pack()


def exec_query():
    global connection
    try:
        curs = connection.cursor()
        curs.execute(SQL_query.get())
    except Exception as e:
        messagebox.showerror(message=e)
        connection.rollback()
        curs.close()
    else:
        messagebox.showinfo(message='Запрос был выполнен')
        connection.commit()
        curs.close()


tk.Button(frame_second,text='Выполнить запрос', font=font_size, command=exec_query).pack()

root.mainloop()
