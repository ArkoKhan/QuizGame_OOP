from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.windows = Tk()
        self.windows.title("Quiz")
        self.windows.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score : 0", fg="#ffffff", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1, sticky="e", pady=10,)
        self.canvas = Canvas(width=300, height=250, bg="#ffffff")
        self.question_text = self.canvas.create_text(150,125,text="question?", fill=THEME_COLOR,
                                                     font=("arial", 18, "italic"),
                                                     width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=(10, 20))

        ture_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=ture_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0,sticky="w")
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1,sticky="e")

        self.get_next_question()

        self.windows.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_question():
            self.canvas.config(bg="#ffffff")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text= "That's All Folks")
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.windows.after(1500, self.get_next_question)

