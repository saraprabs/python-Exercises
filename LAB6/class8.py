'''
Docstring for LAB6.class8
Private Attributes and Name Mangling  
Create a base class with a private attribute using double underscores.  
Attempt to access the attribute directly and observe what happens.  
Then access it using name mangling and explain how Python handles private 
attributes internally. 
'''
class Myclass:
    def __init__(self):
        self.__private_value = 50

obj = Myclass()
#print(obj.__private_value) # gives an attribute error because
#To protect the variable from being accidentally overwritten or accessed by subclasses/external code, the interpreter internally changes the name. 
# It transforms __private_value into: _Myclass__private_value

print(obj._Myclass__private_value)