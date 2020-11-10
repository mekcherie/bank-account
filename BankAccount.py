
routing_number = 777444111
# Define a BankAccount class.
class BankAccount:
 
    def __init__(self, full_name, account_number, routing_number, balance=0):
        # intializing class
        self.full_name = full_name 
        self.balance= balance
        self.routing_number= routing_number
        self.account_number = account_number

   
    def deposit(self, amount):
        # taking the amount you put in the deposit 
        # make sure to add an amount to this increaing the value from 0
        self.balance = self.balance + amount 

    def withdraw(self, amount):
        if self.balance >=amount:
            # self.balance -= amount(same thing) bc it decreases by the amount you withdraw
            self.balance = self.balance - amount
        else:
            print("Insufficient funds")

    def print_balance(self):
        return "hello, {}. you have {}.".format(self.full_name, self.balance)

    def add_interest(self):
        interest = self.balance *  0.00083 
        return "hello, {}. your annual interest is {}.".format(self.full_name,interest)


account = BankAccount("red", 87654321, routing_number, 300)
account.deposit(100)
account.deposit(200)
account.withdraw(300)
print(account.add_interest())
print(account.print_balance())

account1 = BankAccount("mek", 87652321, 777444122, 200)
account1.deposit(400)
account1.deposit(500)
account1.withdraw(200)
print(account1.add_interest())
print(account1.print_balance())

account2 = BankAccount("Li", 89852321, 777441222, 100)
account2.deposit(500)
account2.deposit(700)
account2.withdraw(500)
print(account2.add_interest())
print(account2.print_balance())




