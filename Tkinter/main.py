from tkinter import Tk, Label, Button, Entry
import turtle


def button_clicked():
    print("I got clicked")
    new_label = input.get()
    my_label.config(text=new_label)


# Window
window = Tk()
window.title('My first GUI Program')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)  # (0,0) is top left corner for place and grid

# Button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="click me too!")
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()