import tkinter as tk

from tkinter import messagebox

# import query_bd as bd

font_size = 'Calibri 18'

class MagazineStart(tk.Tk):
    def __init__(self, height=500, width=400):
        super().__init__()
        self.root = self
        self.root.title('Магазин телефонов')
        self.root.geometry('{}x{}+700+200'.format(height, width))
        self.label_frame_1 = tk.LabelFrame(self.root, text='Авторизация', font=font_size)
        self.label_frame_1.pack(padx=10, pady=10)
        self.login = tk.StringVar()
        self.password = tk.StringVar()
        self.authorization = [
            ('Логин', self.login, ''),
            ('Пароль', self.password, '')
        ]
        for i in self.authorization:
            self.frame_1 = tk.Frame(self.label_frame_1)
            self.frame_1.pack()
            self.label_1 = tk.Label(self.frame_1, text=i[0], font=font_size)
            self.label_1.pack(side='left')
            self.enter_1 = tk.Entry(self.frame_1, textvariable=i[1], font=font_size)
            if i[1] == self.password:
                self.enter_1.config(show='*')
            # ______________________________________________(вставить проверку админ не админ)
            self.enter_1.pack(side='left')
            i[1].set(i[2])
        self.btn_1 = tk.Button(self.label_frame_1, text='ВОЙТИ', font=font_size, command=self.autho)
        self.btn_1.pack(padx=3, pady=3)
        self.label_frame_1_2 = tk.LabelFrame(self.root)
        self.label_frame_1_2.pack(pady=10)
        self.frame_1_2 = tk.Frame(self.label_frame_1_2)
        self.frame_1_2.pack()
        self.btn_1_2 = tk.Button(self.frame_1_2, text='ЗАРЕГИСТРИРОВАТЬСЯ', font=font_size, command=self.registr)
        self.btn_1_2.pack(padx=3, pady=3)

    def autho(self):
        login = self.login.get()
        password = self.password.get()
        print(login, password)

    def registr(self):
        self.root.withdraw()
        mregistr = MagazineRegistr(500, 400)
        mregistr.mainloop()


class MagazineRegistr(tk.Tk):
    def __init__(self, height=500, width=400):
        super().__init__()
        self.root_2 = self
        self.root_2.title('Регистрация')
        self.root_2.geometry(f'{height}x{width}+700+200')
        self.label_frame_2 = tk.LabelFrame(self.root_2, text='Регистрация', font=font_size)
        self.label_frame_2.pack(padx=10, pady=10)
        self.firstname = tk.StringVar()
        self.name = tk.StringVar()
        self.lastname = tk.StringVar()
        self.login = tk.StringVar()
        self.password = tk.StringVar()
        self.regi = [
            ('Фамилия', self.firstname, ''),
            ('Имя', self.name, ''),
            ('Отчество', self.lastname, ''),
            ('Логин', self.login, ''),
            ('Пароль', self.password, '')
        ]
        self.labels = []
        self.enties = []
        for i in self.regi:
            self.frame_2 = tk.Frame(self.label_frame_2)
            self.frame_2.pack()
            label = tk.Label(self.frame_2, text=i[0], font=font_size)
            label.pack(side='left')
            entry = tk.Entry(self.frame_2, textvariable=i[1], font=font_size)
            if i[1] == self.password:
                entry.config(show='*')
            entry.pack(side='left')
            i[1].set(i[2])
            self.labels.append(label)
            self.enties.append(entry)
        self.btn_2 = tk.Button(self.label_frame_2, text='ЗАРЕГИСТРИРОВАТЬСЯ', font=font_size, command=self.registring)
        self.btn_2.pack(padx=3, pady=3)


    def registring(self):
        self.root_2.withdraw()
        mtelephone = MagazinTelephone()
        mtelephone.mainloop()
        
        
        pass
        # a=self.enties[0].get()
        # bd.registration(self.enties[0].get(),
        #                 self.enties[1].get(),
        #                 self.enties[2].get(),
        #                 self.enties[3].get(),
        #                 self.enties[4].get())

class MagazinTelephone:
    def __init__(self, title='Magazine') -> None:
        self.root_mag = tk.Tk()
        self.root_mag.title(title)

if __name__ == '__main__':
    mstart = MagazineStart(300, 500)
    mstart.mainloop()