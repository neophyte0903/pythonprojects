import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(
            f"is the guess {guess} too high (h/H) too low (l/L) or correct(c/C)")
