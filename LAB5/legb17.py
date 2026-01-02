'''
Demonstrate LEGB with nested functions. Create a function that contains 
another function. Use variables with the same name at multiple levels and 
demonstrate which is used where. Modify the enclosing variable using nonlocal. 
'''


x = 5

def outer_fn():
    x = 10
    print("Outer function X= ", x)
    def inner_fn():
        nonlocal x
        print("Inner function nonlocal X= ", x)
    inner_fn()
    
print("Global variable X= ", x)
outer_fn()
