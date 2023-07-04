import tkinter

# Create a window for GUI
window = tkinter.Tk()
window.title("Miles to Kilometer Converter")  # Adding the title of the window
window.config(padx=20, pady=20)  # Initial pading for the components of GUI with respect to the window lines


# Function to convert miles to kilometer when the button is pressed
def convert():
    m = int(text.get())  # Get the mile value from the input text
    value["text"] = round(m*1.6, 2)  # Calculate the value and change the label


# Text object to take the input
text = tkinter.Entry(width=10)
text.grid(row=0, column=1)  # Using grid pattern to set the position of the component and every component's position is given by this method

# All the label object display the text
miles = tkinter.Label(text="Miles")
miles.grid(row=0, column=2)

label1 = tkinter.Label(text="is equal to")
label1.grid(row=1, column=0)

value = tkinter.Label(text="0")  # Label to display the calculated value
value.grid(row=1, column=1)

label2 = tkinter.Label(text="Kilometers")
label2.grid(row=1, column=2)

# Button to calculate the value by using the function convert
button = tkinter.Button(text="Calculate", command=convert)
button.grid(row=2, column=1)


window.mainloop()
