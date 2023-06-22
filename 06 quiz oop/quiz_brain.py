class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        ans = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False) ")
        self.check_ans(ans, self.question_list[self.question_number].ans)
        self.question_number += 1
        print(f"Your Current score is {self.score}/{self.question_number}")

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_ans(self, ans, correct):
        if ans.lower() == correct.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
            print(f"Correct answer was {correct}")