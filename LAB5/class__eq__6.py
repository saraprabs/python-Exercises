'''
Docstring for LAB5.class__eq__6
Implement __eq__. Create a class where two objects are equal if their attributes 
match. 
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
p1 = Point(10,20)
p2 = Point(10,20)
print(p1 == p2)