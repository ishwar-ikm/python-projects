from data import *
from question_model import *
from quiz_brain import *
from ui import *

question_bank = []
for que in question_data:
    question_bank.append(Question(que['question'], que['correct_answer']))

quiz = QuizBrain(question_bank)
quiz_ui = QuizUI(quiz)
