class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 10000

    def get_balance(self):
        return self.balance

    def withdraw(self,amount):
        if amount<self.min_withdraw:
            return f'No Money for you. Minimum Withdrwa: {self.min_withdraw}.'
        elif amount>self.max_withdraw:
            return f'You crossed max limit: {self.max_withdraw}.'
        elif amount>self.balance:
            return f'You are fokir. No money for you.'
        else:
            self.balance -= amount
            return f'Here is your Money: {amount}.'

    def diposit(self,amount):
        self.balance += amount


my_bank = Bank(8000)

reply = my_bank.withdraw(2000)
my_bank.diposit(50000)
bal = my_bank.get_balance()
print(bal)