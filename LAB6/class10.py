'''
Docstring for LAB6.class10
. Design Task – Controlled Inheritance  
Design a small inheritance hierarchy that models a real-world concept.  
Requirements:  - Use inheritance and super() correctly  - Override at least one method  -
 Include at least one class variable  - Include either a protected or private attribute  - 
 Do not use polymorphism or duck typing  
Create objects and demonstrate that the inheritance structure works as intended.
'''
class Employee:
    Company_name = "LogiTech Ltd"
    def __init__(self, name, emp_id, sal):
        self.name = name
        self.emp_id = emp_id
        self.sal = sal
        self._is_active = True
    
    def get_details(self):
        status = "Active" if self._is_active else "Inactive"
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Salary: {self.sal}, Status: {status}"
    
class AccountManager(Employee):
    def __init__(self,  name, emp_id, sal):
        super().__init__( name, emp_id, sal)
        self.__bonus = 5000
    
    def get_details(self):
        emp_details = super().get_details()
        tot_sal = self.assign_bonus()
        return f"{emp_details} , Total salary: {tot_sal} Company: {self.Company_name}"
    
    def assign_bonus(self):
        if self._is_active:
            self.sal += self.__bonus
            return self.sal

mgr1 = AccountManager('Sara',150032, 35000)
print(mgr1.get_details())
mgr2 = AccountManager('Anitha',153320,30000)
print(mgr2.get_details())
