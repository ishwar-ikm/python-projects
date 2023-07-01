import turtle
import pandas

##############################################
# Used to get the co-ordinates of every state
# def get_coor(x, y):
#     print(f"{x}, {y}")
# sc.onclick(get_coor)
##############################################

# Setting up screen
sc = turtle.Screen()
sc.title("Guess The Indian State Game")
image = "india-blank-map.gif"  # Saving image location
sc.addshape(image)  # Adding image to the shape
turtle.shape(image)  # Turtle shape is now in the shape of the image


# This function is used to write the state name at the correct location on the image
def write_state(name, x, y):
    tim = turtle.Turtle()
    tim.hideturtle()
    tim.up()
    tim.color("black")
    tim.goto(x, y)
    tim.write(f"{name}", align="left", font=("Arial", 10, 'normal'))


# Using pandas library the indian state data is extracted
data = pandas.read_csv("states.csv")
# states contains list of all the indian states
states = data['states'].to_list()

guessed = []  # List to store the state already guessed
title = "Guess the state"  # Set the initial title of the pop up window of text input

while len(guessed) < 28:
    user_input = sc.textinput(title=title, prompt="Enter the name of the state. (UT not included)").lower()  # Take the user input
    if user_input in states and user_input not in guessed:  # Check the condition if the state is present or not and if the state is already guessed
        write_state(user_input, int(data[data.states == user_input].x), int(data[data.states == user_input].y))  # Call the write_state
        guessed.append(user_input)  # append the guessed list
    title = f"{len(guessed)}/28 guessed so far"  # Update the title
write_state("Congratulations you have guessed every \nsingle state in india", 80, -140)  # Display greeting message after the game is over
turtle.mainloop()
