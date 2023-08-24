from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question = self.canvas.create_text(150,
                                                125,
                                                text="Hello",
                                                fill=THEME_COLOR,
                                                width=280,
                                                font=("Arial", 14, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.green_image = PhotoImage(file="images/true.png")
        self.green_button = Button(image=self.green_image, highlightthickness=0)
        self.green_button.grid(row=2, column=0)

        self.red_image = PhotoImage(file="images/false.png")
        self.red_button = Button(image=self.red_image, highlightthickness=0)
        self.red_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=q_text)
