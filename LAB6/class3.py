'''
Docstring for LAB6.class3
Multiple Inheritance and MRO  
Create two parent classes that both modify the same attribute in their constructors.  
Create a child class that inherits from both parents.  
Use super() in all constructors.  
Print the final value and print the MRO of the child class.  
Explain why the final value is produced. 
'''
class A:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.value = 10
#if we use value argument we TypeError: object.__init__() takes no parameters, passing a value argument to 
# super().__init__(value),but the final class in the chain—the built-in object class—does not accept any arguments in its __init__ method.    
class B:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.value = 20
#To make multiple inheritance work smoothly with arguments, it is a best practice to use **kwargs. This allows each class 
# to take what it needs and pass the rest up the chain until an empty dictionary is passed to object.
class C(A, B):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

c = C()
print(c.value) #Because ParentA is the first parent listed in the inheritance tuple, its __init__ code 
#(after the super() call) executes after ParentB. Therefore, ParentA overwrites whatever ParentB did.
print(C.mro())
