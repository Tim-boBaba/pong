from turtle import Turtle, Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard
from count_down import Countdown

START_LOCATIONS = [(-380, 0), (380, 0)]


def is_collided(a, b, c):
    distance = b.distance(a.pos())
    radius_a = a.shapesize()[0] * c
    radius_b = b.shapesize()[0] * c
    return radius_a + radius_b >= distance


#Initiate screen
screen = Screen()
screen.tracer(2)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

#Initiate net in middle
net = Turtle()
net.penup()
net.pencolor("white")
net.hideturtle()
net.goto(0, 280)
net.setheading(270)
net.pensize(5)

for _ in range(0, 19):
    net.pendown()
    net.forward(10)
    net.penup()
    net.forward(20)

#Initiate countdown prior to starting
counter = Countdown()
counter.count_down()

#Initiate paddles
user_paddle = Paddle(START_LOCATIONS[0][0], START_LOCATIONS[0][1])
computer_paddle = Paddle(START_LOCATIONS[1][0], START_LOCATIONS[1][1])
computer_iterator = 0

#Initiate barriers
ceiling = Paddle(360, 280)
ceiling.color("black")
floor = Paddle(360, -280)
floor.color("black")

#Check for key press to move paddle up or down
screen.listen()
screen.onkeypress(user_paddle.move_down, "Down")
screen.onkeypress(user_paddle.move_up, "Up")

ball = Ball()

player_score = 0
computer_score = 0

player_scoreboard = Scoreboard(-60, 240)
player_scoreboard.score = player_score
computer_scoreboard = Scoreboard(60, 240)
computer_scoreboard.score = computer_score

game_is_on = True
player_wins = False

while game_is_on:
    screen.update()
    time.sleep(0.035)
    ball.move_ball()

    if is_collided(computer_paddle, ceiling, 20):
        computer_iterator = 1
    if is_collided(computer_paddle, floor, 20):
        computer_iterator = 0
    if computer_iterator == 1:
        computer_paddle.computer_move_down()
    if computer_iterator == 0:
        computer_paddle.computer_move_up()

    # Check for collision between either paddle and calculate which direction ball should go
    if is_collided(ball, user_paddle, 10):
        ball.setheading(0)
        user_paddle.last_hit = True
        computer_paddle.last_hit = False
    elif is_collided(ball, user_paddle, 20):
        ball.setheading(45)
        user_paddle.last_hit = True
        computer_paddle.last_hit = False
    if is_collided(ball, computer_paddle, 10):
        ball.setheading(180)
        computer_paddle.last_hit = True
        user_paddle.last_hit = False
    elif is_collided(ball, computer_paddle, 20):
        ball.setheading(135)
        computer_paddle.last_hit = True
        user_paddle.last_hit = False

    # Detect if player or computer scores if ball goes out of bounds
    if ball.xcor() >= 400:
        player_score += 1
        player_scoreboard.add_point()
        time.sleep(1)
        ball.goto(0, 0)
    elif ball.xcor() <= -400:
        computer_score += 1
        computer_scoreboard.add_point()
        time.sleep(1)
        ball.goto(0, 0)
        ball.setheading(180)

    # Check for collision of ball with ceiling/floor and determine which direction the ball should go in
    if ball.ycor() >= 280 and computer_paddle.last_hit:
        ball.setheading(225)
    elif ball.ycor() <= -280 and computer_paddle.last_hit:
        ball.setheading(135)
    elif ball.ycor() >= 280 and user_paddle.last_hit:
        ball.setheading(315)
    elif ball.ycor() <= -280 and user_paddle.last_hit:
        ball.setheading(45)

    # Detect if max score of 5 has been reached by either user or computer and determine winner
    if player_score == 5:
        game_is_on = False
        player_wins = True
    elif computer_score == 5:
        game_is_on = False
        player_wins = False

#Determine winner and show final score
if not game_is_on:
    if player_wins:
        print("Game Over. You win!")
        print(f"Final scores:")
        print(f"Your score: {player_score}")
        print(f"Computer score: {computer_score}")
    elif not player_wins:
        print("Game over. You lose!")
        print(f"Final scores:")
        print(f"Your score: {player_score}")
        print(f"Computer score: {computer_score}")

screen.exitonclick()
screen.mainloop()
