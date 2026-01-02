'''
Docstring for LAB8.flexibledecor8
Flexible decorator with arguments 
Create a decorator that accepts its own arguments. 
The decorator should alter its behavior based on the provided arguments. 
Apply the decorator to multiple functions using different decorator arguments. 
'''
import functools

def dec_factory(bonus): #Decorator factory that takes an argument
    def my_decorator(func): #Actual decorator
        @functools.wraps(func)  # the functions meta data passed to the wrapper
        def wrapper(*args, **kwargs):   #the wrapper that modifies behaviour
            result = func(*args, **kwargs)
            return result + bonus   # perform action on result with decorator arguments
        return wrapper          
    return my_decorator

@dec_factory(bonus = 5000 ) # passing value to the decorator argument 
def add_emp_bonus(emp_sal):
    return emp_sal 

@dec_factory(bonus = 10000) # passing value to the decorator argument 
def add_mgr_bonus(mgr_sal):
    return mgr_sal

print(f"Employee total salary with bonus: {add_emp_bonus(15000)}") #bonus 5000 added by decorator arg bonus
print(f"Manager total salary with bonus: {add_mgr_bonus(30000)}") #bonus 10000 added by decorator arg bonus