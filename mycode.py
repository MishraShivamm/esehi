import random

num = random.randint(1, 15)
attempt = 0

while attempt < 3:
    guess = int(input("Enter your guess: "))

    if num == guess:
        print("You guessed it right!")
        print("The number was:", num)
        break
    else:
        print("Wrong guess! Try Again.")
        attempt += 1

if attempt == 3:
    print("You are out of attempts!")
    print("The number was:", num)