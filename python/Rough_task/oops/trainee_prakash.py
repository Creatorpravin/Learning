class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
      
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.balance += amount
        
        

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        
        

class SavingAccount(BankAccount):
    def __init__(self, name, balance=0, interest_rate=0.01):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        return interest
        
my_account_details = BankAccount('Prakash',1000)
print(my_account_details.balance)
my_account_details.deposit(500)
print(my_account_details.balance)
my_account_details.withdraw(1000)
print(my_account_details.balance)

interest_details = SavingAccount(name="prakash",balance=0)
print(interest_details.add_interest())
