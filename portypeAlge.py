#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk
import spacy
from sympy import symbols, Eq, solve


nlp = spacy.load("en_core_web_sm")

numX=0
numSym=0
num=0
numX=0
numSym=0
numright=0
newx=0
x = symbols('x')


def custom_tokenizer(nlp):
    # Add custom rules to the default tokenizer
    infixes = ['\+', '\-', '\*', '/']
    infix_regex = spacy.util.compile_infix_regex(infixes)
    nlp.tokenizer.infix_finditer = infix_regex.finditer

custom_tokenizer(nlp)


def solve_equation():
    equation = equation_entry.get()
    try:
        left, right = equation.split('=')
        left = left.strip()
        right = right.strip()

        left_side, right_side = equation.split('=')
        left_side = left_side.strip()
        right_side = right_side.strip()

        left_doc = nlp(left_side)
        left_entities = [token.text for token in left_doc]

        # Tokenize and parse the right side using spaCy
        right_doc = nlp(right_side)
        right_entities = [token.text for token in right_doc]

        print("Left Side Entities:", left_entities)
        print("Right Side Entities:", right_entities)



        for token in left_entities:
            if 'x' in token:
                numX = token
                newx = int(numX.split('x')[0])
            elif '+' in token or '-' in token or '*' in token or '/' in token:
                numSym = token
            else:
                num = token

        for token in right_entities:
            if 'x' in token:
                numX = token
                newx = int(numX.split('x')[0])
            else:
                numright = token


        if numSym == '+':
            print("+")
            equation = Eq(newx * x + int(num), int(numright))
        elif numSym == '-':
            print("-")
            equation = Eq(newx * x - int(num), int(numright))
        elif numSym == '*':
            print("*")
            equation = Eq(newx * x * int(num), int(numright))
        elif numSym == '/':
            print("/")
            equation = Eq(newx * x / int(num), int(numright))
        else:
            # Handle the case when numSym is not any of the recognized symbols
            print("Invalid operation")
            equation = None

        # Check if equation is created before attempting to solve
        if equation is not None:
            solution = solve(equation, x)[0].evalf()
            formatted_solution = str(solution).rstrip('0').rstrip('.')
            print(f"Decimal Solution: {formatted_solution}")
            result_text.set(f"Result: x = {formatted_solution}")

        print("Left Side Entities:", left_entities)
        print("Right Side Entities:", right_entities)

    except Exception as e:
        result_text.set(f"Error: {e}")
        steps_text.delete(1.0, END)




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
