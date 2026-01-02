'''
 Break Duck Typing on Purpose- Understand the risk of duck typing.
 1. Take your function from Lab 1. 
2. Pass an object that does not implement the expected behavior. 
3. Observe the error. 
4. Explain: when the error occur
'''
def make_it_upper(s):
    return s.upper()        

class Simple:
    def __init__(self, text):
        self.text = text
    
    def upper(self):
        return self.text.upper() #Attribute error: type mismatch

print(make_it_upper("Hello"))
print(make_it_upper(Simple(1234))) 