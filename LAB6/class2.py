'''
Docstring for LAB6.class2
Modifying State Through super()  
Create a base class that stores a numeric value.  
Create two subclasses that modify this value in diAerent ways inside their 
constructors.  
Use super() so that each class in the inheritance chain contributes to the final value.  
Print the final result. 
'''
class A:
    def __init__(self,value):
        print(f"Printing from class A: value= {value} ")
        self.value = value
        
    
class B(A):
    def __init__(self, value):
        print(f"printing from class B: value = {value}")
        super().__init__(value)
        self.value += 10
        

class C(B):
    def __init__(self, value):
        print(f"printing from class C: value = {value}")
        super().__init__(value)
        self.value *=2
     
c= C(10)
print(c.value)
print(C.mro())