#!/usr/bin/env python3
import spacy
from sympy import symbols, Eq, solve

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")
numX=0
numSym=0
num=0
numX=0
numSym=0
numright=0
newx=0
def custom_tokenizer(nlp):
    # Add custom rules to the default tokenizer
    infixes = ['\+', '\-', '\*', '/']
    infix_regex = spacy.util.compile_infix_regex(infixes)
    nlp.tokenizer.infix_finditer = infix_regex.finditer

# Add the custom tokenizer to spaCy pipeline
custom_tokenizer(nlp)

def process_input(user_input):
    # Split the input equation into left and right sides
    left_side, right_side = user_input.split('=')
    left_side = left_side.strip()
    right_side = right_side.strip()

    # Tokenize and parse the left side using spaCy
    left_doc = nlp(left_side)
    left_entities = [token.text for token in left_doc]

    # Tokenize and parse the right side using spaCy
    right_doc = nlp(right_side)
    right_entities = [token.text for token in right_doc]

    return left_entities, right_entities



# Take user input
user_equation = input("Enter an equation: ")
left_entities, right_entities = process_input(user_equation)
x = symbols('x')

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
print("Left Side Entities:", left_entities)
print("Right Side Entities:", right_entities)
