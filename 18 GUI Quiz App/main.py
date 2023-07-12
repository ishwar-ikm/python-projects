# Import necessary modules and classes
from data import *  # Import the question_data
from question_model import *  # Import the Question class
from quiz_brain import *  # Import the QuizBrain class
from ui import *  # Import the QuizUI class

# Create an empty list to store Question objects
question_bank = []

# Iterate through the question_data and create Question objects
for que in question_data:
    question_bank.append(Question(que['question'], que['correct_answer']))

# Create a QuizBrain object with the question_bank list
quiz = QuizBrain(question_bank)

# Create a QuizUI object with the quiz object
quiz_ui = QuizUI(quiz)
