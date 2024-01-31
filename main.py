import time
from turtle import Screen, Turtle

from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard

screen = Screen()
screen.title("PONG")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

pd1 = Paddle((-350, 0))
pd2 = Paddle((350, 0))

screen.listen()
screen.onkey(pd1.move_up, 'w')
screen.onkey(pd1.move_down, 's')
screen.onkey(pd2.move_up, 'Up')
screen.onkey(pd2.move_down, 'Down')

ball = Ball()

scoreboard = ScoreBoard()

game = True
while game:
    screen.update()
    time.sleep(0.1)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(pd1) < 50 and ball.xcor() < -320 or ball.distance(pd2) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    if ball.xcor() < -410:
        scoreboard.r_point()
        ball.reset()
    if ball.xcor() > 410:
        scoreboard.l_point()
        ball.reset()


screen.exitonclick()
