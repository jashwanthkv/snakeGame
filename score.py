from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score=0
        self.hideturtle()
        self.penup()
        self.goto(0,380)
        self.write(f"Score is: {self.score}",align="center",font=("Arial",14,"normal"))
    def update(self):
        self.score+=1
        self.clear()
        self.write(f"Score is: {self.score}", align="center", font=("Arial",14, "normal"))
    def over(self):
        self.goto(0,0)
        self.write("GAME OVER!!",align="center",font=("Arial",24,"normal"))