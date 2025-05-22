import random

options = ("rock", "paper", "scissors")
running = True

while running:
    player = None

    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors) :")
    if player == computer:
        print("It's a tie!") 
    elif player == 'rock' and computer == 'scissors':
        print("You win!")
    elif player == 'scissors' and computer == 'paper':
        print("You win!")
    elif player == 'paper' and computer == 'rock':
        print("You win!")
    else:
        print("Computer wins!")
    print(f"Computer choice was {computer}")
    if not input("Do you want to play again (y/n)").lower() == "y":
        running = False
print("Thanks for playing")
    

