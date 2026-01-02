'''
Docstring for LAB5.class_kwargs_prop_dund20
Combine kwargs, property, and a dunder method. Create a class that: - accepts 
all attributes via **kwargs - includes at least one property with getter and setter - 
implements one or more dunder methods - includes a method that performs a 
calculation using its data
'''
class Employee:
    def __init__(self, **kwargs):
        self._data_dict = kwargs
        for key, value in self._data_dict.items():
            setattr(self, key, value)
    @property
    def data_dict(self):
        return self._data_dict
    
    @data_dict.setter
    def data_dict(self, new_dict):
        self._data_dict = new_dict

    def __str__(self):
       return ', '.join(f'{key}={value}' for key, value in self._data_dict.items())
    
    def __eq__(self, other):
        return self.sal == other.sal
    
    def calc_tot_sal(self, bonus):
        return self.sal + bonus
    
e1 = Employee(name = 'Sara', id = 13256, sal = 25000)
e2 = Employee(name = 'Aleesha', id = 13251, sal = 25000)
print("Employee1 Class object data-- ",e1)
print("Employee2 Class object data-- ",e2)
print("Comparing salary of 2 employees is equal? ", e1 == e2)
print("Total salary of Employee 1= ", e1.calc_tot_sal(5000))
print("Total salary of Employee 1= ", e2.calc_tot_sal(10000))