'''
Docstring for LAB5.classproperty1
Create a class with a property and setter. Create a class with one attribute that 
can only be accessed and modified through a property and setter. Include a 
method that performs a calculation using the attribute.  
'''

class Area:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def set_radius(self):
        return self.radius

    @set_radius.setter
    def set_radius(self, value):
        self.radius = value
        print("setting the radius to value {self.radius}")

a = Area(3)
b = Area(4)
print(a.set_radius)
print(b.set_radius)

