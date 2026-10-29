import random
print("Welcome to the Higher/Lower game!")
#generate random number for user to guess
soln = random.randint(1,100)
#get user input
guess = int(input("Guess a number between 1 and 100: "))
while not (Guess >=1 and guess <= 100):
    guess = int(input("Invalid number. Please try again: "))
    #Determine need of guess adjustment
    if guess > soln :
        print("Lower.")
    elif guess < soln :
        print("Higher.")
    elif guess == soln:
        print("You got it boss!")
    

