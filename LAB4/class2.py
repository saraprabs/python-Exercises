'''
Docstring for LAB4.class2
Class Attribute vs Instance Attribute
Create a program demonstrating a class attribute shared 
across multiple objects. Then change the attribute for only 
one object and show that the other objects still use the original 
class attribute.
'''
class Alpha:
     counter = 5
     
a = Alpha()
b = Alpha()
c = Alpha()
print(a.counter)
print(b.counter)
c.counter = 10
print(c.counter)