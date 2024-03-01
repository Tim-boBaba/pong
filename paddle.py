from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__()
        self.penup()
        self.goto(xcor, ycor)
        self.shape("square")
        self.color("white")
        self.shapesize(1, 3)
        self.setheading(270)
        self.last_hit = False

    # move the paddle up and down
    def move_up(self):
        if self.ycor() >= 260:
            return False
        else:
            self.penup()
            self.setheading(90)
            self.forward(20)

    def move_down(self):
        if self.ycor() <= -260:
            return False
        else:
            self.setheading(270)
            self.forward(20)

    #TODO Make function for computer paddle movement
    def computer_move_up(self):
        self.setheading(90)
        self.forward(20)

    def computer_move_down(self):
        self.setheading(270)
        self.forward(20)


