class BankAccount:
    def __init__(self, balance=0):
        if isinstance(balance, int): self.__balance = balance
        else: return NotImplemented

    def get_balance(self):
        return self.__balance

    def deposit(self, amount=0):
        if isinstance(amount, int): self.__balance += amount
        else: return NotImplemented

    def withdraw(self, amount=0):
        if isinstance(amount, int):
            if self.__balance - amount >= 0:
                self.__balance -= amount
            else: raise ValueError("На счете недостаточно средств")
        else: return NotImplemented

    def transfer(self, account, amount=0):
        if isinstance(account, BankAccount):
            self.withdraw(amount)
            account.deposit(amount)
        else: return NotImplemented
