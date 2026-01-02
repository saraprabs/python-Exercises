'''
Docstring for LAB 2.list_comp
List Comprehension - Even Numbers
Write a program that takes a list of integers 
and uses list comprehension to create a new list
containing only the even numbers.
'''
int_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 33, 44, 34, 56, 69, 92, 99]

print(int_lst)

even_lst = [i for i in int_lst if i % 2 == 0]

print(even_lst)