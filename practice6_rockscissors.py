# Rock, Paper, Scissors Game
# A logic-based console game that simulates a match between a user and the computer.

# Inputs: User selection (Rock, Paper, or Scissors).

# Logic: * Computer generates a random selection.

# Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.

# Handle ties when both selections match.

# Outputs: The computer's choice, the result of the match, and the declaration of the winner.

import random

options = ['rock', 'paper', 'scissors']
computer = random.choice(options)
user_input = input('For this epict battle, pick rock, paper or scissors: ').lower().strip()

if user_input not in options:
    print("Invalid entry!")
else:
    computer = random.choice(options)
    print(f"Computer chosen: {computer}")

    if user_input == computer:
        print("Empate!")
    elif (user_input == "rock" and computer == "scissors") or \
         (user_input == "scissors" and computer == "paper") or \
         (user_input == "paper" and computer == "rock"):
        print("You won!")
    else:
        print("Computer won!")

# Optimized IA code:

# import random

# choices = ["rock", "paper", "scissors"]
# # The dictionary acts as a lookup table: key is what you play, value is what beats it
# defeats = {"rock": "paper", "paper": "scissors", "scissors": "rock"}

# user_choice = input("Choose (rock, paper, scissors): ").lower().strip()

# if user_choice not in choices:
#     print("Invalid move!")
# else:
#     computer_choice = random.choice(choices)
#     print(f"Computer chose: {computer_choice}")

#     if user_choice == computer_choice:
#         print("It's a tie!")
#     elif defeats[user_choice] == computer_choice:
#         print("Computer wins!")
#     else:
#         print("You win!")