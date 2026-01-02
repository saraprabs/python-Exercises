'''
Docstring for LAB6.class6
Class Variables Across Inheritance  
Create a base class with a class variable.  
Create two subclasses.  
Override the class variable in one subclass but not the other.  
Create objects from all classes and show how the value differs depending on which 
class is used. 
'''
class A:
    count =1

class B(A):
    count = 5

class C(A):
    pass

a = A()
b = B()
c = C()
print("From class A ",a.count)
print("From class B ",b.count)
print("From class C ", c.count)