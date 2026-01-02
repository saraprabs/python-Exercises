'''
Docstring for LAB4.global_var1
 Function Using a Global Variable
Write a function that reads the value of a global variable without 
changing it. Show in the output that the
global value remains the same after the function call.
'''
name = 'sara'

def display():
    global name
    label=name

print("Before functon call global variable:-- ", name)
print("call function\n","display()")
print("GLobal variable remains unchanged after function call:--", name)