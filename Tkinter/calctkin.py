'''
    Программа написано основвываясь на курсе Создание GUI приложения Python tkinter.
    Создаем калькулятор на tkinter
    egoroff_channel
'''
import tkinter as tk


# Отображает цифры при нажатии кнопок
def add_digit(digit):
    value = calc.get() + str(digit)
    calc.delete(0, tk.END)
    calc.insert(0, value)


# Отображает нажатие кнопок с операциями и производит вычисления
def add_operation(operation):
    value = calc.get()
    # Проверяет наличие операции в строке если 2 подряд то заменяет первую на вторую
    if value[-1] in '+-*/':
        value = value[:-1]
    # Проверяет наличие операции в строке если есть то вычисляет
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)


# Производит вычисления с помощью ф-ии eval()
def calculate():
    value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, eval(value))


# Очищает экран
def clear_screen():
    calc.delete(0, tk.END)


# Возвращает отображение кнопок с цифрами в окне:
def digit_button(digit):
    return tk.Button(text=digit, bd=3, font=('', 13), command=lambda: add_digit(digit), bg='red')


# Возвращает отображение кнопок с операциями в окне:
def operation_button(operation):
    return tk.Button(text=operation, bd=3, font=('', 13), command=lambda: add_operation(operation), bg='blue',
                     fg='white')


# Возвращает отображение кнопку = в окне:
def calc_button(operation):
    return tk.Button(text=operation, bd=3, font=('', 13), command=lambda: calculate(), bg='blue',
                     fg='white')


# Возвращает отображение кнопу 'C' в окне:
def clear_button(operation):
    return tk.Button(text=operation, bd=3, font=('', 13), command=lambda: clear_screen(), bg='blue',
                     fg='white')


root = tk.Tk()

root.title('Калькулятор')
root.geometry('240x270+300+200')
root['bg'] = '#22ffee'

calc = tk.Entry(root, justify=tk.RIGHT, font=('', 15))
calc.grid(row=0, column=0, columnspan=4, sticky='we')

digit_button('1').grid(row=1, column='0', sticky='wens', padx=3, pady=3)
digit_button('2').grid(row=1, column='1', sticky='wens', padx=3, pady=3)
digit_button('3').grid(row=1, column='2', sticky='wens', padx=3, pady=3)
digit_button('4').grid(row=2, column='0', sticky='wens', padx=3, pady=3)
digit_button('5').grid(row=2, column='1', sticky='wens', padx=3, pady=3)
digit_button('6').grid(row=2, column='2', sticky='wens', padx=3, pady=3)
digit_button('7').grid(row=3, column='0', sticky='wens', padx=3, pady=3)
digit_button('8').grid(row=3, column='1', sticky='wens', padx=3, pady=3)
digit_button('9').grid(row=3, column='2', sticky='wens', padx=3, pady=3)
digit_button('0').grid(row=4, column='0', sticky='wens', padx=3, pady=3)

operation_button('+').grid(row=1, column='3', sticky='wens', padx=3, pady=3)
operation_button('-').grid(row=2, column='3', sticky='wens', padx=3, pady=3)
operation_button('/').grid(row=3, column='3', sticky='wens', padx=3, pady=3)
operation_button('*').grid(row=4, column='3', sticky='wens', padx=3, pady=3)

calc_button('=').grid(row=4, column='2', sticky='wens', padx=3, pady=3)

clear_button('C').grid(row=4, column='1', sticky='wens', padx=3, pady=3)

root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)
root.grid_columnconfigure(3, minsize=60)

root.grid_rowconfigure(1, minsize=60)
root.grid_rowconfigure(2, minsize=60)
root.grid_rowconfigure(3, minsize=60)
root.grid_rowconfigure(4, minsize=60)

calc.mainloop()
root.mainloop()
