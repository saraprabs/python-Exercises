'''
Docstring for LAB6.class9
 Overriding __str__ in a Subclass  
Create a base class with a meaningful __str__ method.  
Override __str__ in a subclass.  
Use super().__str__() inside the subclass and add subclass-specific information.  
Print objects of both classes to show the difference. 
'''
class Employee:
    def __init__(self, name, age, sal):
        self.name = name
        self.age =age
        self.sal = sal
    def __str__(self):
        return f"{self.name}, age {self.age} earns salary £{self.sal}"

class Developer(Employee):
    def __init__(self, name, age, sal):
        super().__init__(name, age, sal)
    
    def __str__(self):
        print(f"{self.name} is a Developer")
        return super().__str__()

emp1 = Employee('Alex', 45, 45000)
dev1 = Developer('Anna', 35, 25000)
print(emp1)
print(dev1)