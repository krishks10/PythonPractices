import random

guess_no = random.randint(1, 100)
while True:
    try:
        user_guess = int(input("Guess the number between 1 and 100: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue
    if user_guess < guess_no:
        print("Too low! Try again.")
    elif user_guess > guess_no:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")
        break

