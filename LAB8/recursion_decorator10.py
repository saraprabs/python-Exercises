'''
Docstring for LAB8.recursion_decorator10
 Decorators + recursion interaction 
Create a recursive function that performs a calculation. 
Apply a decorator that logs information about each function call. 
Observe how the decorator behaves during recursive execution and explain the result.
'''
import functools 
def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__}({args[0]})")
        result = func(*args, **kwargs)
        print(f"{func.__name__}({args[0]} returned value {result})")
        return result
    return wrapper

@trace
def factorial(n):
    if n<= 1:
        return 1
    return n * factorial(n-1)

print("Factorials: ", factorial(4))