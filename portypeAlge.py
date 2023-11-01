from tkinter import *

def perform_operation():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = operator_var.get()
        
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                result_label.config(text="Error: Division by zero")
                return
            result = num1 / num2
        else:
            result_label.config(text="Error: Invalid operator")
            return
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Error: Invalid input")

window = Tk()
window.geometry("400x200")
window.title("Basic Algebra Calculator")

frame = Frame(window)
frame.pack(pady=10)

label_num1 = Label(frame, text="Number 1:")
label_num1.grid(row=0, column=0)

entry_num1 = Entry(frame)
entry_num1.grid(row=0, column=1)

label_operator = Label(frame, text="Operator:")
label_operator.grid(row=1, column=0)

operator_var = StringVar()
operator_var.set("+")  # Default operator is addition

operators = ["+", "-", "*", "/"]
operator_menu = OptionMenu(frame, operator_var, *operators)
operator_menu.grid(row=1, column=1)

label_num2 = Label(frame, text="Number 2:")
label_num2.grid(row=2, column=0)

entry_num2 = Entry(frame)
entry_num2.grid(row=2, column=1)

calculate_button = Button(frame, text="Calculate", command=perform_operation)
calculate_button.grid(row=3, columnspan=2)

result_label = Label(frame, text="")
result_label.grid(row=4, columnspan=2)

window.mainloop()