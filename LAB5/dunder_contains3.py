'''
People class stores its data as a tuple containing a single element: the entire people_list.
The containment check will look for the Person("John", 25) object inside the tuple (people_list,).
 Since the only element in that tuple is the list itself, the check fails.
The check Person("John", 25) in p would still fail
The Person("John", 25) on the left side of the in operator is a brand new object in memory.
The Person("John", 25) inside the people_list is a different object in memory.
Since the Person class does not define an __eq__ method (which handles the == operator), Python defaults to 
comparing object identity (where the object is in memory), not object value (what its attributes are).
To make the comparison work based on the attributes (name and age), you would need to define the __eq__ method 
in your Person class:
'''
class Person:
    def __init__(self, name, age):
        self.data = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.data == other.data
        return "Not Implemented"
class People:
    def __init__(self, people_list):
        self.data = people_list

    def __contains__(self, item):
        return item in self.data

people_list = [Person("John", 25), Person("Jane", 30), Person("Bob", 35)]
p = People(people_list)

if Person("John", 25) in p:
    print("Yes, 'John' is present in the given list.")
else:
    print("No, 'John' is not present in the given list.")