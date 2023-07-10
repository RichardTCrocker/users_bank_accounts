class BankAccount:

    all_accounts = []
    def __init__(self, int_rate, balance = 0): 
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self)
        return
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    
    def yield_interest(self):
        yielded_amount = self.balance * self.int_rate
        self.balance = self.balance + yielded_amount
        return self
    

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(.02, 0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(f"{self.name}'s account has a balance of ${self.account.balance}")
        return self

account_123 = BankAccount(.01, 500)
account_456 = BankAccount(.25, 750)

account_123.deposit(100).deposit(150).deposit(250).withdraw(500)
account_456.deposit(50).deposit(700).withdraw(25).withdraw(25).withdraw(25).withdraw(25).yield_interest().display_account_info()


Spencer = User("Spencer", "spencer@gmail.com")
print("1")
Spencer.display_user_balance
print("2")
print(Spencer.name, Spencer.email, Spencer.account.balance)