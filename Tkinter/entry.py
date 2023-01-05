import tkinter as tk

# Выводит в консоль если окно чистое то get entry или что там написано
def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print('get entry')

# Очищает Entry с 0 позиции до последней (позиции можно задавать)
def delete_entry():
    name.delete(0, tk.END)

win = tk.Tk()
win.title('first window')
win.geometry('420x300+200+200')

tk.Label(text='name').grid(row=0, column=0, sticky='w')
tk.Label(text='password').grid(row=1, column=0, sticky='w')

name = tk.Entry(win)
name.grid(row=0, column=1)
password = tk.Entry(show='*')   # Скрыть ввод пароля show='*'
password.grid(row=1, column=1)

tk.Button(text='get', command=get_entry).grid(row=2, column=0, sticky='we')
tk.Button(text='delete', command=delete_entry).grid(row=2, column=1, sticky='we')
tk.Button(text='вставляем', command=lambda : name.insert(0, 'hello')).grid(row=2, column=2, sticky='we')

win.grid_columnconfigure(0, minsize=200)
win.grid_columnconfigure(1, minsize=100)
win.grid_columnconfigure(2, minsize=100)

win.mainloop()