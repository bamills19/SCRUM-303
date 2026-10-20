#FXNS SHEET

#string by nature in python is an array of letters


import random
#having computer choose the secret word from pre-arranged list
def choose_word():
    
    words = ["lives", "poker", "beach", "dirty", "earth", "fruit", "quiet", "river", "brain", "smile"]
    secret = random.choice(words)
    return secret


#get the players guess--if not 5 words have them redo it.
def get_guess(guesses):
    while True:
            
        guess=input("Guess the five letter word: ").lower()
        if len(guess) != 5 :
            print("Try again... Your guess must be 5 letters.")
        elif guess in guesses:
            print("You already tried that word, use another one.")
        else:
            return guess

def evaluate_guess(guess, secret_word): 
    result = ""
    for i in range(len(guess)):
        if guess[i] ==secret_word[i]:
            result += "G"
        elif guess[i] in secret_word:
            result += "Y"
        else:
            result += "-"
    return result


def display_guess(guesses, secret_word):
    for guess in guesses:
        print(" ".join(guess.upper()))
        print(evaluate_guess(guess,secret_word))
        print(" ")


#evaluating player guess and comparing to player guess  ********NOT DONE*****



