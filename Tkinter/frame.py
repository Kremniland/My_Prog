import tkinter as tk

root = tk.Tk()

root.title('Текст')
root.geometry('500x400+1000+200')

frame_main = tk.LabelFrame(root, text='Главный контейнер')
frame_main.pack()

lbl = tk.Label(frame_main, text='Имя')
tb = tk.Entry(frame_main)

lbl.pack(side='left')
tb.pack(side='left')

frame_second = tk.Frame(root)

tk.Label(frame_second, text='Фамилия').pack(side='left')
tk.Entry(frame_second).pack(side='left')

frame_second.pack()

root.mainloop()
