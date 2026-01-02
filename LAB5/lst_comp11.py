'''
Docstring for LAB5.lst_comp11
Rewrite a loop using a list comprehension. Convert any loop-based list 
transformation into a single list comprehension. 
'''
num_lst = [1,2,3,4,5,6,6,7,8,9,11]

sq_lst=[]
for m in num_lst:
    sq_lst.append( m * m)

print("Square list: ",sq_lst)

sq_lst2 = [x*x for x in num_lst]
print("using list comprehension: ", sq_lst2)