"""
Number Guessing Game
----------------------
The program picks a random number in a given range and the user tries
to guess it. Hints ('too high' / 'too low') are given after each guess,
attempts are tracked, and the user can play multiple rounds.

Author: <YOUR NAME HERE>
"""

import random


def play_round(low=1, high=100):
    """Play a single round of the guessing game and return the attempt count."""
    secret_number = random.randint(low, high)
    attempts = 0

    print(f"\nI'm thinking of a number between {low} and {high}.")

    while True:
        guess_input = input("Enter your guess: ").strip()

        if not guess_input.isdigit():
            print("Please enter a valid whole number.")
            continue

        guess = int(guess_input)
        attempts += 1

        if guess < low or guess > high:
            print(f"Please guess a number within the range {low}-{high}.")
        elif guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"\nCorrect! The number was {secret_number}.")
            print(f"It took you {attempts} attempt(s).")
            return attempts


def main():
    print("=" * 40)
    print("        NUMBER GUESSING GAME")
    print("=" * 40)

    total_rounds = 0
    total_attempts = 0

    while True:
        attempts = play_round(1, 100)
        total_rounds += 1
        total_attempts += attempts

        play_again = input("\nPlay another round? (y/n): ").strip().lower()
        if play_again != "y":
            avg = total_attempts / total_rounds
            print(f"\nThanks for playing! Rounds played: {total_rounds}, "
                  f"Average attempts: {avg:.1f}")
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
