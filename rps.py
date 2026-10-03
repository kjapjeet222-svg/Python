import random

choices = ["rock", "paper", "scissors"]
print("Welcome to Rock, Paper, scissors!")

while True:
 player = input("Enter rock, paper, or scissors (or 'quit' to stop):").lower()

 if player== "quit":
    print("Thanks for playing!")

 if player not in choices:
    print("Invalid choice. Please try again.")
    continue
 computer= random.choice(Choices)
 print(f"computer chose: {computer}")

 if player == computer:
    print("It's a tie!")

 elif (player == "rock" and computer=="scissors" or  \ ) 
       (player == "paper" and computer=="rock") or\
       (player== "scissors" and computer=="paper"):
print("You win!")
else:
   print("Computer Wins!")
print("_" * 20)
       
