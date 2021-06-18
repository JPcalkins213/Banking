class bankAccount:
    def __init__(self, name, int_rate, balance):
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(self.name, self.balance)
        return self
    def yield_interest(self):
        for x in range(0, 365, 1):
            if(x < 365):
                x+1
            elif(x == 365):
                self.balance = self.balance + (self.balance*self.int_rate) 
        return self


class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = bankAccount('First National Dojo Bank', int_rate = 0.02, balance = 0)
    def make_deposit(self,amount):
        self.account_balance.balance += amount
        return self
    def make_withdrawl(self, amount):
        self.account_balance.balance -= amount
        return self
    def display_user_balance(self):
        print(self.name) 
        print(self.account_balance.balance)
        return self
    def transfer_money(self, other_user, ammount):
        self.account_balance.balance -= ammount
        ammount += other_user
        other_user = self.account_balance.balance
        return self
    def example_method(self):
        #we can call the instances from the bankAccount method
        self.account_balance.deposit(100)
        #or access it sattributes
        print(self.account_balance.balance)

jessica = bankAccount('Jessica Prier Calkins', .5, 3000)
rebekah = bankAccount('Rebekah Anne Bowers', 0.9, 6000)
guido = User('Guido van Rossum', 'guido@python.com')
monty = User('Monty Python', 'monty@python.com')

jessica.deposit(300).deposit(200).withdraw(400).yield_interest()
jessica.display_account_info()
guido.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawl(25).display_user_balance()
