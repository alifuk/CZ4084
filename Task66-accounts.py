from abc import ABC, abstractmethod
class InsufficientFundsError(Exception):
    def __init__(self):
        super().__init__("InsufficientFundsError!!!")
    pass
class InvalidAmountError(Exception):
    pass

class Account(ABC):
    def __init__(self, account_number):
        self.balance = 0
        self.account_number = account_number

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, account_number, interest_rate):
        super().__init__(account_number)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount < 0:
            raise InvalidAmountError()
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise InvalidAmountError()
        if self.balance >= amount:
            self.balance -= amount
            print(f"Vybráno {amount}, zbývá {self.balance}")
        else:
            raise InsufficientFundsError()

    def apply_interest(self):
        self.balance *= (1 + self.interest_rate)

class CheckingAccount(Account):
    def __init__(self, account_number, overdraft_limit):
        self.overdraft_limit = overdraft_limit
        super().__init__(account_number)

    def deposit(self, amount):
        if amount < 0:
            raise InvalidAmountError()
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise InvalidAmountError()
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print(f"Vybráno {amount}, zbývá {self.balance}")
        else:
            raise InsufficientFundsError()

#Vytvoření účtů
savings = SavingsAccount("123456", interest_rate=0.03)
checking = CheckingAccount("654321", overdraft_limit=500)

#Práce s účty
savings.deposit(1000)
savings.apply_interest()

checking.deposit(500)
try:
    checking.withdraw(1200)  # Toto vyvolá výjimku
except InsufficientFundsError as e:
    print(e)

print(savings.get_balance())
print(checking.get_balance())


