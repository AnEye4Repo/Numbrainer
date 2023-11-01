#!/usr/bin/env python3
from tkinter import *

def addition():
    try:
        x = int(enter.get())
        numAdd = []
        sum_val = 0
        for i in range(x):
            num = int(enter_numbers[i].get())
            numAdd.append(num)
            sum_val += num
        result_label.config(text=f"Sum: {sum_val}")
    except ValueError:
        result_label.config(text="Invalid input")

def create_number_input_widgets():
    num_inputs_text = enter.get()

    if num_inputs_text.strip() == "":
        result_label.config(text="Please enter the number of values.")
        return

    num_inputs = int(num_inputs_text)

    for widget in enter_numbers:
        widget.destroy()
    enter_numbers.clear()

    for i in range(num_inputs):
        label = Label(window, text=f"Number {i + 1}:")
        label.place(relx=0.2, rely=0.5 + i * 0.1)
        num_entry = Entry(window)
        num_entry.place(relx=0.4, rely=0.5 + i * 0.1)
        enter_numbers.append(num_entry)

    result_label.config(text="")  # Clear any previous error message

window = Tk()
window.geometry("800x500")

ProgName = Label(window, font=('Times new roman', 20, 'bold'), text="QuantumQuizzle (^_^)", fg="Purple")
ProgName.place(relx=0.4, rely=0.01)

chooseType = Label(window, font=('Times new roman', 20, 'bold'), text="Choose between Addition, Subtraction, Multiplication, and Division", fg="Green")
chooseType.place(relx=0.02, rely=0.2)

optionAdd = Button(window, font=('Times new roman', 15, 'italic'), text="Addition", command=addition)
optionAdd.place(relx=0.01, rely=0.4)

num_label = Label(window, text="How many numbers would you like to use:")
num_label.place(relx=0.2, rely=0.4)
enter = Entry(window)
enter.place(relx=0.4, rely=0.4)

enter_numbers = []
result_label = Label(window, text="", font=('Times new roman', 15, 'bold'))
result_label.place(relx=0.2, rely=0.7)

update_button = Button(window, text="Update Inputs", command=create_number_input_widgets)
update_button.place(relx=0.4, rely=0.7)

window.mainloop()
