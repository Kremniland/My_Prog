import tkinter as Tkinter
def clear():
    # Удаление предыдущего окна, чтобы окна не наслаивались одно на другое
    if frm.winfo_children():
        frm.winfo_children()[0].destroy()
def gotomenu1():
    u"""Построение кнопки первого меню"""
    clear()
    btn = Tkinter.Button(frm, text=u"Кнопка первого меню", width=30)
    btn.place(relx=0.5, rely=0.5, anchor="center")
def gotomenu2():
    u"""Построение кнопки второго меню"""
    clear()
    btn = Tkinter.Button(frm, text=u"Кнопка второго меню", width=30)
    btn.place(relx=0.5, rely=0.5, anchor="center")
root = Tkinter.Tk()
root.geometry("400x400+100+100")
MB = Tkinter.Menu(root)
MN = Tkinter.Menu(MB)
MN.add_command(label=u"Первое окно", command=gotomenu1)
MN.add_command(label=u"Второе окно", command=gotomenu2)
MB.add_cascade(label=u"Выбор окна", menu=MN)
root.config(menu=MB)
frm = Tkinter.Frame(root, width=400, height=400, bg="red")
frm.pack()
root.focus_force()
root.mainloop()