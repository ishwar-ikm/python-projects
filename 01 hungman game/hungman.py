import random
from drawing import *

chosen = random.choice(words)

display = []
length = len(chosen)

for i in range(length):
    display += "_"

print(title)
print(f"Word contains {len(chosen)} letters")
print(f" ".join(display))
print(stage[6])
end = False
lives = 6

while not end:
    user = input("Guess the word: ")
    if user in display:
        print("\nYou have already guessed the word!")

    for i in range(length):
        if user == chosen[i]:
            display[i] = user

    if user not in chosen:
        lives -= 1

    if lives == 0:
        end = True
        print("Man got killed you lost :(")
        print(stage[lives])
        print("Correct ans was: " + chosen)

    else:
        print(f" ".join(display))
        print(stage[lives])
        if "_" not in display:
            end = True
            print("You guessed the word!")