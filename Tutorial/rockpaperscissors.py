# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
# and ask if the players want to start a new game)
#
# Remember the rules:
#
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

player_1 = input("Player 1 pick between Rock, Paper and Scissors: ").lower()

player_2 = input("Player 2 pick between Rock, Paper and Scissors: ").lower()

if player_1 == 'rock' and player_2 == 'scissors':
    print(f"Congratulations Player 1! You WON!!! Rock beat Scissors")
elif player_1 == 'scissors' and player_2 == 'paper':
    print(f"Congratulations Player 1! You WON!!! Scissors beat Paper")
elif player_1 == 'paper' and player_2 == 'rock':
    print(f"Congratulations Player 1! You WON!!! Paper beat Rock")
elif player_1 == 'scissors' and player_2 == 'rock':
    print(f"Congratulations Player 2! You WON!!! Rock beat Scissors")
elif player_1 == 'paper' and player_2 == 'scissors':
    print(f"Congratulations Player 2! You WON!!! Scissors beat Paper")
elif player_1 == 'rock' and player_2 == 'paper':
    print(f"Congratulations Player 1! You WON!!! Paper beat Rock")
else:
    print(f"Sadly, there is no winner")


import sys

user1 = input("What's your name?")
user2 = input("And your name?")
user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)


def compare(u1, u2):
    if u1 == u2:
        return "It's a tie!"
    elif u1 == 'rock':
        if u2 == 'scissors':
            return "Rock wins!"
        else:
            return "Paper wins!"
    elif u1 == 'scissors':
        if u2 == 'paper':
            return "Scissors win!"
        else:
            return "Rock wins!"
    elif u1 == 'paper':
        if u2 == 'rock':
            return "Paper wins!"
        else:
            return "Scissors win!"
    else:
        return "Invalid input! You have not entered rock, paper or scissors, try again."
        sys.exit()


print(compare(user1_answer, user2_answer))
