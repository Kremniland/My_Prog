import tkinter as tk

root = tk.Tk()

root.title('Текст')
root.geometry('500x400+1000+200')

btn_r = tk.Button(text='Нажми на меня', bg='#FF0000', fg='#000000')
btn_g = tk.Button(text='Нажми', bg='#00FF00', fg='#000000')
btn_b = tk.Button(text='Python', bg='#0000FF', fg='#FFFFFF')

# btn_r.pack()
# btn_g.pack()
# btn_b.pack()

# btn_r.pack(expand=True)
# btn_g.pack(expand=True, fill='both')
# btn_b.pack(fill='y')

# expand (False) [True] - Будет ли элемент заполнять всё пространство
# fill (None) [x,y,both] - Будет ли элемент расстягиваться

# btn_r.pack(side='bottom')
# btn_g.pack(side='right')
# btn_b.pack(side='top')

# side (top) [right,left,bottom] - расположение элемента

# btn_r.pack(expand=True, anchor='center')
# btn_g.pack(expand=True, anchor='sw')
# btn_b.pack(expand=True, anchor='e')

# PLACE

# btn_r.place(height=50, width=100, x=100, y=40)
# btn_g.place(relx=0.2, rely=0.5)
# btn_b.place(relheight=0.4, relwidth=0.6)

# GRID

# btn_r.grid(column=0,row=1)
# btn_g.grid(column=2,row=2)
# btn_b.grid(column=1,row=0)

for i in range(4):
    for j in range(4):
        tk.Button(text='{}-{}'.format(i, j), width=7, height=3).grid(row=i, column=j, padx=4, pady=4)

tk.Button(text='columnspan', width=10, height=7).grid(column=0, row=4, columnspan=2, rowspan=2)
tk.Button(text='rowspan', width=10, height=10).grid(column=3, row=4,rowspan=2)

# Растянет кнопки по высоте и длинне win
# for i in range (3):
#     root.grid_columnconfigure(index=i, weight=1)
#     root.grid_rowconfigure(index=i, weight=1)
    
# Создаем кнопки 3 Х 3 в окне
# for i in range(3):
#     for j in range(3):
#         tk.Button(win, text=f'bt {i} {j}').grid(row=i, column=j, sticky='nswe', ipadx=6, ipady=6, padx=4, pady=4)

root.mainloop()
