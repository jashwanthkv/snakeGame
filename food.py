from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.shape("turtle")
        self.penup()
        self.color("blue")
        self.shapesize(0.8,0.8)

        self.refresh()
    def refresh(self):
        x_cor = random.randint(-350, 350)
        y_cor = random.randint(-350, 350)
        self.goto(x_cor, y_cor)