import random
import tkinter

import pandas

BACKGROUND_COLOR = "#B1DDC6"
word = {}  # Variable to store the current word or phrase

try:
    file = pandas.read_csv("data/words_to_learn.csv")  # Try to read the learned words from a CSV file
except FileNotFoundError:
    original = pandas.read_csv("data/hindi_words.csv")  # If the file is not found, read the original word data
    data = original.to_dict(orient="records")  # Convert the word data to a list of dictionaries
else:
    data = file.to_dict(orient="records")  # If the file is found, convert the data to a list of dictionaries


# ------------ Data Visualization ------------ #

def next_word():
    """
    Display the next word or phrase on the flashcard.
    """
    global timer, word
    window.after_cancel(timer)  # Cancel the previous timer
    canvas.itemconfig(bg_img, image=img)  # Set the front image of the flashcard
    word = random.choice(data)  # Select a random word or phrase
    canvas.itemconfig(title, text="Hindi", fill='black')  # Set the title to "Hindi" and text color to black
    canvas.itemconfig(text, text=word['hindi'], fill='black')  # Set the text to the Hindi word or phrase
    timer = window.after(3000, eng_word)  # Schedule the timer to switch to the English translation


def eng_word():
    """
    Display the English translation of the word or phrase on the flashcard.
    """
    canvas.itemconfig(title, text="English", fill='white')  # Set the title to "English" and text color to white
    canvas.itemconfig(text, text=word['english'], fill='white')  # Set the text to the English translation
    canvas.itemconfig(bg_img, image=img3)  # Set the back image of the flashcard


def known():
    """
    Mark the current word or phrase as known and move to the next flashcard.
    """
    data.remove(word)  # Remove the word or phrase from the data set
    print(len(data))  # Print the remaining number of words or phrases
    to_learn = pandas.DataFrame(data)  # Create a DataFrame from the updated data set
    to_learn.to_csv("data/words_to_learn.csv", index=False)  # Save the updated data set to a CSV file
    next_word()  # Move to the next flashcard


# ------------ UI ------------ #

window = tkinter.Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, eng_word)  # Schedule the initial timer to switch to the English translation

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img = tkinter.PhotoImage(file="images/card_front.png")
img3 = tkinter.PhotoImage(file="images/card_back.png")
bg_img = canvas.create_image(400, 263, image=img)  # Create the flashcard image
title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))  # Create the title text
text = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))  # Create the word text
canvas.grid(row=1, column=1, columnspan=2)

img1 = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=img1, highlightthickness=0, command=known)  # Create the "✓" button
right_button.grid(row=2, column=2)

img2 = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=img2, highlightthickness=0, command=next_word)  # Create the "✗" button
wrong_button.grid(row=2, column=1)

next_word()  # Display the first flashcard

window.mainloop()
