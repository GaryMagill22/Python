

class BankAccount:
    

    Account_Info = []
    def __init__(self, balance=0, int_rate=0.01):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.Account_Info.append(self)
        

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
        print('===========')
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
    
    

Checking_Account = BankAccount(100).deposit(25).deposit(25).deposit(100).withdraw(150).yield_interest().display_account_info()
Savings_Account = BankAccount(50).deposit(50).deposit(50).withdraw(25).withdraw(25).withdraw(25).withdraw(25).yield_interest().display_account_info()


# Bonus - USE A CLASSMETHOD TO PRINT ALL INSTANCES OF A BANK ACCOUNTS INFO

# Account1.Get_Info()

class User:

    def __init__(self, First_Name, Last_Name, Email, Info,) -> None:
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Email = Email
        self.Info = Info
        self.Accounts= {'Checking_Account': BankAccount(), 'Savings_Account': BankAccount(int_rate=0.05)}
        # self.account = BankAccount(int_rate=0.02, balance=500)

    def make_deposit(self, type, amount,):
        self.Accounts[type].deposit(amount)
        print(f"Deposited ${amount} into my {type} and now have ${self.Accounts[type].balance}")
        return self
    
    def make_withdraw(self, type, amount):
        self.Accounts[type].withdraw(amount)
        print(f"Withdrew ${amount} from my {type} and now have ${self.Accounts[type].balance}")
        return self

    def display_user_balance(self, type):
        self.Accounts[type].display_account_info()



User1 = User('Tiger', 'Woods', 'Tigerwoods@pgaTour.com', 'Checking_Account').make_deposit('Checking_Account', 100).make_withdraw( 'Checking_Account', 25).display_user_balance("Checking_Account")

