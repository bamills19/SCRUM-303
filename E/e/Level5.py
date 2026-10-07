#Rock paper scissors game... greet participant
import random
player_score=0
computer_score=0
rounds_played=0

print("Welcome to Rock, Paper, Scissors!")
rounds = int(input("How many rounds would you like to play? "))

#Ensure odd number of rounds
while rounds %2 == 0:
    rounds = int(input("Ensure amount of rounds are an odd number to avoid ties! Try again: "))
#List possible options
choice=["rock" , "paper" , "scissors"]

#Player choice function and computer choice function
def get_player_choice():
    while True:
         player=input("Choose Rock, Paper, or Scissors: ").lower()
         if player in choice:
            return player
         print("Invalid choice. Choose again.")

def get_computer_choice():
    
    computer=random.choice(choice)
    return computer



#Winner function
def determine_winner(player,computer):
    if player==computer:
        return "tie"
    if (player == "rock" and computer == "scissors") or \
       (player == "paper" and computer == "rock") or \
       (player == "scissors" and computer == "paper"):
        return "win"
    return "loss"

#Take results and interpret... do score count
while rounds_played<rounds:
    player=get_player_choice()
    computer=get_computer_choice()
    print(f"The computer chose {computer}.")
    result=determine_winner(player,computer)
    if result=="tie":
        print("It's a tie! Play again...")
    elif result == "win":
        print("Wow! You won.")
        player_score+=1
        rounds_played+=1
    elif result == "loss":
        print("You lost...")
        computer_score+=1
        rounds_played+=1



#With functions, defining same thing withm multiple variables.. think of Sadie and numero dog example...

#Final score and winner of the game:
print(f"Final Score: You {player_score} ----------- Computer {computer_score}")
if player_score > computer_score:
    print("Congrats! You've won the game")
else:
    print("Dang... you lost the game. Better luck next time.")