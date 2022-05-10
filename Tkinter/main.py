from tkinter import Tk, Label, Button, Entry
import turtle

window = Tk()
window.title('My first GUI Program')
window.minsize(width=500, height=300)

# Label

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label.config(text="New Text")

# Button

def button_clicked():
    print("I got clicked")
    new_label = input.get()
    my_label.config(text=new_label)


button = Button(text="Click me", command=button_clicked)
button.pack()

# Entry

input = Entry(width=10)
input.pack()

window.mainloop()