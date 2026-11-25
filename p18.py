class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"{self.holder}'s balance is {self.balance}")

acc = BankAccount("Aarav", 1000)
acc.check_balance()
acc.deposit(500)
acc.withdraw(300)
acc.withdraw(5000)
acc.check_balance()
