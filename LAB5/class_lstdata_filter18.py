'''
Docstring for LAB5.class_lstdata_filter18
Create a class that processes input using a comprehension. Write a class that 
receives a list or dictionary and transforms or filters the data internally using a 
comprehension.
'''
class Squarelist:
    def __init__(self, lstdata):
        self.data = lstdata
        self.sqlst = []

    def gen_sq_lst(self):
        self.sqlst = [x*x for x in self.data]
        return self.sqlst
    
num_lst = [1, 2, 3, 4, 5, 6, 7]
sclass = Squarelist(num_lst)
print("Square list generated--", sclass.gen_sq_lst())