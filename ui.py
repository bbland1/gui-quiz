from tkinter import Button, Canvas, Label, PhotoImage, Tk
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250,
                             highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="", font=("Arial", 20, "italic"), fill="black")
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        self.wrong_button_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(
            image=self.wrong_button_img, bg=THEME_COLOR, highlightthickness=0, command=lambda x="False" :self.check_answer(x))
        self.wrong_button.grid(column=0, row=2)

        self.right_button_img = PhotoImage(file="images/true.png")
        self.right_button = Button(
            image=self.right_button_img, bg=THEME_COLOR, highlightthickness=0, command=lambda x="True" :self.check_answer(x))
        self.right_button.grid(column=1, row=2)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR,
                           font=("Arial", 10, "bold"), fg="white")
        self.score_label.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, fill="black")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz!")
            self.wrong_button.config(state="disabled")
            self.right_button.config(state="disabled")

    def check_answer(self, answer):
        self.give_feedback(self.quiz.check_answer(answer))

    def give_feedback(self, correctness):
        if correctness == True:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text, fill="white")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, fill="white")
        self.window.after(1000, self.get_next_question)
