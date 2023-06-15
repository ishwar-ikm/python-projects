import random
from art import logo
import os
clear = lambda: os.system('cls')

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def score(list):
    if sum(list) == 21 and len(list) == 2:
        return 0
    if 11 in list and sum(list) > 21:
        list.remove(11)
        list.append(1)
    return sum(list)

def compare(user, computer):
    if user == 0:
        return "You Hit a Black Jack! You won"
    elif computer == 0:
        return "Computer hit a Black Jack! Computer won"
    elif user > 21:
        return "You got busted! Computer won"
    elif computer > 21:
        return "Computer got busted! You won"
    elif computer == user:
        return "Draw"
    elif user > computer:
        return "You Won"
    else:
        return "You Lose"


def play():
    user_card = []
    computer_card = []
    game_over = False

    for i in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    user_score = score(user_card)
    computer_score = score(computer_card)

    if user_score == 0 or computer_score == 0:
        print(f"\nYour final hand {user_card}, your final score {user_score}")
        print(f"Computer's final hand {computer_card}, Computer's final score {computer_score}")
        print(compare(user_score, computer_score))
        return

    while not game_over:
        user_score = score(user_card)
        computer_score = score(computer_card)
        print(f"Your cards {user_card}, your score {user_score}")
        print(f"Computer's first card {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score >= 21:
            game_over = True
        else:
            if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
                user_card.append(deal_card())
            else:
                game_over = True

    if user_score > 21:
        print(f"\nYour final hand {user_card}, your final score {user_score}")
        print(f"Computer's final hand {computer_card}, Computer's final score {computer_score}")
        print(compare(user_score, computer_score))
        return

    while computer_score < 17:
        computer_card.append(deal_card())
        computer_score = score(computer_card)

    print(f"\nYour final hand {user_card}, your final score {user_score}")
    print(f"Computer's final hand {computer_card}, Computer's final score {computer_score}")
    print(compare(user_score, computer_score))

while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    print(logo)
    play()