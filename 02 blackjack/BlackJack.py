import random
from art import logo
import os
clear = lambda: os.system('cls')

# Function to deal a random card from the deck
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# Function to calculate the score of a hand and handle Aces
def score(hand):
    # If the hand has a total of 21 and contains 2 cards, it's a Blackjack (0 points)
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    # If the hand has an Ace (11 points) but the total score is over 21, convert the Ace to 1 point
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

# Function to compare the scores of the user and the computer and determine the winner
def compare(user_score, computer_score):
    if user_score == 0:
        return "You Hit a Blackjack! You won"
    elif computer_score == 0:
        return "Computer hit a Blackjack! Computer won"
    elif user_score > 21:
        return "You got busted! Computer won"
    elif computer_score > 21:
        return "Computer got busted! You won"
    elif computer_score == user_score:
        return "Draw"
    elif user_score > computer_score:
        return "You Won"
    else:
        return "You Lose"

# Function to play a single round of Blackjack
def play():
    user_hand = []
    computer_hand = []
    game_over = False

    # Deal two initial cards to both the user and the computer
    for i in range(2):
        user_hand.append(deal_card())
        computer_hand.append(deal_card())

    # Calculate the scores for both the user and the computer
    user_score = score(user_hand)
    computer_score = score(computer_hand)

    # Check if either the user or the computer has a Blackjack
    if user_score == 0 or computer_score == 0:
        print(f"\nYour final hand {user_hand}, your final score {user_score}")
        print(f"Computer's final hand {computer_hand}, Computer's final score {computer_score}")
        print(compare(user_score, computer_score))
        return

    # Continue the game until it's over
    while not game_over:
        # Calculate the scores at the start of each turn
        user_score = score(user_hand)
        computer_score = score(computer_hand)
        print(f"Your cards {user_hand}, your score {user_score}")
        print(f"Computer's first card {computer_hand[0]}")

        # Check if the user or the computer has a Blackjack or busted (score >= 21)
        if user_score == 0 or computer_score == 0 or user_score >= 21:
            game_over = True
        else:
            # Ask the user if they want to hit (get another card) or stand (pass)
            if input("Type 'y' to get another card, type 'n' to pass: ").lower() == "y":
                user_hand.append(deal_card())
            else:
                game_over = True

    # If the user busted (score > 21), display the results and end the round
    if user_score > 21:
        print(f"\nYour final hand {user_hand}, your final score {user_score}")
        print(f"Computer's final hand {computer_hand}, Computer's final score {computer_score}")
        print(compare(user_score, computer_score))
        return

    # Computer's turn to hit until it reaches a score of 17 or higher
    while computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = score(computer_hand)

    # Display the results of the round and the winner
    print(f"\nYour final hand {user_hand}, your final score {user_score}")
    print(f"Computer's final hand {computer_hand}, Computer's final score {computer_score}")
    print(compare(user_score, computer_score))

# Main game loop
while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    # Clear the console for a new game
    clear()
    print(logo)
    # Start a new round of Blackjack
    play()
