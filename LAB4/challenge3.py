'''
Docstring for LAB4.challenge3
 Object Interaction
Create two different classes where objects from one class interact with 
objects from the other. Demonstrate how these interactions work and 
how changing attributes in one object affects the result in
the other
'''
class BankAccount:
    def __init__(self, acc_num, init_deposit):
        self.acc_num = acc_num
        self.balance = init_deposit
        print(f"Account {self.acc_num} created with balance: ${self.balance}")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.balance
    
class TransactionManager:
    def process_deposit(self, account_obj, amount):
        if account_obj.deposit(amount):
            print("Deposit successful.")
            print(f"Account {account_obj.acc_num} credited, current balance: ${account_obj.get_balance():.2f}")
        else:
            print("Deposit failed. Invalid amount provided")

    def process_transfer(self, from_account, to_account, amount):
        if from_account.withdraw(amount):
            to_account.deposit(amount)
            print(f"Transaction successful amount ${amount} transferred {from_account.acc_num} to {to_account.acc_num}")
            print(f"Remaining balance in both-- ${from_account.get_balance()} and ${to_account.get_balance()}")
        else:
            print(f"Transactoin failed. Insufficient funds from {from_account.acc_num}")


sara_account = BankAccount('A12345', 500)
ana_account = BankAccount('B45464', 1000)
print("***Simple deposit***")
manager = TransactionManager()
manager.process_deposit(sara_account, 200)
print("\n***Account Transfer:***")
manager.process_transfer(sara_account, ana_account, amount=100)
print(f"Final balance Sara account ${sara_account.get_balance():.2f}")
print(f"Final balance Ana account ${ana_account.get_balance():.2f}")
