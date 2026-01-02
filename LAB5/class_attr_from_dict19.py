'''
Docstring for LAB5.class_attr_from_dict19
Create a class that builds itself from a dictionary. Write a class that receives a 
dictionary and turns every key/value pair into attributes. Build __str__ using a comprehension.
data_dict.items(): 
Iterates over the key-value pairs of the input dictionary.
setattr(self, key, value): 
This built-in Python function is the core of the dynamic creation. 
It is functionally equivalent to writing self.key = value. By placing it inside the loop,
 it creates an attribute on the self object for every key in the dictionary.
'''
class Person:
    def __init__(self, data:dict):
        for key, value in data.items():
            setattr(self, key, value)    #buit-in function to create attributes for instance from dictionary
        
    def __str__(self):
        attributes = self.__dict__ #buit_in dict that holds all attributes of current instance
        attribute_strings =", ".join([f"{key} = '{value}'" for key, value in attributes.items()])
        return f"{self.__class__.__name__}({attribute_strings})" #buit_in variable to access current instance class name
    
person_data = {'name':'Anna', 'age': 36, 'mail':'ana@hotmail.com'}
person_obj = Person(person_data)
print(person_obj)