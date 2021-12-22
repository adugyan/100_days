from Quiz_Game.quiz_game import question_model
from data import question_data
from question_model import Question
from typing import List
from quiz_brain import QuizBrain


question_bank: List[question_model.Question] = []

for data in question_data:
    question = data['text']
    answer = data['answer']
    question_bank.append(Question(question, answer))

game_set = QuizBrain(question_bank)

while game_set.still_questions_remaining():
    game_set.next_question()

game_set.end_game_screen()
