# Objective: Understand the fundamentals of OOP in Python by implementing a BankAccount class that encapsulates banking operations. 
# Use command line arguments to interact with instances of this class.

class BankAccount:
    def __init__(self, initial_balance = 0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False
        
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")