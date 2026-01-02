'''
Docstring for LAB 2.dict_merge
 Dictionaries – Merge
Write a program that merges two dictionaries into one.
If a key exists in both, the value from
the second dictionary should be used
'''
dict_1 = {1:'integer', 2: 'float', 3: 'bool'}
dict_2 = {'a': 'apple', 2 : 'banana', 'c': 'carrot'}

merge_dict = dict_1 | dict_2

print(merge_dict)