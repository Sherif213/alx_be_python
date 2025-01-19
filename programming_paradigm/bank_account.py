class BankAccount:
    account_balance = 0
    def __init__(self,balance):
        account_balance = balance
        
    def deposit(self,amount):
        if amount>0:
            self.account_balance += amount
    
    def withdraw(self,amount):
        if amount >= self.account_balance:
            self.account_balance -= amount
    
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")