from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
MAROON = "#85586F"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=75, bg=MAROON) # So that the window doesn't just contain the tomato

canvas = Canvas(width=200, height=224, bg=MAROON, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(101, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# Timer Label
timer_label = Label(text="Timer", font=(FONT_NAME, 32), fg=GREEN, bg=MAROON)
timer_label.grid(column=1, row=0)

# Buttons
start_button = Button(text="Start")  # command=start_timer
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset")  # command=reset_timer
reset_button.grid(column=2, row=2)

check_marks = Label(text="✔", fg=GREEN, bg=MAROON)
check_marks.grid(column=1, row=3)

window.mainloop()