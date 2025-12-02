# Task 2 - Number Guessing Game
# This program generates a random number and allows the user to guess it with hints.
# Includes difficulty levels and maximum attempt limits.

import random

def number_guessing_game():
    print("🎮 Welcome to the Number Guessing Game!")

    # Choose difficulty level
    print("\nSelect Difficulty Level:")
    print("1. Easy (1 - 50)")
    print("2. Hard (1 - 200)")

    choice = input("Enter 1 for Easy or 2 for Hard: ")

    # Set range based on difficulty
    if choice == "1":
        number = random.randint(1, 50)
        max_attempts = 7
        print("\nYou selected EASY difficulty (Range: 1-50)")
    elif choice == "2":
        number = random.randint(1, 200)
        max_attempts = 10
        print("\nYou selected HARD difficulty (Range: 1-200)")
    else:
        print("Invalid choice! Starting Easy mode by default.")
        number = random.randint(1, 50)
        max_attempts = 7

    attempts = 0

    # Game logic loop
    while attempts < max_attempts:
        attempts += 1
        try:
            guess = int(input(f"\nAttempt {attempts}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("⚠ Invalid input! Please enter a valid number.")
            continue

        # Check guess
        if guess > number:
            print("📉 Too High!")
        elif guess < number:
            print("📈 Too Low!")
        else:
            print(f"🎉 Correct! You guessed the number in {attempts} attempts!")
            break
    else:
        print(f"\n❌ Game Over! You've used all attempts.\nThe correct number was: {number}")

# Start game
number_guessing_game()
