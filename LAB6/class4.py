'''
Docstring for LAB6.class4
Predict and Verify MRO  
Create a diamond-shaped inheritance structure with four classes.  
Before running the program, write down what you believe the MRO will be.  
Then print the actual MRO and compare it with your prediction. 
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

class C(A):
    def __init__(self, value):
        print(f"printing from class C: value = {value}")
        super().__init__(value)
        self.value *=2
     
class D(B,C):
    def __init__(self, value):
        print(f"Printing from Class D value= {value}")
        super().__init__(value)

d = D(10)
print(d.value)
print(D.mro())