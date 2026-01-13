class BankAccount:
    def __init__(self, owner):
        self.__owner = owner
        self.__balance = 0

    def deposit(self, x):
        if x > 0:
            self.__balance += x

    def withdraw(self, x):
        if x <= self.__balance:
            self.__balance -= x

    def get_balance(self):
        return self.__balance

acc = BankAccount("Aset")
acc.deposit(7777777)
acc.withdraw(777777)
print(acc.get_balance())
