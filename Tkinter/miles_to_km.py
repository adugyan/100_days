from tkinter import *

# Window
window = Tk()
window.title('Miles to Kilometer Converter')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def button_clicked():
    print("I got clicked")
    new_answer = float(entry.get())
    print(new_answer)
    new_answer = round(new_answer * 1.609344)
    answer.config(text=f"{new_answer}")


# Labels
intro = Label(text="is equal to", font=("Arial", 12, "bold"))
intro.grid(column=0, row=2)  # (0,0) is top left corner for place and grid

answer = Label(text="0", font=("Arial", 12, "bold"))
answer.grid(column=3, row=2)
km_symbol = Label(text="Km", font=("Arial", 12, "bold"))
km_symbol.grid(column=5, row=2)
miles_symbol = Label(text="miles", font=("Arial", 12, "bold"))
miles_symbol.grid(column=5, row=1)

# Button
calculate_button = Button(text='calculate')
calculate_button.grid(column=3, row=3)
button = Button(text="calculate", command=button_clicked)

entry = Entry(width=10)
entry.grid(column=3, row=1)

window.mainloop()