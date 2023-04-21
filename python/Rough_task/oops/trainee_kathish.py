class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def list_transactions(self):
        print("Last 5 transactions:")
        for t in self.transactions[-5:]:
            print(f"{t[0]}: {t[1]}")


class CreditAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(('deposit', amount))


class DebitAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(('withdraw', amount))
        else:
            print("Insufficient balance")


credit = CreditAccount("1234", 1000)
debit = DebitAccount("5678", 200)

credit.deposit(600)
debit.withdraw(60)
credit.deposit(200)
credit.deposit(300)
credit.deposit(400)
debit.withdraw(20)
debit.withdraw(30)
debit.withdraw(10)
debit.withdraw(40)
debit.withdraw(70)
credit.deposit(800)
debit.withdraw(90)
credit.deposit(600)
credit.deposit(600)

credit.list_transactions()
debit.list_transactions()
