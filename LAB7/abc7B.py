'''
Implementing 7 A with abstract class
'''
from numbers import Number

def divide(a, b):
    if not(isinstance(a, Number) and isinstance(b, Number)):
        return "Error: Both inputs must be numbers"
    
    try:
        return a/b
    except ZeroDivisionError:
        return "Error: cannot divide by zero"
    
print(f"Integer division: {divide(455,25)}")
print(f"Float division: {divide(455.25,25.5):.2f}")
print(f"Complex number division: {divide(complex(4,2),2)}")
print(f"Invalid input: {divide(455,'25')}")