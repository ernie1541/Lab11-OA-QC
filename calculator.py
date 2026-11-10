import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

def mul(a, b):
    return a*b

def div(a, b):
    try:
        return b/a
    except ZeroDivisionError as e:
        raise ZeroDivisionError

def exp(a, b):
    return a**b

# First example
def square_root(a):
    if a< 0 :
        raise ValueError("the number input must be greater than zero")
    return a**0.5

def hypotenuse(a,b):
    return ((a**2)+(b**2))**0.5

def add(a, b): 
    return a+b
    pass

def subtract(a,b):
    return a-b

def logarithm(a,b):
    try:
        return math.log(b,a)
    except ValueError as V:
        return f"Error: {V}"