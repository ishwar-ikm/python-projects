from art import *
from game_data import *
import random

# Display the game logo
print(logo)

# Initialize the score variable to keep track of the user's score
score = 0

# Create a list 'person' and add one random data entry from 'data' to it
person = []
person.append(random.choice(data))

# Variable 'end' to control the game loop
end = False

# Main game loop
while not end:
    # Choose a new random data entry 'temp'
    temp = random.choice(data)

    # Check if 'temp' is already in 'person', if yes, continue to get a new random data entry
    if temp in person:
        continue
    person.append(temp)

    # Display the names, descriptions, and countries of the two data entries to compare
    print(f"Compare A: {person[len(person)-2]['name']}, a {person[len(person)-2]['description']}, from {person[len(person)-2]['country']}")
    print(vs)
    print(f"Against B: {person[len(person) - 1]['name']}, a {person[len(person) - 1]['description']}, from {person[len(person) - 1]['country']}")

    # Ask the user to input their choice 'A' or 'B'
    while True:
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if choice == 'a' or choice == 'b':
            break
        print("Wrong input. Try Again!")

    # Assign indices for the chosen data entries for comparison
    if choice == 'a':
        human = len(person)-2
        other = len(person)-1
    else:
        human = len(person)-1
        other = len(person)-2

    # Check if the user's chosen entry has more followers than the other entry
    # Update the score accordingly and display the current score
    if person[human]['follower_count'] >= person[other]['follower_count']:
        score += 1
        print(f"\nCurrent score: {score}")
    else:
        # If the user's chosen entry has fewer followers, end the game
        end = True
        print(f"Your final score is: {score}")

    # Check if the user has scored the maximum points (50) and end the game if true
    if score == 50:
        print(f"Congratulations! You scored the maximum points!")
        end = True
