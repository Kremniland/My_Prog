import tkinter as tk

root = tk.Tk()

root.title('Текст')
root.geometry('500x400+1000+200')

# Checkbutton
tf1 = tk.IntVar()
tf2 = tk.IntVar()

tk.Checkbutton(text='True/False', variable=tf1).pack()
tk.Checkbutton(text='1/0', variable=tf2).pack()

tk.Label(textvariable=tf1).pack()
tk.Label(textvariable=tf2).pack()

#RadioButton
rb = tk.IntVar()

tk.Radiobutton(text='Доставка курьером', value=1, variable=rb).pack()
tk.Radiobutton(text='Доставка почтой', value=2, variable=rb).pack()
tk.Radiobutton(text='Самовывоз', value=3, variable=rb).pack()

tk.Label(textvariable=rb).pack()

root.mainloop()
