#Exercise :Write a program to guess a number between 1 to 9.
import random

def guess_number():
    number_to_guess = random.randint(1, 9)
    attempts = 0
    max_attempts = 3

    print("Guess a number between 1 and 9. You have 3 attempts.")

    while attempts < max_attempts:
        try:
            user_guess = int(input("Enter your guess: "))
            if user_guess < 1 or user_guess > 9:
                print("Please guess a number between 1 and 9.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        attempts += 1

        if user_guess == number_to_guess:
            print(f"Congratulations! You've guessed the correct number {number_to_guess} in {attempts} attempts.")
            return
        else:
            print(f"Wrong guess. You have {max_attempts - attempts} attempts left.")

    print(f"Sorry, you've used all your attempts. The correct number was {number_to_guess}.")