'''
Docstring for LAB5.class_getitem_11
 Implement __getitem__. Create a class that allows indexing with square brackets 
to access internal data. 
DUnder class method __getitem__. The __getitem__() method is used to
 access elements from the data list stored inside the object.used to retrieve items from 
 containers or objects that support indexing or key-based access.
 The __getitem__() method is used to access elements from the data list stored inside the object.
The method allows us to use the object like a normal list, and my_list[2] internally calls
 my_list.__getitem__(2) to return the value 3.
 def __getitem__(self, key):
'''
class List:
    def __init__(self, data):
        self.data = data
    
    def __getitem__(self, index):
        return self.data[index]
    
a = List([1, 2, 3, 4, 5, 6, 7])

print(a[2])
print(a[-2:])
print(a[:5])
print(a[::2])