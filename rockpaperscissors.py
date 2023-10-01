
import random

def play_game(num_rounds):
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0

    for round_num in range(1, num_rounds + 1):
        print(f"Round {round_num}:")
        print("Choices: rock, paper, scissors")

        # Computer's choice
        computer_choice = random.choice(choices)

        # User's choice
        user_choice = input("Your choice: ").lower()

        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            return

        print(f"Computer's choice: {computer_choice}")

        # Determine the winner of the round
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        # Check if a player has won the game
        if user_score >= 2 or computer_score >= 2:
            print("Game over!")
            if user_score > computer_score:
                print("You win the game!")
            elif user_score < computer_score:
                print("Computer wins the game!")
            else:
                print("It's a tie!")

            return

# Prompt the user for the number of rounds (3 or 5)
num_rounds = int(input("Enter the number of rounds (3 or 5): "))

if num_rounds not in [3, 5]:
    print("Invalid number of rounds. Please choose 3 or 5.")
else:
    play_game(num_rounds)