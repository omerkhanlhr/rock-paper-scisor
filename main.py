import random

options = ("rock", "paper", "scissors")


is_running = True

computer = random.choice(options)
while is_running:
    player = None
    while player not in options:
            player = input("Enter a choice (rock, paper, scissors): ").lower()

    print(f"\nYou chose {player}, computer chose {computer}.\n")
    if player == computer:
        print(f"Both players selected {player}. It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("Rock smashes scissors! You win!")
    elif player == "paper" and computer == "rock":
        print("Paper covers rock! You win!")
    elif player == "scissors" and computer == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("You Lose!")

    if not input("Play again? (y/n): ").lower() == "y":
        is_running = False
        print("Thanks for playing!")   