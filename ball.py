from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.goto(0, 0)

    def move_ball(self):
        self.forward(20)
