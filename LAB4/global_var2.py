'''
Docstring for LAB4.global_var
Function That Modifies a Global Variable
Write a program where a function changes the value of a global variable using the global keyword.
Display the value before and after the function call
'''
model='Volvo'
def car():
    global model
    model = 'Audi'

print("Global variable model before function call:-- ", model)
print("Call function\n","car()")
car()
print("After function call")
print("Change of global model value after functon call:--", model)


