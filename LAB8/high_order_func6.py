'''
Higher-order function pipeline 
Create a function that takes another function as input. 
Chain multiple function calls together to process a value step by step. 
Use both named functions and lambda expressions in the pipeline.
'''
def high_func_pipeline(func, a, b):
    return func(a,b)

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

multiply_lambda = lambda x,y: x * y

multiple_funcs = [add, multiply_lambda, sub, mul]
for i in multiple_funcs:
    print(high_func_pipeline(i,8,7))
   




