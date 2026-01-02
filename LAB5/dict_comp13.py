'''
Docstring for LAB5.dict_comp13
Create a dictionary using a dict comprehension. Use two lists and combine them 
into a dictionary via comprehension. 
'''
lst1 = [1,2,3,4,5]
lst2 = ['one','two','three','four','five']

dict1 = {x : y for x, y in zip(lst1, lst2)}
print(dict1)