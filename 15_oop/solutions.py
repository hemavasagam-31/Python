class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def show(self):
        print(f"Car: {self.brand}, Year: {self.year}")

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

acc = BankAccount("Ana", 1000)
acc.deposit(500)
acc.withdraw(300)
print("Balance:", acc.balance)
