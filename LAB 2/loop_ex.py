'''
Docstring for LAB 2.loop_ex
Loop - Power Calculation
Write a program that takes two integers as input (base and exponent)
and calculates the power using loops
'''
base = int(input("Base: "))
exp = int(input("Exponent: "))
result = base
if exp == 1:
    print(result)
elif exp > 1:
    for i in range(1, exp):
        result=result*base
    print(result)
else:
    print("Invalid input")
