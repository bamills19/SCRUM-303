
#randomly generate number between 1 and 100. Count is 0
import random
secret = random.randint(1,100)
total_guess = 0
#Player guesses a number between 1 and 100
while True:
    guess = int(input("Pick a number between 1 and 100!"))
total_guess+=0
    #Too low, tell player to guess higher
    if guess > secret:
    print("Too low! Try again...")

    #Too high, tell player to guess lower
    if guess < secret:
    print("Too high! Try again...")
    #Invalid answer, 
    if guess == secret:
    Print("You got it!")
    Print(f"Your guess count was {total_guess}!")
    Print("If you want to play again, press y")
    input()




    