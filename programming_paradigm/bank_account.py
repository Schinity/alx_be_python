
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}."
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                return f"Withdrew {amount}."
            else:
                return "Insufficient funds."
        else:
            return "Withdrawal amount must be positive."

    def display_balance(self):
        return f"Current Balance: {self.__balance}"