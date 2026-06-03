# Number Guessing Game: Logic & Rapid Thinking
# A console-based educational game designed to sharpen estimation and logical deduction skills.

# Inputs: User’s numeric guesses.

# Logic:

# System generates a secret random integer between 1 and 100.

# Input validation: Raise a ValueError for non-numeric input or integers outside the [1, 100] range.

# Feedback loop: Compare the guess to the secret number and signal "too high" or "too low" until the correct match is found.

# Outputs: Real-time guidance on guess accuracy and success confirmation upon completion.

import random

secret_number = random.randint(1, 100)
tries = 0

print('Super Guessing Game - Number Edition!')

while True: #the code needs to repeat until it reaches the last else and then breaks, that's why we have the while
    try:
        guess = int(input('Please type in your guess, a number between 1 and 100: '))
        if guess < 1 or guess > 100:
            raise ValueError
    except ValueError:
        print('Please enter a valid number between 1 and 100.\n')
        continue

    if guess > secret_number:
        print('Too high! Try again.\n')
        print(f'You did {tries} tries.')
        tries += 1
    elif guess < secret_number:
        print('Too low! Try again.\n')
        print(f'You did {tries} tries.')
        tries += 1
    else:
        print(f'YOU GOT IT after {tries} tries! The secret number was {secret_number}!')
        break