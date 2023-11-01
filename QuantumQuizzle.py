#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk

def addition():
    result_label.config(text="Addition button pressed")
    
def subtraction():
    result_label.config(text="Subtraction button pressed")

def multiplication():
    result_label.config(text="Multiplication button pressed")

def division():
    result_label.config(text="Division button pressed")

window = Tk()
window.geometry("800x500")

ProgName = Label(window, font=('Times new roman', 20, 'bold'), text="QuantumQuizzle (^_^)", fg="Purple")
ProgName.place(relx=.4, rely=.01)

chooseType = Label(window, font=('Times new roman', 20, 'bold'), text="Choose between Addition, Subtraction, Multiplication, and Division", fg="Green")
chooseType.place(relx=.02, rely=.2)

optionAdd = ttk.Button(window, text="Addition", command=addition)
optionAdd.place(relx=.01, rely=.4)
optionSub = ttk.Button(window, text="Subtraction", command=subtraction)
optionSub.place(relx=.01, rely=.5)
optionMult = ttk.Button(window, text="Multiplication", command=multiplication)
optionMult.place(relx=.01, rely=.6)
optionDiv = ttk.Button(window, text="Division", command=division)
optionDiv.place(relx=.01, rely=.7)

result_label = Label(window, font=('Times new roman', 15, 'bold'), text="")
result_label.place(relx=.2, rely=.8)

enter = Entry(window)
enter.place(relx=.3, rely=.5)
window.mainloop()
