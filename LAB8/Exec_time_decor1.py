'''
Task 1: Execution-time decorator 
Create a decorator that measures how long a function takes to execute. 
The decorator should print the execution time after the function has finished. 
Apply the decorator to a function that processes a list of numbers. 
'''
import time
from functools import wraps

def execution_timer(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"Function '{func.__name__}' executed in {duration:.6f} seconds")
        return result
    return wrapper

@execution_timer
def process_numbers(numbers):
    return [n**2 for n in numbers]

my_list = list(range(100000))
processed = process_numbers(my_list)