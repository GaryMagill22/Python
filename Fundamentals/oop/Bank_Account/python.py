class BankAccount:
    

    Account_Info = []
    def __init__(self, balance=0, int_rate=0.01):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.Account_Info.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    @classmethod
    def Get_Info(cls):
        for Info in cls.Account_Info:
            print(Info.balance)
        return cls

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= 5
            print('Insufficient funds: Charging a $5 fee.')
            return self
        self.balance -= amount
        return self
    
    def display_account_info(self):
        print('===========')
        print(f'Balance : {self.balance}')
        print(f'Interest Rate : {self.int_rate}')
        print(f'Account Type : {self.account_type}')
        print('===========')
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
    
    

Account1 = BankAccount(100).deposit(25).deposit(25).deposit(100).withdraw(150).yield_interest().display_account_info()
Account2 = BankAccount(50).deposit(50).deposit(50).withdraw(25).withdraw(25).withdraw(25).withdraw(25).yield_interest().display_account_info()


# Bonus - USE A CLASSMETHOD TO PRINT ALL INSTANCES OF A BANK ACCOUNTS INFO

Account1.Get_Info()

class User:

    def __init__(self, First_Name, Last_Name, Info) -> None:
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Account_type = {'Checking': BankAccount(), 'Savings': BankAccount()}
        self.Info = Info

User1 = User('Tiger', 'Woods' )
User1.Account_type['Savings']