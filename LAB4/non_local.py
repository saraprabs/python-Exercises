'''
Docstring for LAB4.non_local
 Using nonlocal
Create an example where an inner function modifies a variable in 
the enclosing function using the 
nonlocal keyword. Show the change before and after
'''

def outer_fn():
    flag = False
    def inner_fn():
        nonlocal flag
        print("Varible from enclosing function ",flag)
        flag = True
        print("Varible from enclosing function after change ",flag)
    inner_fn()

outer_fn()