'''
Docstring for LAB5.classkwarg4
Create a class that initializes from **kwargs. Write a class where attributes are 
automatically created from keyword arguments, even when different objects 
receive different arguments.  
'''
class Person:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __str__(self):
       return ', '.join(f'{key}={value}' for key,value in self.__dict__.items())
    
P1 = Person(name='Ana', age = 35, email = 'ana327@gmail.com')
P2 = Person(name='Alex', age = 38)

print(P1)
print(P2)
