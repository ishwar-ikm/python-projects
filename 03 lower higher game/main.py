from art import *
from game_data import *
import random

print(logo)
score = 0
person = []
person.append(random.choice(data))
end = False
while not end:
    temp = random.choice(data)
    if temp in person:
        # print("running again")
        continue
    person.append(temp)
    # print(f"\n{person[len(person)-2]['follower_count']}\n{person[len(person)-1]['follower_count']}\n")

    print(f"Compare A: {person[len(person)-2]['name']}, a {person[len(person)-2]['description']}, from {person[len(person)-2]['country']}")
    print(vs)
    print(f"Against B: {person[len(person) - 1]['name']}, a {person[len(person) - 1]['description']}, from {person[len(person) - 1]['country']}")
    
    while True:
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if choice == 'a' or choice == 'b':
        break
    print("Wrong input Try Again!")
    
    if choice == 'a':
        human = len(person)-2
        other = len(person)-1
    else:
        human = len(person)-1
        other = len(person)-2

    if person[human]['follower_count'] >= person[other]['follower_count']:
        score += 1
        print(f"\nCurrent score {score}")
    else:
        end = True
        print(f"Your final score is {score}")
    if score == 50:
        print(f"You scored maximum points congratulations!")
        end = True
