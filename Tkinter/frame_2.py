from tkinter import *
from tkinter import ttk

def create_frame(label_text):
    frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
    # добавляем на фрейм метку
    label = ttk.Label(frame, text=label_text)
    label.pack(anchor=NW)
    # добавляем на фрейм текстовое поле
    entry = ttk.Entry(frame)   
    entry.pack(anchor=NW)
    # возвращаем фрейм из функции
    return frame

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

name_frame = create_frame("Введите имя")
name_frame.pack(anchor=NW, fill=X, padx=5, pady=5)

email_frame = create_frame("Введите email")
email_frame.pack(anchor=NW, fill=X, padx=5, pady=5)

root.mainloop()