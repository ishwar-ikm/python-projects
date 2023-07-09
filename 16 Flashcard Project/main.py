import random
import tkinter

import pandas

BACKGROUND_COLOR = "#B1DDC6"
word = {}

try:
    file = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original = pandas.read_csv("data/hindi_words.csv")
    data = original.to_dict(orient="records")
else:
    data = file.to_dict(orient="records")


# ------------ Data Visualisation ------------ #
def next_word():
    global timer, word
    window.after_cancel(timer)
    canvas.itemconfig(bg_img, image=img)
    word = random.choice(data)
    canvas.itemconfig(title, text="Hindi", fill='black')
    canvas.itemconfig(text, text=word['hindi'], fill='black')
    timer = window.after(3000, eng_word)


def eng_word():
    canvas.itemconfig(title, text="English", fill='white')
    canvas.itemconfig(text, text=word['english'], fill='white')
    canvas.itemconfig(bg_img, image=img3)


def known():
    data.remove(word)
    print(len(data))
    to_learn = pandas.DataFrame(data)
    to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_word()


# ------------ UI ------------ #
window = tkinter.Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, eng_word)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img = tkinter.PhotoImage(file="images/card_front.png")
img3 = tkinter.PhotoImage(file="images/card_back.png")
bg_img = canvas.create_image(400, 263, image=img)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=1, column=1, columnspan=2)

img1 = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=img1, highlightthickness=0, command=known)
right_button.grid(row=2, column=2)

img2 = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=img2, highlightthickness=0, command=next_word)
wrong_button.grid(row=2, column=1)

next_word()

window.mainloop()
