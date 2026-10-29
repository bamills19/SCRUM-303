#FXN SHEET
import random
class BankAccount: #making account class
#Deposits
    def __init__(self,name):   #Properties of account through __init__
        self.balance = 0.00
        self.name = name
        self.acct_num = random.randint(1000,9999)

    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited {amount:.2f}.")
        print(f"Your balance is now {self.balance:.2f}.")

    #Withdraw money return balance
    def withdrawal(self, amount):
        if self.balance < amount :
            print("Insufficient funds.")
        else:
            self.balance -=amount
            print(f"Withdrew {amount:.2f}.")
            print(f"Your balance is now {self.balance:.2f}.")

    #Viewing and printing account summary.
    def ViewAcct(self):
        print("ACCOUNT SUMMARY")
        print(f"Name: {self.name}")
        print(f"Account #: {self.acct_num}")
        print(f"Balance: {self.balance:.2f}")
        #We dont need to set variables in self in parameter cause self will pass them all in!