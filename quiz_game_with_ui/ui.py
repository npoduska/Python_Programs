from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = "Arial", 20, "italic"

class QuizInterface:
    
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR) 
        
        #Question text window
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Question text here",
            fill=THEME_COLOR,
            font=FONT,
            width= 280)
        
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Score Label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=FONT)
        self.score_label.grid(column=1, row=0)
        
        # # Category Label
        # self.category_label = Label(text="Category: ", fg="white", bg=THEME_COLOR, font=FONT)
        # self.category_label.grid(column=0, row=0)
        # self.canvas.itemconfig(self.question_text, text= q_text)
        
        # Setting up wrong button
        x_image = PhotoImage(file="quiz_game_with_ui\\images\\false.png")
        self.wrong_button = Button(image=x_image, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(column=1, row=2)
        # Setting up correct button
        checkmark_image = PhotoImage(file="quiz_game_with_ui\\images\\true.png")
        self.correct_button = Button(image=checkmark_image, highlightthickness=0, command=self.true_pressed)
        self.correct_button.grid(column=0, row=2)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text= "You've reached the end of the quiz.")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
            
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
        
    def false_pressed(self):
        is_right= self.quiz.check_answer("False")
        self.give_feedback(is_right)
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)