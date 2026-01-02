'''
To overcome the problem of isinstance we use polmorphism and abstract methods
'''
from abc import ABC, abstractmethod
class Shape(ABC):       #uses abstraction and polymorphism 
    @abstractmethod 
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius **2)
class Square(Shape) :
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side **2
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height * 0.5
def calc_area(shape:Shape):
    return shape.area() # doesn't care about circle or square,
#it checks its a shape and has .area method
shapes = [Circle(5), Square(6), Triangle(5,8)]
for s in shapes:
    print(f"Area: {calc_area(s)}")    

        