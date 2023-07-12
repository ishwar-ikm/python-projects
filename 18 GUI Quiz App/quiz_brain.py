import html


class QuizBrain:
    def __init__(self, question_list):
        """
        Initializes a QuizBrain object with the provided question list.

        :param question_list: A list of Question objects representing the quiz questions.
        """
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        """
        Retrieves the next question from the question list.

        :return: A formatted string representing the next question.
        """
        self.question_number += 1
        return f"Q.{self.question_number}: {html.unescape(self.question_list[self.question_number].text)}"

    def still_has_question(self):
        """
        Checks if there are any remaining questions in the quiz.

        :return: True if there are more questions, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def check_ans(self, ans, correct):
        """
        Checks if the provided answer matches the correct answer and updates the score accordingly.

        :param ans: The user's answer.
        :param correct: The correct answer.
        :return: True if the answer is correct, False otherwise.
        """
        if ans.lower() == correct.lower():
            self.score += 1
            return True
        else:
            return False
