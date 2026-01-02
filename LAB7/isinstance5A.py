'''
Write a function that: accepts an object, behaves differently depending on the object’s type,  uses isinstance 
2. Add a new class that should be supported. 
3. Identify all places that must be modified. 
4. Redesign the solution using polymorphism so: 
new classes require no changes to existing functions
'''
class Square:
    def __init__(self, side):
        self.side = side
class Circle:
    def __init__(self, radius):
        self.radius = radius
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
def calc_area(shape):               #Isinstance problem, if we want to add another shape,
    if isinstance(shape, Circle):   #we neeed to add a new elif block and new class
        return f"Area of circle = {3.14 * shape.radius **2:.2f}"# if there is 4 functions using the
    elif isinstance(shape, Square):  #shapes, then we need to modify all of them
        return f"Area of Square = {shape.side **2:.2f} "
    elif isinstance(shape, Triangle):
        return f"Area of Triangle = {0.5 *shape.base * shape.height:.2f}"
    else:
        raise ValueError("Unknown shape type")
print(calc_area(Circle(5))) 
print(calc_area(Square(5)))
print(calc_area(Triangle(5, 8)))
    