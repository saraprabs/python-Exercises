'''
Docstring for LAB6.class1
Constructor Execution Order  
Create a base class and two subclasses that form an inheritance chain.  
Each class must print a message from its constructor.  
Create an object of the most derived class and observe the order in which the 
constructors are executed.  
Use super() in all constructors. 
'''
class A:
    def __init__(self, value):
        print(f"Printing from Class A value= {value}")
        self.value = value
        

class B(A):
    def __init__(self, value):
        print(f"Printing from Class B value= {value}")
        super().__init__(value)
        

class C(B):
    def __init__(self, value):
        print(f"Printing from Class C value= {value}")
        super().__init__(value)
        

c = C(10)
print(c.value)
print(C.mro())