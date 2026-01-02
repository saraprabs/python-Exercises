'''
Docstring for LAB3.func_cond
Functions & Conditionals 
Create functions that: 
1. Return a greeting with a name 
2. Return a default greeting if no name is given 
3. Check if a number is even 
4. Add two numbers only if both are even, otherwise return 0
'''
def greet(name=''):
    return f"Hello {name}, Welcome" 
   
print(greet("Sara"))
print(greet())

def even_fn(n):
    return n%2 == 0

print(even_fn(3)) 
print(even_fn(6)) 

def sum_even(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return f"sum of even numbers {a} and {b} is {a+b}"
    else:
        return f"Not even {0}"

print(sum_even(3,4))
print(sum_even(6,4))