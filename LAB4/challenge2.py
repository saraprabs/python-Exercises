'''
Docstring for LAB4.challenge2
Class With Both Class-Level and Instance-Level Behavior
Write a class that uses:- at least one class attribute- at least 
one instance attribute- at least one method that uses the class attribute- 
at least one method that uses only the instance attributes
Then add a way to change the class attribute and show how this 
affects all existing objects. Also show how changing an instance attribute 
affects only one object.
'''
class Car:
    year = 2025
    def __init__(self, model, engine, yom ):
        self.model = model
        self.yom = yom
        self.engine = engine

    def calc_warranty(self):
            if Car.year - self.yom >5:
                 print(self.model," Warranty expired")
            else:
                 print(self.model, " Warranty covered")
    
    def diplay(self):
         print("Displaying the car details : ")
         print("Model - ", self.model)
         print("Engine - ", self.engine)
         print("Manufacturing year",self.yom)
    
car1 = Car('Audi Q3', 'TFSI', 2023)
car2 = Car('Ford bronco', 'EcoBoost v6', 2018)
car1.diplay()
car2.diplay()
car1.calc_warranty()
car2.calc_warranty()
Car.year = 2024
print("After change of warranty year")
car1.calc_warranty()
car2.calc_warranty()