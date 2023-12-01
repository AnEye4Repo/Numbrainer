#!/usr/bin/env python3
from sympy import symbols, Eq, solve

# Define symbolic variable
x = symbols('x')

# Define the linear equation
equation = Eq(2*x + 5, 10)

# Solve the equation and convert to decimal
solution = solve(equation, x)[0].evalf()

# Format the decimal solution to remove trailing zeros
formatted_solution = str(solution).rstrip('0').rstrip('.')

# Display the solution in decimal form without trailing zeros
print(f"Decimal Solution: {formatted_solution}")
