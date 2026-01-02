'''
Docstring for LAB 2.nestedlst
 Nested List
Given the list l = [3, 7, [1, 4, 'hello']], change the value 'hello' to 'goodbye'
'''
lst_1 = [3, 7, [1, 4, 'hello']]
print(lst_1)

lst_1[2][2] = 'goodbye'
print(lst_1)