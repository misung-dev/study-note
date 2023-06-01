class Account:
    def __init__(self, name, amount):
        self.owner = name
        self.balance = amount
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("잔액 부족")
    def print_balance(self):
        print("잔액:", self.balance)

acc1 = Account("Sarah", 50000)
acc2 = Account("John", 30000)
acc1.deposit(20000)
acc2.withdraw(150000)

print(acc1.owner, end=" - ")
acc1.print_balance()

print(acc2.owner, end=" - ")
acc2.print_balance()
