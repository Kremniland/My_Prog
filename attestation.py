import tkinter as tk
from tkinter import messagebox

import Modul_DB as db

FontSize = 'Arial 20'


class StartWindow:
    def __init__(self, title='Start window') -> None:
        # Вывод первого входного окна:
        self.root = tk.Tk()
        self.root.title(title)
        self.label_login = tk.Label(self.root, text='Login: ', font=FontSize)
        self.label_login.grid(row=0, column=0)
        self.ent_login = tk.Entry(self.root, font=FontSize, bd=3)
        self.ent_login.grid(row=0, column=1)
        self.label_pass = tk.Label(self.root, text='Password: ', font=FontSize)
        self.label_pass.grid(row=1, column=0)
        self.ent_pass = tk.Entry(self.root, font=FontSize, show='*', bd=3)
        self.ent_pass.grid(row=1, column=1)
        self.btn_input = tk.Button(
            self.root, text='Enter', font=FontSize, command=self.enter_magazine, bd=3)
        self.btn_input.grid(columnspan=2, sticky='we')
        self.btn_input = tk.Button(
            self.root, text='Register', font=FontSize, command=self.registration, bd=3)
        self.btn_input.grid(columnspan=2, sticky='we')

# Принимает логин и пароль при входе
    def enter_magazine(self):
        login = self.ent_login.get()
        password = self.ent_pass.get()
        enter = db.reg_input(login, password)
        if enter == 'Error':
            messagebox.showerror('Error', 'No registration')
        # Переходим в окно магазина для пользователя
        elif enter == 'User':
            self.user_magazine()
        # Переходим в окно администратора
        elif enter == 'Admin':
            self.admin_win_start()
        
# Открывает дочернее окно для регистрации
    def registration(self):
        self.root.withdraw()
        self.root.regist = ChieldWindow(self.root, title='Registration')

        self.firstname = tk.StringVar()
        self.patronymic = tk.StringVar()
        self.lastname = tk.StringVar()
        self.log_registr = tk.StringVar()
        self.pass_registr = tk.StringVar()

        list_registr = [
            ('Lastname: ', self.lastname),
            ('Firstname: ', self.firstname),
            ('Patronymic: ', self.patronymic),
            ('Login: ', self.log_registr),
            ('Password: ', self.pass_registr),
        ]
        count_row = 0

        for item in list_registr:
            tk.Label(self.root.regist.root, text=item[0], font=FontSize).grid(row=count_row, column=0)
            tk.Entry(self.root.regist.root, textvariable=item[1], font=FontSize, bd=3).grid(row=count_row, column=1)
            if item[0]=='Password: ':
                tk.Entry(self.root.regist.root, textvariable=item[1], show='*', font=FontSize, bd=3).grid(row=count_row, column=1)
            count_row += 1
            
        self.btn_registr = tk.Button(
            self.root.regist.root, text='Registration', font=FontSize, command=self.save_registration, bd=3)
        self.btn_registr.grid(columnspan=2, sticky='we')
        # Закрывает главное окно при закрытии дочернего:
        self.root.regist.root.protocol(
            "WM_DELETE_WINDOW", lambda: self.root.destroy())

# принимает значения введенные при регистрации, заносит в бд:
    def save_registration(self):
        try:
            db.registration(self.firstname.get(), self.patronymic.get(), self.lastname.get(), self.log_registr.get(), self.pass_registr.get())
        except Exception:
            messagebox.showerror('Error', 'Error')
        else:
            messagebox.showinfo('Ok', 'Save ok!')
            # Закрываем окно регистрации:
            self.root.regist.root.withdraw()
        self.user_magazine()

# Окно магазина для пользователя:
    def user_magazine(self):
        self.root.withdraw()
        self.root.user = ChieldWindow(self.root, title='Magazine')
        lst_phone = [('Model', 'Size memory', 'Size RAM', 'Processor')]
        for i in db.telephone():
            lst_phone.append(i)
        count_row = 0
        for phone in lst_phone:
            count_column = 0
            for j in phone:
                tk.Label(self.root.user.root, text=j, font=FontSize, bg='#C0C0C0').grid(row=count_row, column=count_column, sticky='we', padx=3, pady=3)
                count_column += 1
            count_row += 1
        # Закрывает главное окно при закрытии дочернего:
        self.root.user.root.protocol(
            "WM_DELETE_WINDOW", lambda: self.root.destroy())
    
# Окно адмистратора:
    def admin_win_start(self):
        self.root.withdraw()
        self.root.admin_magazine = ChieldWindow(self.root, title='Admin magazine')
        lst_phone = [('Model', 'Size memory', 'Size RAM', 'Processor')]
        for i in db.telephone():
            lst_phone.append(i)
        count_row = 0
        for phone in lst_phone:
            count_column = 0
            for j in phone:
                tk.Label(self.root.admin_magazine.root, text=j, font=FontSize, bg='#C0C0C0').grid(row=count_row, column=count_column, sticky='we', padx=3, pady=3)
                count_column += 1
            count_row += 1
        # Закрывает главное окно при закрытии дочернего:
        self.root.admin_magazine.root.protocol(
            "WM_DELETE_WINDOW", lambda: self.root.destroy())
        
# Запуск главного окна:
    def run_window(self):
        self.root.mainloop()


# Класс дочернего окна, где parent - родительское окно
class ChieldWindow:
    def __init__(self, parent, title='MyChield') -> None:
        self.root = tk.Toplevel(parent)
        self.root.title(title)


if __name__ == '__main__':
    win = StartWindow()
    win.run_window()
