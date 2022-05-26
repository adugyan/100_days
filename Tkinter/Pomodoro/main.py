from tkinter import *
from math import floor

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
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_marks.config(text='', fg=GREEN, bg=MAROON)


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60

    if reps % 2 != 0 and reps < 7:
        count_down(work_time)
        timer_label.config(text="Work", fg=GREEN)
    elif reps % 2 == 0:
        count_down(short_break_time)
        timer_label.config(text="Break", fg=PINK)
    elif reps == 7:
        count_down(long_break_time)
        timer_label.config(text="Break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count: int):
    count_min = floor(count / 60)
    count_sec = count % 60
    if count_sec == 0 or count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = floor(reps / 2)
        for _ in range(work_sessions):
            marks += '✔'
        check_marks.config(text=marks, fg=GREEN, bg=MAROON)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=75, bg=MAROON)  # So that the window doesn't just contain the tomato

canvas = Canvas(width=200, height=224, bg=MAROON, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(101, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# Timer Label
timer_label = Label(text="Timer", font=(FONT_NAME, 32), fg=GREEN, bg=MAROON)
timer_label.grid(column=1, row=0)

# Buttons
start_button = Button(text="Start", command=start_timer)  # command=start_timer
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)  # command=reset_timer
reset_button.grid(column=2, row=2)

check_marks = Label(text="", fg=GREEN, bg=MAROON)
check_marks.grid(column=1, row=3)

window.mainloop()
