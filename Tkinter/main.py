import tkinter
import turtle

window = tkinter.Tk()
window.title('My first GUI Program')
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()

tim = turtle.Turtle()
tim.write()
window.mainloop()