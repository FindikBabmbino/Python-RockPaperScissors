import random

def PrintPicks(computer,player):
    print("computer: {}".format(computer))
    print("player: {}".format(player))


def ShowChoices(player,computer):
    if player == computer:
        PrintPicks(computer, player)
        print("Tie!")
    elif player == "rock":
        PrintPicks(computer, player)
        if computer == "paper":
            print("You Lose!")
        else:
            print("You win!")

    elif player == "paper":
        PrintPicks(computer, player)
        if computer == "scissors":
            print("You Lose!")
        else:
            print("You win!")

    elif player == "scissors":
        PrintPicks(computer, player)
        if computer == "rock":
            print("You Lose!")
        else:
            print("You win!")


def RunGame():
    while True:
        choices=["rock","paper","scissors"]
        computer=random.choice(choices)
        player=None
        while player not in choices:
            player = input("rock,paper, or scissors?: ").lower()
        ShowChoices(player,computer)
        continuePlaying=None
        while continuePlaying != "yes" and continuePlaying != "no":
            continuePlaying=input("Continue playing? (yes/no): ").lower()
        if continuePlaying=="yes":
            continue
        elif continuePlaying=="no":
            break
