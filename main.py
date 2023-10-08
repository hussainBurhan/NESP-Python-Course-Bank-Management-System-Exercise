# Import the datetime module for handling dates and times
import datetime

# Define a class named 'Account'
class Account():
    
    # Define a static method 'current_time' to get the current date and time
    @staticmethod
    def current_time(self):
        return datetime.datetime.now()

    # Initialize the Account object with a name and initial balance
    def __init__(self, name, balance):
        # Private variables for name, balance, and transaction history
        self.__name = name
        self.__balance = balance
        self.__trans_list = [(Account.current_time(self), balance)]
        print(f'Account created for {name} with balance {balance} dollars')
        
    # Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0 :
            self.__balance += amount
            self.show()
            self.__trans_list.append((Account.current_time(self), amount))
    
    # Method to withdraw money from the account
    def withdraw(self, amount):
        if 0 < amount <= self.__balance :
            self.__balance -= amount
            self.show()
            self.__trans_list.append((Account.current_time(self), (-1*amount)))
        else:
            print(f'{self.__name} You are Bankrupt')            
    
    # Method to display the current balance
    def show(self):
        print(f'{self.__name} Your balance is {self.__balance}')
        
    # Method to display the transaction history
    def show_trans_list(self):
        for date, amount in self.__trans_list:
            if amount > 0 :
                trans_type = 'Deposit'
            else:
                trans_type = 'Withdraw'
                amount *= -1
            print(f'Amount {amount} dollars, {trans_type} on {date}')

# Create an instance of the Account class for 'Hussain' with an initial balance of 50 dollars
Hussain = Account('Hussain', 50)

# Deposit 200 dollars into the account
Hussain.deposit(200)

# Withdraw 150 dollars from the account
Hussain.withdraw(150)

# Display the transaction history
Hussain.show_trans_list()

# Attempt to withdraw 150 dollars, but it will fail due to insufficient funds
Hussain.withdraw(150)
