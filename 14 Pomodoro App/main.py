import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
ch = ""
time_down = None


# ---------------------------- TIMER RESET ------------------------------- #
# Function to reset the window
def reset_timer():
    global ch
    global time_down
    window.after_cancel(time_down)
    title.config(text="Timer", fg=GREEN)
    ch = ""
    check.config(text=ch)
    canvas.itemconfig(time, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
# Function to start the timer
def start_timer():
    global rep
    rep += 1

    # Checking of the current time is for work or for break using a rep variable
    if rep%2 == 1:
        count_down(WORK_MIN*60)
        title.config(text="Work", fg=GREEN)

    elif rep % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        title.config(text="Break", fg=RED)

    else:
        count_down(SHORT_BREAK_MIN*60)
        title.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# Function to count down the timer to the given count value which is in seconds
def count_down(count):
    global rep
    global ch
    global time_down

    # Getting the minute and seconds value out of count
    minute = str(int(count/60))
    if len(minute) < 2:
        minute = "0" + minute
    sec = str(count % 60)
    if len(sec) < 2:
        sec = "0" + sec

    canvas.itemconfig(time, text=minute+":"+sec)
    if count > 0:
        time_down = window.after(1000, count_down, count-1)
    else:
        # Add a check mark if the work time is over and call the function start_timer to start the next phase of timer
        if rep%8 == 0:
            ch = ""
            check.config(text=ch)
        elif rep%2 == 1:
            ch += "✔"
            check.config(text=ch)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
# Window for the UI
window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(padx=110, pady=60, bg=YELLOW)

# Canvas for Image
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
time = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))
canvas.grid(row=1, column=1)

# Title Label
title = tkinter.Label(text="Timer", font=(FONT_NAME, 40, 'bold'), bg=YELLOW, fg=GREEN)
title.grid(row=0, column=1)
check = tkinter.Label(font=(FONT_NAME, 20, 'normal'), bg=YELLOW, fg=GREEN)
check.grid(row=3, column=1)

# Buttons
start = tkinter.Button(text="Start", padx=5, pady=2, command=start_timer)
reset = tkinter.Button(text="Reset", padx=5, pady=2, command=reset_timer)
start.grid(row=2, column=0)
reset.grid(row=2, column=2)


window.mainloop()
