# w8d2-tp-s24-OOP1

Creating the BankAccount class.

# Class Attributes

There are two class-level variables that are initialized. "all" is a list that holds all instances of BankAccount. "account_numbers" is a list that holds all used bank account numbers. This list is referenced when a new account number is issued to a new instance of BankAccount.

# Instance Attributes

Each instance of BankAccount holds three attributes: self.accountHolder, self.accountNumber, and self.balance. Only self.accountHolder and self.balance are set by arguments to the **init** method. However, self.accountnumber is set by first generating a random number between 10000 and 99999, checking to see if the generated number has already been used, and then assigning it to the new instance. This method allows for the generation of 89999 instances of this class (this bank isn't big enough to hold more than that). The **init** method uses assert to ensure that self.accountHolder is a string and self.balance is a float. The instance is then appended to BankAccount.all in order to keep track of all instances.

# Representation

The **repr** method is used to define how an instance is represented when printed.

# Deposit

A deposit() method is defined to update a balance by adding the amount passed to the method. It then prints out the updated balance.

# Withdraw

A withdraw () method is defined to update a balance by subtracting the amount passed to the method; however, this happens only after an initial conditional test occurs that ensures that the balance is sufficient enough for the withdrawal. If not, a print statement is made stating that the balance is not enough to have the amount withdrawn.

# Balance Inquiry

A get_balance() method is defined to print the current balance of a given account.

# Display

A display_account_info() method is defined to allow account information to be displayed. This method utilizes the **repr** method to defined how information is displayed.
