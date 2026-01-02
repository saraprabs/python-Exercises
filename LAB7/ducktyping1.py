'''
Discover Duck Typing
Understand that shared behavior, not shared type, enables polymorphism.
1. Write a function that: accepts a single argument, calls one method on that argument
2. Call the function with: a built-in type, a custom class you create yourself 
3. The function must work without modification for both. 
'''
def make_it_upper(s):
    return s.upper()

class Simple:
    def __init__(self, text):
        self.text = text
    
    def upper(self):
        return self.text.upper()

print(make_it_upper("Hello"))
print(make_it_upper(Simple("Welcome")))