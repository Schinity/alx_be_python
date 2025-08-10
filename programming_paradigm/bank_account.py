class BankAccount:
    def __init__(self, account_number, __balance=0):
        self.account_number = account_number
        self.__balance = __balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}."
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if self.__balance > 0 and amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount}."
        elif amount > self.__balance:
            return "Insufficient funds."
        else:
            return "Withdrawal amount must be positive."

    def display_balance(self):
        return f"Current balance: {self.__balance:.2f}"