"""
Rock, Paper, Scissors Game
By StephVgo
"""

from random import randint

options = ["ROCK", "PAPER", "SCISSORS"]
message = {
    "tie": "It's a tie!",
    "won": "Hooray, you won!",
    "lost": "Too bad, you lost!"
}


def decide_winner(user_choice, computer_choice):
    print
    "You have chosen %s" % user_choice
    print
    "Your opponent has chosen %s" % computer_choice
    if user_choice == computer_choice:
        print
        message["tie"]
    elif user_choice == options[0] and computer_choice == options[2]:
        print
        "Rock beats scissors!"
        print
        message["won"]
    elif user_choice == options[1] and computer_choice == options[0]:
        print
        "Paper beats rock!"
        print
        message["won"]
    elif user_choice == options[2] and computer_choice == options[1]:
        print
        "Scissors beats paper!"
        print
        message["won"]
    else:
        print
        message["lost"]


def play_RPS():
    user_choice = raw_input("Enter Rock, Paper or Scissors: ")
    user_choice = user_choice.upper()
    computer_choice = options[randint(0, 2)]
    decide_winner(user_choice, computer_choice)
    play_again = raw_input("Would you like to play again? Yes/No:")
    play_again = play_again.upper()
    if play_again == "YES":
        play_RPS()
    else:
        print
        "Okay! Goodbye!"


play_RPS()
