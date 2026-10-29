from Ch8fxn import BankAccount
print("Welcome to Beckham's Bank!") #import and setup
name = input("Enter your name: ")
account = BankAccount(name) #set specific account to user
#make loop
while True:
        
    print("Please choose an option: ")
    print("1. Make a deposit")
    print("2. Make a withdrawal")
    print("3. View account information")
    print("4. Quit")
    action = input()
    #add in correction to make sure input is between 1 - 4
    if action == "1" :
        amount = float(input("Enter amount here: "))
        account.deposit(amount)


    elif action == "2":
        amount = float(input("Enter amount here: "))
        account.withdrawal(amount)


    elif action == "3":
        
        account.ViewAcct()

    elif action == "4" : #break to escape loop here... acceptable use of break?
        print("Bye")
        break
    else:
        print("Invalid Choice. Please try again.") #accounting for error entry (anything not 1-4)