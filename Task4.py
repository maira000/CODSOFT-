import random

def play_round(user_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

    if user_choice == computer_choice:
        return "It's a tie!", 0, 0
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!", 1, 0
    else:
        return "Computer wins!", 0, 1

def rock_paper_scissors_game():
    user_score = 0
    computer_score = 0
    rounds = 0

    print("Welcome to Rock-Paper-Scissors Game!")

    while True:
        user_choice = input("\nEnter your choice (rock/paper/scissors) or 'quit' to exit: ").lower()

        if user_choice == 'quit':
            print("\nThanks for playing! Final scores:")
            print(f"You: {user_score}, Computer: {computer_score}")
            break

        if user_choice in ['rock', 'paper', 'scissors']:
            result, user_win, computer_win = play_round(user_choice)
            print(result)

            user_score += user_win
            computer_score += computer_win
            rounds += 1
        else:
            print("Invalid choice. Please enter 'rock', 'paper', 'scissors', or 'quit'.")

    print(f"\nTotal Rounds: {rounds}")

if __name__ == "__main__":
    rock_paper_scissors_game()
