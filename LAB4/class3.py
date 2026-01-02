'''
Docstring for LAB4.class3
Class With a Calculation Method
Write a class with one attribute and a method that calculates something 
based on that attribute (for example area, price, or length). 
Show how changing the attribute affects the calculation.
'''
class Area:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        r = self.radius
        return Area.pi * r * r
    
a = Area(4)
a.calc_area()
print("Area of circle a object", a.calc_area())
b = Area(7)
print("Area of circle b object", b.calc_area())

