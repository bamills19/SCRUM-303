#Loop for replaying, lowercase.
play_again = "y"
while play_again.lower() == "y" :
        
    #randomly generate number between 1 and 100. Count is 0
    import random
    secret = random.randint(1,100)
    total_guess = 0
    #Player guesses a number between 1 and 100
    guess=int(input("Guess a number between 1 and 100: "))
    while guess != secret :
        if guess > 100 or guess < 1 :
            print("Invalid, try again!")
            total_guess += 1
        elif guess < secret :
            print("Too low, try again!")
            total_guess += 1
        elif guess > secret :
            print("Too high, try again!")
            total_guess += 1
        guess = int(input("Try again!"))
    #Player guesses correctly, they move past the loop. Print results and congratulations!
    if guess == secret :
        #== vs = when to use?
        print("Nice work, you got it!")
        print(f"It took you {total_guess} guesses!")
    #Guess count results...
    if total_guess <= 3 :
        print("Excellent work, my friend!")
    elif total_guess == 4 or total_guess == 5 :
        print("Amazing job!")
    elif total_guess == 6 or total_guess == 7 :
        print("Nice work!")
    elif total_guess == 8 or total_guess==9:
        print("Took a while, but you finally got it!")
    elif total_guess >= 10 :
        print("Took ya long enough...")
#Loop to play again if they want, if not, thank for playing and end it.
    print("Would you like to play again?")
    input("If so, press Y : ")

print("Thanks for playing!")









    #While if its invalid.... so it keeps going back
    #then once its valid itll move on to the if elif elif sequence
    #git commit -m "Testing"