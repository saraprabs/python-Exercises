'''
Docstring for LAB4.LEGB
Inner Function and the LEGB Rule
Write a function that contains an inner function. 
Use print statements to show which version of a name
is being used (local, enclosing, or global)
'''

x = 5

def outer_fn():
    x = 10
    print("Outer function X= ", x)
    def inner_fn():
        x = 15
        print("Inner function X= ", x)
    inner_fn()
    
print("Global variable X= ", x)
outer_fn()
