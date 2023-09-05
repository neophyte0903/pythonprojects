import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # can also be high both are same
        feedback = input(
            f"is the guess {guess} too high (h/H) too low (l/L) or correct(c/C)").lower()
        if feedback == 'h':
            high = guess-1
        if feedback == 'l':
            low = guess+1
        else:
            print("invalid input")
    print("yaay i guessed it correctly")


computer_guess(10)
