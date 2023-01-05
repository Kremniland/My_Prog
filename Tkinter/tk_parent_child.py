#------------------------------------------------------------------------------------------------------
import tkinter as tk
class my_root(tk.Tk):
    def __init__(self, val,  *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.param = val

root = my_root(7)


def next_window(root):

    root.withdraw()  # Скрыть окно
    second_window = tk.Toplevel()
    entry = tk.Entry(second_window).pack()
    tk.Button(second_window, text="окно 2", command=lambda: next_window_2(second_window)).pack()
    # При закрытии дочернего окна убиваем главное окно:
    second_window.protocol("WM_DELETE_WINDOW", lambda: root.destroy())
    # или так: second_window.protocol("WM_DELETE_WINDOW", root.destroy)

def next_window_2(second_window):
    
    second_window.withdraw()
    
    next_window_2 = tk.Toplevel()
    bt = tk.Button(next_window_2, text="окно 3").pack()
    next_window_2.protocol("WM_DELETE_WINDOW", lambda: root.destroy())

bt = tk.Button(root, text="Следующее окно", command=lambda: next_window(root))
bt.pack()
root.mainloop()

# Gureev Kirill, [29.10.2022 13:40]
# root.param=entry.get()

# Gureev Kirill, [29.10.2022 13:41]
# Внутри def next_windows

#--------------------------------------------------------------------------------------------------------
# from tkinter import Tk, Button, Label, IntVar
# class App(Tk):
# 	def __init__(self):
# 		super().__init__()
# 		self.value = IntVar()
# 		self.value.set(0)
# 		self.button = Button(self, command=lambda: self.value.set(self.value.get() + 1))
# 		self.button.pack()
# 		self.value_display = Label(self, textvariable=self.value)
# 		self.value_display.pack()
		
# a = App()
# a.mainloop()