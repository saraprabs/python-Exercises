'''
Docstring for LAB5.dunder_contains
__contains__ dunder method in python
Python’s built-in function `__contains__()` is a powerful tool that allows us to 
check if a specific value exists in a given sequence. This function can be used 
with several data types, including strings, lists, tuples, and sets. 
When we use the `__contains__()` function, Python checks whether the specified value 
is present in the sequence or not. If the value is present, the function returns True; 
otherwise, it returns False. 
'''
class Container:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return ', '.join(x for x in self.data)
    
    def __contains__(self, item):
        return item in self.data
    
c = Container(['apple','banana','strawberry','melon'])
print("Original list: ", c)
print("check if apple in list ",'apple' in c)
print("check if grape in list ",'grape' in c)

