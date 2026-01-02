'''
Doc List Builder 
Students must: 
1. Create a list with 5 mixed-type elements 
2. Use append() to add two new items 
3. Use pop() to remove an element 
4. Reverse the list 
5. Sort the list (if possible) 
6. Print the final result string for listbuilder
'''
lst_1 = ['H', 'Hello', 34.3234, 7, True ]

lst_1.append(3)
lst_1.append(False)
lst_1.pop(3)
lst_1.reverse()
try:
    lst_1.sort()
except TypeError:
    print("Can't sort a list with different datatypes")

print(lst_1)