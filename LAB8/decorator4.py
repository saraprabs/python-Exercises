'''
Decorator that modifies return values 
Create a decorator that intercepts the return value of a function. 
Modify the return value in some meaningful way before returning it. 
Apply the decorator to at least one function and demonstrate the effect. 
'''
def my_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'Function "{func.__name__}" with arguments {args} returned {result}')
        return result.upper()
    return wrapper

@my_decorator
def str_chk(text):
    if isinstance(text, str):
        return text.strip() 

print("After decoration of text : ",str_chk("Happy! Welocme"))
