import random
from drawing import *

# Choose a random word from the predefined list 'words'
chosen = random.choice(words)

# Create a list 'display' to represent the word to be guessed with underscores
display = []
length = len(chosen)

for i in range(length):
    display += "_"

# Display the title, word length, and initial state of the drawing
print(title)
print(f"Word contains {len(chosen)} letters")
print(f" ".join(display))
print(stage[6])

# Initialize game variables
end = False
lives = 6

while not end:
    # Get the user's guess as input
    user = input("Guess the word: ")

    # Check if the guessed letter is already revealed in the 'display'
    if user in display:
        print("\nYou have already guessed the letter!")

    # Update the 'display' list to reveal correctly guessed letters in their appropriate positions
    for i in range(length):
        if user == chosen[i]:
            display[i] = user

    # Decrease the remaining lives if the guessed letter is not in the word
    if user not in chosen:
        lives -= 1

    # Check if the player has lost all lives and end the game if true
    if lives == 0:
        end = True
        print("Man got killed, you lost :(")
        print(stage[lives])
        print("Correct answer was: " + chosen)

    else:
        # Display the current state of the 'display' and the drawing
        print(f" ".join(display))
        print(stage[lives])

        # Check if all the letters are guessed correctly and end the game if true
        if "_" not in display:
            end = True
            print("Congratulations! You guessed the word!")
