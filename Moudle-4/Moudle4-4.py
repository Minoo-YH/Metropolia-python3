import random

secret = random.randint(1, 10)  # pick the number ONCE
guess = None

while guess != secret:  # repeat until the guess is correct
    guess = int(input("Guess the number (1-10): "))

    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    else:
        print("Correct")
