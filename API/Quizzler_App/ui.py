from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(fg="white", text=f"Score: {self.quiz.score}", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Test",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.select_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.select_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg='white')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the round of questions!")
            self.canvas.config(bg='white')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def select_true(self):
        true_option = "True"
        is_right = self.quiz.check_answer(true_option)
        self.give_feedback(is_right)

    def select_false(self):
        false_option = "False"
        is_right = self.quiz.check_answer(false_option)
        self.give_feedback(is_right)

    def correct_answer_display(self):
        self.canvas.config(bg='green')

    def incorrect_answer_display(self):
        self.canvas.config(bg='red')

    def give_feedback(self, is_right):
        if is_right == True:
            self.correct_answer_display()
            self.window.after(1000, self.get_next_question)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.incorrect_answer_display()
            self.window.after(1000, self.get_next_question)