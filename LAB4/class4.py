'''
Docstring for LAB4.class4
Method for Updating an Attribute
Write a class where an attribute can be updated through a custom method. 
Demonstrate how the updated attribute changes the behavior 
of another method in the class
'''
class Employee:
    
    def __init__(self, name, salary, bonus=5000):
        self.name = name
        self.bonus = bonus
        self.salary = salary

    def total_sal(self):
        if (self.salary < 25000):
            self.bonus = self.bonus + 5000
    
    def display(self):
        print("Employee name",self.name)
        print("Employee salary",self.salary)
        print("Employee name",self.bonus)

emp1 = Employee('Alex',35000)
emp2 = Employee('Anna',20000)
emp1.total_sal()
emp1.display()
emp2.total_sal()
emp2.display()
