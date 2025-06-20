class BankAccount:
    def __init__(self, acc_holder, balance=0):
        self._acc_holder = acc_holder
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{amount} is deposited and my final balance is {self._balance}")
        else:
            print("Deposit amount is invalid")

    def check_balance(self):
        return self._balance


class SavingsAccount(BankAccount):
    def __init__(self, acc_holder, balance=0, interest_rate=0.05):
        super().__init__(acc_holder, balance)
        self._interest_rate = interest_rate

    def calculate_interest(self):
        interest = self._balance * self._interest_rate
        self._balance += interest
        print(f"Interest of {interest} is added and the new balance is {self._balance}")


# Creating an object of SavingsAccount
savings = SavingsAccount("Nevetha", balance=1000, interest_rate=0.04)
savings.deposit(2000)
savings.calculate_interest()

print("After savings the balance is:", savings.check_balance())
