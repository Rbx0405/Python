import random

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    choices = ["rock", "paper", "scissors"]
    player = input("Enter rock, paper, or scissors: ").strip().lower()
    if player not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return
    
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")
    
    result = get_winner(player, computer)
    print(result)

if __name__ == "__main__":
    play_game()
