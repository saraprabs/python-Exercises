'''
Docstring for LAB3.even_filter
Even Number Filter Tool (Mini Project) 
Create a program that: 
1. Accepts a line of numbers from the user 
2. Converts the input into a list of integers 
3. Uses filter() + lambda to keep only even numbers 
4. Prints: 
o The list of even numbers 
o The count of even numbers 
'''
lst1= []
lst1 = list(map(int,input().split()))
print(lst1)
even_lst = list(filter(lambda x: x%2 ==0, lst1))
print("Even list",even_lst)
print("Count of even numbers: ",len(even_lst))
