import html


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        self.question_number += 1
        return f"Q.{self.question_number}: {html.unescape(self.question_list[self.question_number].text)}"

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_ans(self, ans, correct):
        if ans.lower() == correct.lower():
            self.score += 1
            return True
        else:
            return False
