# Robust Arithmetic Calculator
# A modularized command-line calculator designed for input safety and error handling.

# Inputs: Two numeric operands and an arithmetic operation choice (+, -, *, /).

# Logic:

# Modular design using dedicated functions for each operation.

# Exception handling:

# ValueError: Raised when non-numeric input is provided.

# ZeroDivisionError: Raised when attempting division by zero.

# Outputs: The result of the calculation or descriptive error messages upon invalid input.

def calculation(n1, n2, op):
    try:
        if op == '+':
            print(f'The result is {n1 + n2}')
        elif op == '-':
            print(f'The result is {n1 - n2}')
        elif op == '*':
            print(f'The result is {n1 * n2}')
        elif op == '/':
            print(f'The result is {n1 / n2}')
        else:
            print('Please select a valid operator')
    except ZeroDivisionError:
        print('Division by zero is not allowed. Please change your parameters.')

try:
    first_number = float(input('Type first number: '))
    operator = input('Type operator (+, -, *, /): ')
    second_number = float(input('Type second number: '))

    calculation(first_number, second_number, operator)

except ValueError:
    print('Please type a valid numeric value.')

# Optimized IA code:

# # Robust Arithmetic Calculator

# def add(n1, n2):
#     return n1 + n2

# def subtract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     if n2 == 0:
#         raise ZeroDivisionError
#     return n1 / n2

# OPERATIONS = {
#     '+': add,
#     '-': subtract,
#     '*': multiply,
#     '/': divide,
# }

# def calculate(n1, n2, op):
#     if op not in OPERATIONS:
#         print('Invalid operator. Please use +, -, * or /.')
#         return

#     try:
#         result = OPERATIONS[op](n1, n2)
#         print(f'The result is {result}')
#     except ZeroDivisionError:
#         print('Division by zero is not allowed.')

# try:
#     n1 = float(input('Type first number: '))
#     op = input('Type operator (+, -, *, /): ')
#     n2 = float(input('Type second number: '))
#     calculate(n1, n2, op)
# except ValueError:
#     print('Invalid input. Please enter numeric values.')