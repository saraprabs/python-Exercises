'''
Design a base class representing a general concept. 
2. The base class must define a method but not implement it. 
3. Create at least three subclasses that: 
o inherit from the base class 
o override the method with different behavior 
4. Write a function that: 
o accepts the base class 
o calls the method 
o does NOT use conditionals 
5. Call the function with each subclass.
'''
from abc import ABC, abstractmethod
class Payment(ABC):
    #base class for different payment methods
    @abstractmethod
    def process_payment(self, amount):
        pass
class Creditcard(Payment):
    def process_payment(self, amount):
        return f"Processing {amount} via credit card."
class Klarna(Payment):
    def process_payment(self, amount):
        return f"Processing {amount} via Klarna."
class Swish(Payment):
    def process_payment(self, amount):
        return f"Processing {amount} via Swish."
    
def execute_transaction(payment_method, amount):
    print(payment_method.process_payment(amount))
cc = Creditcard()
kl = Klarna()
sw = Swish()
execute_transaction(cc, 150)
execute_transaction(kl, 200)
execute_transaction(sw, 60)