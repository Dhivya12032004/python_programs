class BankAccount:
   
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder  # Public attribute
        self.__balance = balance  # Private attribute
    
    def get_balance(self):
        return self.__balance

    def _set_balance(self, amount):
        
        self.__balance = amount

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        raise NotImplementedError("Withdraw method must be implemented by subclasses.")

    def get_account_info(self):
        raise NotImplementedError("get_account_info method must be implemented by subclasses.")

    def __str__(self):
        return self.get_account_info()


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.03):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        current_balance = self.get_balance()
        if current_balance - amount >= 500:
            self._set_balance(current_balance - amount)
            print(f"{amount} withdrawn from Savings Account.")
        else:
            print("Insufficient balance! Minimum balance of ₹500 must be maintained.")

    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest of ₹{interest:.2f} added.")

    def get_account_info(self):
        return f"SavingsAccount: Holder: {self.account_holder}, Balance: ₹{self.get_balance():.2f}"


class CurrentAccount(BankAccount):
    
    def __init__(self, account_holder, balance=0, overdraft_limit=1000):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        current_balance = self.get_balance()
        if current_balance - amount >= -self.overdraft_limit:
            self._set_balance(current_balance - amount)
            print(f"{amount} withdrawn from Current Account.")
        else:
            print("Exceeded overdraft limit!")

    def get_account_info(self):
        return f"CurrentAccount: Holder: {self.account_holder}, Balance: ₹{self.get_balance():.2f}"


def main():
    # Create account objects
    savings = SavingsAccount("dhivya", balance=30000, interest_rate=0.05)
    current = CurrentAccount("Anna", balance=500, overdraft_limit=500)

    # Demonstrating polymorphism
    accounts = [savings, current]

    for account in accounts:
        print("\n" + str(account))
        account.deposit(1000)
        account.withdraw(500)

        if isinstance(account, SavingsAccount):
            account.calculate_interest()

    print("\nFinal Account Information:")
    for account in accounts:
        print(account)

if __name__ == "__main__":
    main()
