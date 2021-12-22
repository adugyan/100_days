from os import system, name
from art import end_text


class QuizBrain:
    def __init__(self, question_list):
        self.q_number = 0
        self.q_list = question_list
        self.score = 0

    def still_questions_remaining(self):
        return self.q_number < len(self.q_list)

    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        user_choice = input(f"Q.{self.q_number}: {current_question.text} (True/False): ").title()
        self.check_answer(user_choice, current_question.answer)

    def check_answer(self, choice, answer):
        if choice == answer:
            print("Well done")
            self.score += 1
        else:
            print("That wasn't quite right")
        print(f"Your score is {self.score}/{self.q_number}")
        print("\n")

    def end_game_screen(self):
        self.display_art()
        print("You've completed the quiz!")
        print(f"Your final score was {self.score}/{self.q_number}")

    def display_art(self):
        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

        print(end_text)
