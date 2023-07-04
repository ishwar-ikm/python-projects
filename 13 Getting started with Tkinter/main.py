import tkinter

window = tkinter.Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)


def convert():
    m = int(text.get())
    value["text"] = round(m*1.6, 2)


text = tkinter.Entry(width=10)
text.grid(row=0, column=1)

miles = tkinter.Label(text="Miles")
miles.grid(row=0, column=2)

label1 = tkinter.Label(text="is equal to")
label1.grid(row=1, column=0)

value = tkinter.Label(text="0")
value.grid(row=1, column=1)

label2 = tkinter.Label(text="Kilometers")
label2.grid(row=1, column=2)

button = tkinter.Button(text="Calculate", command=convert)
button.grid(row=2, column=1)


window.mainloop()