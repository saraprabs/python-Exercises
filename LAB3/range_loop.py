"""
Docstring for LAB3.range_loop
 Range & Loops (Numbers and Iteration) 
Create a program that: 
1. Prints all odd numbers from 1–20 
2. Calculates and prints the sum of numbers from 1–100 
3. Asks the user for a number and prints its multiplication table (1–10)
"""
print("Printing odd numbers from 1 to 20")
for i in range(1,21):
    if i%2 != 0:
        print(i, end=' ')

print("\nSum of numbers form 1 to 100")
sum = 0
for x in range(1,101):
    sum += x
print(sum)

num = int(input("Enter a number: "))
for a in range(1,11):
    print(f"{num} x {a} = {num*a}")