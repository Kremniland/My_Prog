import tkinter as tk

class Window:
    def __init__(self, title='MyWindow', width=200, height=200) -> None:
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f'{width}x{height}+200+200')

# Запуск главного окна:
    def run_window(self):
        self.root.mainloop()

# Вызов дочернего окна через ф-ию:
    def create_chield(self):
        ChieldWindow(self.root)

# Скрыть главное окно:
    def withdraw_window(self):
        self.root.withdraw()

# Класс дочернего окна, где parent - родительское окно
class ChieldWindow:
    def __init__(self, parent, title='MyChield', width=200, height=200) -> None:
        self.root = tk.Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f'{width}x{height}+400+400')

# Скрыть дочернее окно:
    def withdraw_chield(self):
        self.root.withdraw()

if __name__ == '__main__':
    win = Window()
    # win.create_chield()
    chield = ChieldWindow(win.root, title='1', width=400, height=400)

    ent = tk.Entry(chield.root).pack()
    tk.Button(chield.root, text='click me').pack()


    win.run_window()
