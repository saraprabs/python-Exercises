'''
Docstring for LAB6.class5
Overriding a Method and Calling the Parent  
Create a base class with a method that prints a message.  
Override this method in a subclass.  
Inside the overridden method, call the parent version using super() and then add 
additional behavior.  
Call the method and show both outputs. 
'''
class Animal:
    def make_sound(self):
        print("Aimals makes sound")

class Dog(Animal):
    def make_sound(self):
        super().make_sound()

mydog = Dog()
mydog.make_sound()