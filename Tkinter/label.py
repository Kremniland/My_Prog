import tkinter as tk

root = tk.Tk()

root.title('Текст')
root.geometry('500x400+1000+200')

lbl1 = tk.Label(root, text='Lable_1\nl2',
                bg ='red',
                fg='white',
                pady=20,
                padx=20,
                font=('Arial', 20, 'bold'),
                width=15,
                relief='raised',
                bd=10,
                justify=tk.LEFT
                )
lbl1.pack()

label_1 = tk.Label(text='Hello tkinter\nHello python\nHello',
                   font='Helvetic 36',
                   background='#faf',
                   foreground='#ef4',
                   height=4,
                   width=15,
                   justify='right')

label_1.pack()

label_2 = tk.Label(text='module Tkinter\nHTTP',
                   font='Calibri 16',
                   background='#000',
                   foreground='#fff',
                   height=6,
                   width=14,
                   justify='left')

label_2.pack()

root.mainloop()
