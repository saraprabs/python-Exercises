'''
Docstring for LAB8.decorator7
 Preserving function metadata 
Create a decorator that wraps a function. 
Ensure that the wrapped function retains its original metadata. 
Verify this by inspecting the function’s name and documentation before and after 
decoration.
'''
import functools
import math
def my_decorator(func):

    @functools.wraps(func)# this line copies meta data from func to wrapper
    
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def calc_area(radius):
    return math.pi * (radius ** 2)

print(f"Function Name: {calc_area.__name__}")
print(f"Docstring:     {calc_area.__doc__}")

result = calc_area(5)
print(f"Result: {result:.2f}")



