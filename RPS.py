from RPS_game import get_user_choice, get_computer_choice, determine_winner

def play_game():
    user_score = 0
    computer_score = 0
    rounds = 0

    while True:
        user = get_user_choice()
        computer = get_computer_choice()
        result = determine_winner(user, computer)

        print(f"\nYou chose: {user}")
        print(f"Computer chose: {computer}")
        print(result)

        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1
        rounds += 1

        print(f"\nScore: You {user_score} - {computer_score} Computer (Rounds: {rounds})")

        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break
