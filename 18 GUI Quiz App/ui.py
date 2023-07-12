from tkinter import *
THEME_COLOR = '#375362'


class QuizUI:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("The Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0")
        self.score_label.config(bg=THEME_COLOR, fg='white', font=("arial", 12, 'normal'))
        self.score_label.grid(row=1, column=2)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, width=280, fill=THEME_COLOR, font=('arial', 20, 'italic'))
        self.canvas.grid(row=2, column=1, columnspan=2, pady=40)

        false_image = PhotoImage(file="images/false.png")
        true_image = PhotoImage(file="images/true.png")

        self.false_button = Button(image=false_image, highlightthickness=0, command=self.true_pressed)
        self.false_button.grid(row=3, column=1)

        self.true_button = Button(image=true_image, highlightthickness=0, command=self.false_pressed)
        self.true_button.grid(row=3, column=2)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg='white')
        self.score_label.config(text=f"Score: {self.quiz.score}")
        que = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=que)

    def true_pressed(self):
        self.feedback(self.quiz.check_ans(self.quiz.question_list[self.quiz.question_number].ans, "true"))

    def false_pressed(self):
        self.feedback(self.quiz.check_ans(self.quiz.question_list[self.quiz.question_number].ans, "false"))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.next_question)