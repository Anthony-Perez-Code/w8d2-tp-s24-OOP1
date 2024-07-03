import random

class BankAccount:
    #create a class-level variable that holds a list of all instances (instance attributes updated dyamically as changes are made)
    all = []
    #create a class-level variable that holds current available account number
    account_numbers = []
    
    #define a constructor method
    def __init__(self, accountHolder, balance):
        assert type(accountHolder) == str, f"accountHolder must be a string."
        assert type(balance) == float, f"Current balance must be a float."
        assert balance >= 0, f"Current balance must be non-negative."
        #assign a random integer in [10000,99999] as the account number (if it isn't taken already)
        while True:
            num = random.randint(10000,99999)
            if num not in BankAccount.account_numbers:
                self._accountNumber = num
                break
        self._accountHolder = accountHolder
        self._balance = balance
        BankAccount.all.append(self)

    #define a method to format how instance is displayed
    def __repr__(self):
        return f"{self._accountHolder}, {self._accountNumber}, {self._balance}"

    #define method to update balance after deposit
    #prints out updated balance
    def deposit(self, amount):
        self._balance += amount
        print(f"You have deposited ${amount}. Your new balance is ${self._balance}.")

    #define a method to update balance after withdrawal
    #if amount is exceed current balance, no money is withdrawn; otherwise, prints out updated balance
    def withdraw(self, amount):
        if amount > self._balance:
            print(f"Not enough funds to withdraw {amount}. Your balance is only {self._balance}.")
        else:
            self._balance -= amount
            print(f"You have withdrawn ${amount}. Your new balance is ${self._balance}.")

    #define a method to print out current balance
    def get_balance(self):
        print(f"{self._accountHolder}, your account with number {self._accountNumber} currently has a balance of {self._balance}.")

    #define method to display account info
    def display_account_info(self):
        print(self)

#instantiate instances of the class
account1 = BankAccount("Anthony", 100.59)
account2 = BankAccount("Harold", 43.56)
account3 = BankAccount("Henry", 1000.25)

print("Here is a listing of all current accounts.")
for i in BankAccount.all:
    print(i)

print("Currently performing some actions.")
account1.withdraw(50)
account1.get_balance()
account4 = BankAccount("Tom", 1503.34)
account4.deposit(200)

print("Here is an updated listing of all current accounts.")
for i in BankAccount.all:
    print(i)

print("Currently performing some more actions.")
account2.withdraw(100)
account5 = BankAccount("Tina", 203.45)

print("Here is an updated listing of all current accounts.")
for i in BankAccount.all:
    print(i)

print("Here is a test of the display_account_info() method.")
account1.display_account_info()