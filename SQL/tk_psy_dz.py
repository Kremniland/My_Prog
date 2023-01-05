import tkinter as tk
from tkinter import messagebox
import psycopg2

root = tk.Tk()
root.geometry('450x600+600+100')
root.title('БД')

frame_main = tk.LabelFrame(root, text='Ввод данных подключения:')
frame_main.pack()

dbname = tk.StringVar()
user = tk.StringVar()
password = tk.StringVar()
host = tk.StringVar()
port = tk.StringVar()

con_el = [
    ('БД', dbname, 'python'),
    ('Пользователь', user, 'postgres'),
    ('Пароль', password, ''),
    ('Хост', host, 'localhost'),
    ('Порт', port, '5432'),
]

font_size = "Calibri 20"
activ_button = tk.NORMAL

count_row = 0

for item in con_el:
    tk.Label(frame_main, text=item[0], font=font_size, anchor='w').grid(row=count_row, column=0, sticky='we')
    entry = tk.Entry(frame_main, textvariable=item[1], font=font_size, justify= tk.LEFT, bd=3)
    if item[1] == password:
        entry.config(show='*')
    entry.grid(row=count_row, column=1)
    count_row+=1
    item[1].set(item[2])

def bd_connect():
    global connection
    try:
        connection = psycopg2.connect(
            database=dbname.get(),
            user=user.get(),
            password=password.get(),
            host=host.get(),
            port=port.get()
        )
    except psycopg2.OperationalError as e:
        messagebox.showerror(message=f'Подключиться к базе данных не удалось\n{e}')
    except Exception as e:
        messagebox.showerror(message=f'Что-то пошло не так\n{e}')
    else:
        messagebox.showinfo(message=f'Вы успешно подключились к базе данных')
        

tk.Button(frame_main, text='connect', command=bd_connect, font=font_size, bd=5).grid(columnspan=2, sticky='we')

#--------------------------------second_frame-----------------------------------------------

second_frame = tk.LabelFrame(root, text='SQL qwery')
second_frame.pack()

SQL_qwery = tk.StringVar()

def exec_qwery():
    global connection
    try:
        curs = connection.cursor()
        curs.execute(SQL_qwery.get())        
    except Exception as e:
        messagebox.showerror(message=f'что то не так\n {e}')
        connection.rollback()
        curs.close()
    else:
        messagebox.showinfo(message='Все ок!')
        print(curs.fetchall())
        connection.commit()
        curs.close()


tk.Entry(second_frame, textvariable=SQL_qwery, font=font_size).pack()
tk.Button(second_frame, font=font_size ,text='Выполнить запрос', command=exec_qwery).pack()

#---------------------------------second_root--------------------------------

input_frame = tk.LabelFrame(root, text='Input window')
input_frame.pack()

first_name = tk.StringVar()
family = tk.StringVar()
salary = tk.StringVar()

input_lst = [
            ('Имя', first_name),
            ('Фамилия', family),
            ('Оклад', salary)
            ]

count_input_row = 0

for i in input_lst:
    tk.Label(input_frame, text=i[0], font=font_size).grid(row=count_input_row,column=0, sticky='we')
    tk.Entry(input_frame, textvariable=i[1], font=font_size).grid(row=count_input_row, column=1, sticky='we')
    count_input_row+=1

def insert_employee():
    global connection
    try:
        curs = connection.cursor()
        curs.execute('INSERT INTO employee (firstname, name, salary) VALUES (%s,%s,%s)',
        (family.get(), first_name.get(), salary.get()))
    except Exception as e:
        messagebox.showerror(message=f'ERROR {e}')
        connection.rollback()
        curs.close()
    else:
        messagebox.showinfo(message='Все ок!')
        connection.commit()
        curs.close()
    
tk.Button(input_frame, text='Ввести запись', font=font_size, command=insert_employee).grid(columnspan=2, sticky='we')

root.mainloop()