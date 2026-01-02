'''
Docstring for LAB5.class18
 Create a class that processes input using a comprehension. Write a class that 
receives a list or dictionary and transforms or filters the data internally using a 
comprehension.
'''
class Person:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __str__(self):
        return f"Person name {self.name} with age {self.age} has email id {self.email}"
    
    def __repr__(self):
        return f"Person name {self.name} with age {self.age} has email id {self.email}"

P1 = Person(name='Ana', age = 35, email = 'ana327@gmail.com')
P2 = Person(name='Alex', age = 38, email = 'alex_dev@gmail.com')

print(P1)
print(P2)
print(repr(P2))