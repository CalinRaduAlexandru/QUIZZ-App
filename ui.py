from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
TITLE = ("courier", 30, "italic")

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz-app")
        self.window.config(padx=150, pady=50, bg=THEME_COLOR)

        self.score_label =  Label(text=f"Scor: {self.quiz.score}/{self.quiz.question_number} out of {len(self.quiz.question_list)}",
                                  font=("Courier", 16), fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.config(bg="white")
        self.canvas.grid(column=0, row=1, columnspan=4, pady=25)

        self.question = self.canvas.create_text(150, 125,
                                                text="lorem ipsum",
                                                fill=THEME_COLOR,
                                                font=("ariel", 16, "bold"),
                                                width=260)


        self.button_unknown = Button(text="👎", highlightthickness=0, pady=10, command=self.false_btn_pressed)
        self.button_unknown.grid(row=2, column=0)

        self.button_right = Button(text="👍", highlightthickness=0, pady=10, command=self.correct_btn_pressed)
        self.button_right.grid(row=2, column=2)

        self.retrieve_question()

        self.window.mainloop()

    def retrieve_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=f"{q_text}")
        else:
            self.canvas.config(bg="blue")
            self.canvas.itemconfig(self.question, text=f"You finished the game", fill="white")


    def correct_btn_pressed(self):
        self.give_feedback(self.quiz.check_answer("true"))


    def false_btn_pressed(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Scor: {self.quiz.score}/{self.quiz.question_number} out of {len(self.quiz.question_list)}")
        else:
            self.canvas.config(bg="red")
            self.score_label.config(text=f"Scor: {self.quiz.score}/{self.quiz.question_number} out of {len(self.quiz.question_list)}")
        self.window.after(1000, self.retrieve_question)


