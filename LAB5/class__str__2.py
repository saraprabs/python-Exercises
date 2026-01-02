'''
Docstring for LAB5.class__str__2
Create a class with a clean __str__ representation. Create a class with at least 
three attributes and implement __str__ to make printed objects readable and 
nicely formatted. 
'''
class Person:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __str__(self):
        return f"Person name {self.name} with age {self.age} has email id {self.email}"
    
    
P1 = Person(name='Ana', age = 35, email = 'ana327@gmail.com')
P2 = Person(name='Alex', age = 38, email = 'alex_dev@gmail.com')

print(P1)
print(P2)
