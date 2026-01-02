'''
Docstring for LAB4.var_scope
Local vs Global Variable
Create a program that demonstrates the difference between 
a local variable and a global variable. The
program should clearly show both values
'''
a = 'apple'

def fruit(my_fruit):
    print("I'm Local fruit: ", my_fruit)

fruit("banana")

print("I'm global fruit: ", a)