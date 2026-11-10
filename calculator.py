import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    return a+b
    pass

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    try:
        return b/a
    except ZeroDivisionError as e:
        return f"ERROR: {e}"

def logarithm(a,b):
    try:
        return math.log(b,a)
    except ValueError as V:
        return f"Error: {V}"

def exponent(a,b):
    return a**b
