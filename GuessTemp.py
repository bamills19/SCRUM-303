import random
play_again = "y"
while play_again.lower()== "y":
    #computer picks mystery temp between -20 and 120 degrees Fahrenheit
    temp=random.randint(-20,120)
    total_guess=0
    #player makes their guess
    guess = int(input("Guess the mystery Temperature between -20 and 120 degrees Fahrenheit: "))
    while guess != temp:
        if guess > 120 or guess < -20 :
            print("Invalid guess, try again...")
            total_guess += 1
        elif guess < temp :
            print("Too low, try again!")
            total_guess += 1
        elif guess > temp:
            print("Too high, try again!")
            total_guess += 1
        guess = int(input("Guess the mystery Temperature between -20 and 120 degrees Fahrenheit: "))
#guesswork, adding to the total guess score...
    if guess == temp:
        if total_guess>1:
            print("Nice! You finally got it!")
            #putting lots of variation in the ending messages...
        if total_guess==1 :
            print("Nice! You got it!")
        print(f"It took you {total_guess} tries!")
        if total_guess <=3 :
            print("Incredible work! You've some serious talent!")
        elif total_guess == 4 or total_guess==5:
            print("Good work, not bad at all!")
        elif total_guess >=7 and total_guess <= 9:
            print("Took you long enough!")
        elif total_guess >= 10:
            print("Come on man... you can do better than that!")
#Looping the whole thing!
    print("Do you want to play again?")
    play_again = input("Press y/n : ")
#leaving them an out to cancel... says y or n but they can opress anything BUT y and it works...
print("Thanks for playing! Have a good day! :)")
