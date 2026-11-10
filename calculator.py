import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    return b/a

def log(a, b):
    return math.log(b, a)

def exp(a, b):
    return a**b

# First example
def add(a, b): 
    return a+b
    pass

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def logarithm(a,b):
    try:
        return math.log(b,a)
    except ValueError as V:
        return f"Error: {V}"

def exponent(a,b):
    return a**b
