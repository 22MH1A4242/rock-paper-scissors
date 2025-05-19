import random

def get_user_choice():
    user_input = input("Enter Rock, Paper, or Scissors: ").lower()
    if user_input not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Try again.")
        return get_user_choice()
    return user_input

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"
