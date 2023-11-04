#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk

def solve_equation():
    equation = equation_entry.get()
    try:
        left, right = equation.split('=')
        left = left.strip()
        right = right.strip()
        if '+' in left:
            progress.config(text="+ is being detected ^o^")
            x_coefficient, constant = left.split('x')
            x_coefficient = float(x_coefficient.strip())
            befoCon = float(constant.strip('+'))
            constant = float(right) - float(constant.strip())

            # Check for division by zero
            if x_coefficient == 0:
                result_text.set("Error: Division by zero")
                steps_text.delete(1.0, END)
            else:
            # Calculate and display the result
                result = constant / x_coefficient

                steps = []
                steps.append(f"Solving equation: {equation}")
                steps.append(f"Step 1: Rearrange the equation")
                steps.append(f"{x_coefficient}x = {right} - {befoCon}")
                steps.append(f"Step 2: Divide both sides by {x_coefficient}")
                steps.append(f"x = {constant} / {x_coefficient}")
                steps.append(f"x = {constant/x_coefficient}")

                result_text.set(f"Result: x = {result}")
                steps_text.delete(1.0, END)
                for step in steps:
                    steps_text.insert(END, step + "\n")

        elif '-' in left:
            progress.config(text="- is being detected ^o^")
            x_coefficient, constant = left.split('x')
            x_coefficient = float(x_coefficient.strip())
            befoCon = float(constant.strip('-'))
            constant = float(right) + float(constant.strip('-'))

            # Check for division by zero
            if x_coefficient == 0:
                result_text.set("Error: Division by zero")
                steps_text.delete(1.0, END)
            else:
            # Calculate and display the result
                result = constant / x_coefficient

                steps = []
                steps.append(f"Solving equation: {equation}")
                steps.append(f"Step 1: Rearrange the equation")
                steps.append(f"{x_coefficient}x = {right} + {befoCon}")
                steps.append(f"Step 2: Divide both sides by {x_coefficient}")
                steps.append(f"x = {constant} / {x_coefficient}")
                steps.append(f"x = {constant/x_coefficient}")

                result_text.set(f"Result: x = {result}")
                steps_text.delete(1.0, END)
                for step in steps:
                    steps_text.insert(END, step + "\n")

        elif '*' in left:
            progress.config(text="* is being detected ^o^")
            x_coefficient, constant = left.split('x')
            x_coefficient = float(x_coefficient.strip())
            befoCon = float(constant.strip('*'))
            constant = float(right) / float(constant.strip('*'))

            # Check for division by zero
            if x_coefficient == 0:
                result_text.set("Error: Division by zero")
                steps_text.delete(1.0, END)
            else:
            # Calculate and display the result
                result = constant / x_coefficient

                steps = []
                steps.append(f"Solving equation: {equation}")
                steps.append(f"Step 1: Rearrange the equation")
                steps.append(f"{x_coefficient}x = {right} / {befoCon}")
                steps.append(f"Step 2: Divide both sides by {x_coefficient}")
                steps.append(f"x = {constant} / {x_coefficient}")
                steps.append(f"x = {constant/x_coefficient}")

                result_text.set(f"Result: x = {result}")
                steps_text.delete(1.0, END)
                for step in steps:
                    steps_text.insert(END, step + "\n")

        elif '/' in left:
            progress.config(text="/ is being detected ^o^")
            x_coefficient, constant = left.split('x')
            x_coefficient = float(x_coefficient.strip())
            befoCon = float(constant.strip('/'))
            constant = float(right) * float(constant.strip('/'))

            # Check for division by zero
            if x_coefficient == 0:
                result_text.set("Error: Division by zero")
                steps_text.delete(1.0, END)
            else:
            # Calculate and display the result
                result = constant / x_coefficient

                steps = []
                steps.append(f"Solving equation: {equation}")
                steps.append(f"Step 1: Rearrange the equation")
                steps.append(f"{x_coefficient}x = {right} * {befoCon}")
                steps.append(f"Step 2: Divide both sides by {x_coefficient}")
                steps.append(f"x = {constant} / {x_coefficient}")
                steps.append(f"x = {constant/x_coefficient}")

                result_text.set(f"Result: x = {result}")
                steps_text.delete(1.0, END)
                for step in steps:
                    steps_text.insert(END, step + "\n")


    except Exception as e:
        result_text.set(f"Error: {e}")
        steps_text.delete(1.0, END)
            
    #     x_coefficient, constant = left.split('x')
    #     x_coefficient = float(x_coefficient.strip())
    #     befoCon = float(constant.strip())
    #     constant = float(right) - float(constant.strip())

    #     # Check for division by zero
    #     if x_coefficient == 0:
    #         result_text.set("Error: Division by zero")
    #         steps_text.delete(1.0, END)
    #     else:
    #         # Calculate and display the result
    #         result = constant / x_coefficient

    #         steps = []
    #         steps.append(f"Solving equation: {equation}")
    #         steps.append(f"Step 1: Rearrange the equation")
    #         steps.append(f"{x_coefficient}x = {right} - {befoCon}")
    #         steps.append(f"Step 2: Divide both sides by {x_coefficient}")
    #         steps.append(f"x = {constant} / {x_coefficient}")
    #         steps.append(f"x = {constant/x_coefficient}")

    #         result_text.set(f"Result: x = {result}")
    #         steps_text.delete(1.0, END)
    #         for step in steps:
    #             steps_text.insert(END, step + "\n")
    # except Exception as e:
    #     result_text.set(f"Error: {e}")
    #     steps_text.delete(1.0, END)

window = Tk()
window.geometry("800x500")
window.title("Linear Equation Solver")

ProgName = Label(window, font=('Times new roman', 50, 'bold'), text="QuantumQuizzle (^_^)", fg="Purple")
ProgName.place(relx=.1, rely=.01)

equation_label = ttk.Label(window, text="Enter an equation (e.g., 2x+5=10): ")
equation_label.place(relx=.1, rely=.2)
equation_entry = Entry(window)
equation_entry.place(relx=.3, rely=.2)

solve_button = ttk.Button(window, text="Solve", command=solve_equation)
solve_button.place(relx=.6, rely=.2)

result_text = StringVar()
result_label = ttk.Label(window, textvariable=result_text)
result_label.place(relx=.1, rely=.3)

steps_label = Label(window, font=('Times new roman', 15, 'bold'), text="Solution Steps:")
steps_label.place(relx=.1, rely=.35)

steps_text = Text(window, height=10, width=60)
steps_text.place(relx=.1, rely=.4)

progress = Label(window, font=('Times new roman', 20, 'bold'), text="I have change", fg="Purple")
progress.place(relx= .5,rely=.5)

window.mainloop()
