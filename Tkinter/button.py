import tkinter as tk

root = tk.Tk()

root.title('Текст')
root.geometry('500x400+1000+200')

count_click = 0

lbl = tk.Label(text='Количество нажатий: {}'.format(count_click))

def click_button():
    # print('Кнопка была нажата')
    global count_click
    count_click += 1
    lbl.config(text='Количество нажатий: {}'.format(count_click))
    root.title('Количество нажатий: {}'.format(count_click))


btn = tk.Button(text='Нажми меня',
                bg='#0F489A',
                fg='#F8BFE1',
                activebackground='#000000',
                activeforeground='#FFFFFF',
                state='normal',   # active - нажатое состояние,
                                    # normal - обычная кнопка,
                                    # disabled - заблокированная кнопка
                font='24',
                command=click_button)

btn.pack()

lbl.pack()

root.mainloop()
