'''
Docstring for LAB4.class1
Creating Your Own Class
Write a class with at least two instance attributes and a method 
that prints or returns information based on those attributes. 
Create at least two objects and demonstrate that they can have 
different values.
'''
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print("Employee name = ", self.name)
        print("Employee ID = ", self.id)

emp1 = Employee('John','130045')
emp2 = Employee('Emili','130123')
emp1.display()
emp2.display()