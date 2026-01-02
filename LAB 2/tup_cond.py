'''
Docstring for LAB 2.tup_cond
Tuple with Condition
Create a new tuple that contains only the even numbers
from a given tuple of integers
'''
tup_1 = (1,3,5,7,8,9,10,12,13,15,44,77,88)

even_tup = tuple(i for i in tup_1 if i%2 == 0)

print(even_tup)