'''
Docstring for LAB4.global_var3
 Local Variable Shadowing a Global Variable
Create an example where a global variable and a local variable 
have the same name. The program should demonstrate which value is 
used inside the function and which is used outside.
'''
x = 5

def num():
    x = 10
    lst = [x for _ in range(x)]
    print("Local x inside function num() = ", x)

print("Global X= ", x)
print("Call function num()")
num()
print("X after function call is the global x unchanged = ", x)
