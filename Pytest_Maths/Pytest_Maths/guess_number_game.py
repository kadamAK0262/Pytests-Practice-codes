import random

def guess_number(secret_number, guess):
    if guess == secret_number:
        return "Congratulations! You guessed the number correctly!"
    elif guess < secret_number:
        return "Too low. Try again."
    else:
        return "Too high. Try again."
