class bankaccount:
    def __init__(self,accholder,balance=0):
        self.accholder=accholder
        self._balance=balance
    def deposit(self,amount):
        if amount>0:
            self._balance=self._balance+amount
            print(f"{amount} is deposited ,and my final balance is {self._balance} ")
        else:
            print("deposit amount is invalid")
    def check_balance(self):
        return self._balance
account=bankaccount("dhivya",20000)
print(account.accholder)
account.deposit(10000)
print(account.check_balance)
print(account._balance)
