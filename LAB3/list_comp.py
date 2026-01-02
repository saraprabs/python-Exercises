'''
Docstring for LAB3.list_comp
Lists & Comprehensions 
Create a program that: 
1. Takes a given list of numbers 
2. Generates and prints: 
o A list of squares using a loop 
o A list of squares using a list comprehension 
o A list of positive numbers using a comprehension 
'''
num_lst = [1,2,3,4,5,6,6,7,8,9,11]
num_lst2 = [-1,-3,-5,5,3,8,-9,-6,7,6]
sq_lst=[]
for m in num_lst:
    sq_lst.append( m * m)

print("Square list: ",sq_lst)

sq_lst2 = [x*x for x in num_lst]
print("using list comprehension: ", sq_lst2)

print("Original list: ", num_lst2)
plus_lst = [x for x in num_lst2 if x>0]
print("Positive list: ",plus_lst)