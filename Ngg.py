import random  

secret = random.randint(1, 50)
attempts = 5
won = False

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 50. You have 5 attempts.")

while attempts > 0 and not won:
    guess = int(input("\nEnter your guess: "))
    
    if guess == secret:
        print("Congratulations! You guessed the secret number!")
        won = True
    else:
        attempts -= 1
        
        diff = abs(secret - guess)
        if diff >= 20:
            hint = "ice cold"
        elif diff >= 10:
            hint = "cold"
        elif diff >= 5:
            hint = "warm"
        else:
            hint = "hot"
            
        print(f"Wrong guess! You are {hint}.")
        
        print("Remaining lives: ", end="")
        for _ in range(attempts):
    
     print() 

if not won:
    print(f"\nGame Over! You ran out of attempts. The secret number was {secret}.")