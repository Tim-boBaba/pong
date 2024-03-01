from turtle import Turtle
import time


class Countdown(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("red")
        self.penup()
        self.goto(0, 0)

    def count_down(self):
        self.write(f"3", True, "center", ("terminal", 36, "normal"))
        time.sleep(1)
        self.clear()
        self.goto(0, 0)
        self.write(f"2", True, "center", ("terminal", 36, "normal"))
        time.sleep(1)
        self.clear()
        self.goto(0, 0)
        self.write(f"1", True, "center", ("terminal", 36, "normal"))
        time.sleep(1)
        self.clear()
        self.goto(0, 0)
        self.write(f"Go!", True, "center", ("terminal", 36, "normal"))
        time.sleep(1)
        self.clear()
