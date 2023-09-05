import random


def play():
    print("Ram Ram bhai Sareya ne ")
    userChoice = input(
        "Whats your Choice \n r for rock p for paper s for scissors\n")
    computerChoice = random.choice(['r', 'p', 's'])

    if userChoice == computerChoice:
        return 'its a tie'

    if winner(userChoice, computerChoice):
        return 'you won'

    return 'You lost'


def winner(user, opponent):
    # return true if user wins

    if ((user == 'r' and opponent == 's') or (user == 's' and opponent == 'p') or (user == 'p' and opponent == 'r')):
        return True


print(play())
