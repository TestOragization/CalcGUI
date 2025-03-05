from tkinter import *
from Calc import Calculator

def on_button_click(char):
    if char == '=':
        expression = entry.get()
        result = calculator.calculate(expression)
        result_label.config(text=f"Результат: {result}")
        entry.delete(0, END)
    else:
        entry.insert(END, char)

def clear_entry():
    entry.delete(0, END)
    result_label.config(text="Результат:")

def show_history():
    history_text.delete(1.0, END)
    calculator.cursor.execute("SELECT Expression, Result, TimeOfAction FROM History")
    rows = calculator.cursor.fetchall()
    if rows:
        for row in rows:
            history_text.insert(END, f"{row.Expression} = {row.Result} at {row.TimeOfAction}\n")
    else:
        history_text.insert(END, "История пуста.")

def show_logs():
    logs_text.delete(1.0, END)
    calculator.cursor.execute("SELECT Action, Result FROM UserLogs")
    rows = calculator.cursor.fetchall()
    if rows:
        for row in rows:
            logs_text.insert(END, f"{row.Action} | {row.Result}\n")
    else:
        logs_text.insert(END, "Логи пусты.")

root = Tk()
root.title("Калькулятор (GUI)")
calculator = Calculator()

entry = Entry(root, width=40, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

result_label = Label(root, text="Результат: ", font=("Arial", 12))
result_label.grid(row=1, column=0, columnspan=4)

history_label = Label(root, text="История вычислений:", font=("Arial", 12))
history_label.grid(row=2, column=0, columnspan=4)

history_text = Text(root, height=5, width=50, font=("Arial", 10))
history_text.grid(row=3, column=0, columnspan=4, padx=10, pady=5)

logs_label = Label(root, text="Логи пользователя:", font=("Arial", 12))
logs_label.grid(row=4, column=0, columnspan=4)

logs_text = Text(root, height=5, width=50, font=("Arial", 10))
logs_text.grid(row=5, column=0, columnspan=4, padx=10, pady=5)

btn_history = Button(root, text='История', width=20, height=2, command=show_history)
btn_history.grid(row=6, column=0, columnspan=2)

btn_logs = Button(root, text='Логи', width=20, height=2, command=show_logs)
btn_logs.grid(row=6, column=2, columnspan=2)

btn_7 = Button(root, text='7', width=10, height=2, command=lambda: on_button_click('7'))
btn_7.grid(row=7, column=0)
btn_8 = Button(root, text='8', width=10, height=2, command=lambda: on_button_click('8'))
btn_8.grid(row=7, column=1)
btn_9 = Button(root, text='9', width=10, height=2, command=lambda: on_button_click('9'))
btn_9.grid(row=7, column=2)
btn_div = Button(root, text='/', width=10, height=2, command=lambda: on_button_click('/'))
btn_div.grid(row=7, column=3)

btn_4 = Button(root, text='4', width=10, height=2, command=lambda: on_button_click('4'))
btn_4.grid(row=8, column=0)
btn_5 = Button(root, text='5', width=10, height=2, command=lambda: on_button_click('5'))
btn_5.grid(row=8, column=1)
btn_6 = Button(root, text='6', width=10, height=2, command=lambda: on_button_click('6'))
btn_6.grid(row=8, column=2)
btn_mul = Button(root, text='*', width=10, height=2, command=lambda: on_button_click('*'))
btn_mul.grid(row=8, column=3)

btn_1 = Button(root, text='1', width=10, height=2, command=lambda: on_button_click('1'))
btn_1.grid(row=9, column=0)
btn_2 = Button(root, text='2', width=10, height=2, command=lambda: on_button_click('2'))
btn_2.grid(row=9, column=1)
btn_3 = Button(root, text='3', width=10, height=2, command=lambda: on_button_click('3'))
btn_3.grid(row=9, column=2)
btn_sub = Button(root, text='-', width=10, height=2, command=lambda: on_button_click('-'))
btn_sub.grid(row=9, column=3)

btn_0 = Button(root, text='0', width=10, height=2, command=lambda: on_button_click('0'))
btn_0.grid(row=10, column=0)
btn_dot = Button(root, text='.', width=10, height=2, command=lambda: on_button_click('.'))
btn_dot.grid(row=10, column=1)
btn_eq = Button(root, text='=', width=10, height=2, command=lambda: on_button_click('='))
btn_eq.grid(row=10, column=2)
btn_add = Button(root, text='+', width=10, height=2, command=lambda: on_button_click('+'))
btn_add.grid(row=10, column=3)

btn_clear = Button(root, text='C', width=10, height=2, command=clear_entry)
btn_clear.grid(row=11, column=0, columnspan=2)


root.mainloop()