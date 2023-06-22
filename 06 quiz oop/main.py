from data import *
from question_model import *
from quiz_brain import *

question_bank = []
for que in question_data:
    question_bank.append(Question(que['text'], que['answer']))

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
    print("")

print(f"The quiz is complete and your final score was {quiz.score}/{len(question_bank)}")
