#PROGRAM SHEET

# #Welcome player
from wordle_fxns import get_guess, choose_word, display_guess, has_won



#insert play again option
print("Welcome to mystery wordle!")
print()
print("Guess the five letter word.")
print()
print("G = Correct letter and position")
print()
print("Y = Correct letter, wrong position")
print()
print("- = letter is not in word")
print()
play_again = "yes"
while play_again == "yes":
    #computer selects secret 5 letter word
    secret_word=choose_word()
    won = False
    guesses=[]
    attempts = 1
    #loop to allow player to make 6 guesses
    while attempts <=6:
        print(f"Attempt {attempts} of 6")
        
#Comparing guesses to secret and displaying results

        guess=get_guess(guesses)
        guesses.append(guess)
        display_guess(guesses,secret_word)
        if has_won(guesses, secret_word): #win condition
            print("Correct!")
            won=True
            
            break
        attempts +=1
    if not won:
            print(f"You're out of attempts... The correct word was {secret_word}. ")
#Replay
    play_again=input("Would you like to play again? (Type yes or no )").lower()
         #Goodbye
print("See ya later!")


#player guess limited to 5 letters
