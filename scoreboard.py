from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, xcor, ycor):
        self.group_scores = []
        self.xcor = xcor
        self.ycor = ycor
        self.score = 0
        self.create_board()


    def create_board(self):
        this_board = Turtle()
        self.group_scores.append(this_board)
        this_board.penup()
        this_board.hideturtle()
        this_board.pencolor("white")
        this_board.goto(self.xcor, self.ycor)
        this_board.write(f"{self.score}", True, "center", ("terminal", 36, "normal"))

    def add_point(self):
        self.group_scores[0].clear()
        self.group_scores.pop(0)
        t_board = Turtle()
        self.score += 1
        t_board.penup()
        t_board.hideturtle()
        t_board.goto(self.xcor, self.ycor)
        t_board.pencolor("white")
        t_board.write(f"{self.score}", True, "center", ("terminal", 36, "normal"))
        self.group_scores.append(t_board)
