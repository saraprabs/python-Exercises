'''
Docstring for LAB5.strfromobjdictdata
 Build a formatted string using a comprehension. Generate a formatted string 
from object or dictionary data using comprehension and join().  
'''
class Employee:
    def __init__(self, data:dict):
        self.__dict__ = data

    def __str__(self):
        return ', '.join([f'{key} = {value}' for key,value in self.__dict__.items()])
  
emp1 = {
    'name' : 'Sara',
    'id' : 13256,
    'sal' : 25000
}
emp2 = {
    'name' : 'Aleesha',
    'id' : 55459,
    'sal' : 20000
}

e1 = Employee(emp1)
e2 = Employee(emp2)
print(e1)
print(e2)