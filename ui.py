from tkinter import *


THEME_COLOR = "#375362"


class QuizInterface:

    def __ini__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        # self.window.config(padx=20)

        # self.canvas = Canvas(width=300, height=250, bg=THEME_COLOR, highlightthickness=0)

        self.window.mainloop()
