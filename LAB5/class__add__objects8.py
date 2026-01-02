'''
Docstring for LAB5.class__add__objects
Implement __add__. Create a class where adding two objects with + produces a 
new combined object. 
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point X = {self.x} and Point Y = {self.y}"

    def __add__(self, other):
        ny_x = self.x + other.x
        ny_y = self.y + self.y
        return Point(ny_x, ny_y)
    
p1 = Point(10,20)
p2 = Point(20,30)
print("P1 ",p1)
print("P2 ",p2)
p3 = p1 + p2
print("P1 + P2= P3 ",p3)
