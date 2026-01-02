'''
Docstring for LAB5.class__len__obj9
Implement __len__. Create a class where len(object) returns a meaningful 
numeric value based on internal data. 
'''
class Point:
    def __init__(self, x, *args):
        self.x = x
        self.y = list(args)

    
    def __len__(self):
        return len(self.y)
    
p1 = Point(10,20,30,40,50,60,70,80,90)
p2 = Point(20,30,40,50,60,70)
print(len(p1))
print(len(p2))