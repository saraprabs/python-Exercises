'''
Docstring for LAB6.class7
Protected Attributes  
Create a base class that uses a protected attribute (single underscore).  
Access and modify this attribute from a subclass.  
Demonstrate that the attribute can be accessed, and explain why this is allowed but 
discouraged outside the class hierarchy. 
'''
class A:
    def __init__(self):
        self._internal_value = 10
        print(f"class A value = {self._internal_value}")

class B(A):
    def __init__(self):
        super().__init__()
        self._internal_value = 5
        print(f"value after changed in class B= {self._internal_value}")

b = B()
print(b._internal_value)
#Unlike double underscores (__attribute), which trigger name mangling to prevent accidental overrides,
#  the single underscore does nothing to the variable name in memory.
#Protected attributes often have specific logic governing them. 
# By modifying it directly from the outside, you might bypass safety checks.