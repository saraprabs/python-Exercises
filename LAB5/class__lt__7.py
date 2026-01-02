'''
Docstring for LAB5.class__it__7
Implement __lt__. Create a class where objects can be compared using < based 
on one chosen attribute. 
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y
    
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
    
p1 = Point(10,20)
p2 = Point(20,30)
p3 = Point(50,60)
p4 = Point(30,40)
print(p1 < p2)
print(p3 > p4)